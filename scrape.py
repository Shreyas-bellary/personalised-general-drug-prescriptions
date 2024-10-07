from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import csv
import os
import re
import datetime
import requests
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor


# Function to get the HTML of a webpage
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve {url}")
        return None

# Function to scrape treatment options from the main page
def get_treatment_options(url):
    response = get_html(url)
    soup = BeautifulSoup(response, 'html.parser')
    head = soup.head
    if head:
        head.extract()

    treatment_options = soup.find_all('ul', class_="ddc-list-column-4")
    new_soup = BeautifulSoup(str(treatment_options), 'html.parser')
    disease_list = []
    disease_links = []
    all_diseases = new_soup.find_all('a')

    for disease in all_diseases:
        disease_text = disease.get_text(strip=True)
        if disease_text == "Weight Loss":
            disease_list.append("Obesity")
            disease_links.append("https://www.drugs.com" + disease['href'])
        elif disease_text == "Incontinence":
            disease_list.append("Urinary Incontinence")
            disease_links.append("https://www.drugs.com" + disease['href'])
        elif disease_text != "Mental Health":
            disease_list.append(disease_text)
            disease_links.append("https://www.drugs.com" + disease['href'])
    
    disease_list.append("Fever")
    disease_links.append("https://www.drugs.com/condition/fever.html")
    return disease_list, disease_links

# Function to scrape detailed drug info for each link
def get_detailed_drug_info(url):
    Bname = []
    mg = []
    allergy = []

    response = get_html(url)
    if response is None:
        return Bname, mg, allergy

    soup = BeautifulSoup(response, 'html.parser')
    content = soup.find("p", class_="drug-subtitle")
    
    if content:
        content_str = content.get_text(separator=" ", strip=True)
        start_pos = content_str.find("Brand names:")
        if start_pos == -1:
            start_pos = content_str.find("Brand name:")

        # Stop extraction at "show all" if present
        end_pos_show_all = content_str.find("... show all")
        # Handle both "Dosage form" and "Dosage forms"
        end_pos_dosage_form = content_str.find("Dosage form:")
        if end_pos_dosage_form == -1:
            end_pos_dosage_form = content_str.find("Dosage forms:")

        end_pos_drug_class = content_str.find("Drug class:")

        # Determine the valid end position
        end_pos = min(end_pos_dosage_form, end_pos_drug_class) if end_pos_dosage_form != -1 and end_pos_drug_class != -1 else max(end_pos_dosage_form, end_pos_drug_class)
        if end_pos == -1:
            end_pos = len(content_str)

        # If "show all" is found, limit text to just before "show all"
        if end_pos_show_all != -1 and end_pos_show_all < end_pos:
            end_pos = end_pos_show_all

        if start_pos != -1:
            brand_names_section = content_str[start_pos:end_pos].strip()
            brand_names_only = brand_names_section.split(":", 1)[1].strip()
            brand_names_only = brand_names_only.replace(',', ';')
            Bname.append(brand_names_only)
        else:
            Bname.append(None)
    else:
        Bname.append(None)

    sidebox = soup.find('div', class_='ddc-sidebox ddc-sidebox-drug-image')
    if sidebox:
        figcaption = sidebox.find('figcaption')
        mg_value = re.search(r'\d+ mg', figcaption.text)
        mg.append(mg_value.group() if mg_value else None)
    else:
        mg.append(None)

    target_paragraph = soup.find("h2", id="before-taking", string="Before taking this medicine")
    if target_paragraph:
        ul_element = target_paragraph.find_next("ul")
        new_soup = BeautifulSoup(str(ul_element), 'html.parser')
        li_elements = ul_element.find_all('li')
        if li_elements:
                for ele in li_elements:
                    cleaned_text = ele.get_text(strip=True)           
                    # Split based on " or " and " or"
                    cleaned_text = cleaned_text.replace(';', '')
                    cleaned_text = cleaned_text.replace('.', '')
                    # Remove 'or' at the end of the sentence if it exists
                    cleaned_text = cleaned_text.rstrip(' or')
                    allergy.append(cleaned_text)
        else:
            allergy.append(None)
    else:
        allergy.append(None)
    return Bname, mg, allergy



# Function to scrape data for a single drug link
def scrape_drug_info(link, disease):
    response = get_html(link + "?page_all=1")
    soup = BeautifulSoup(response, 'html.parser')
    medicines = soup.find_all(class_="ddc-table-row-medication data-table-row")

    results = []
    for medicine in medicines:
        new_soup = BeautifulSoup(str(medicine), 'html.parser')
        drug_name = new_soup.find('a', class_="ddc-text-wordbreak").get_text(strip=True)
        dlink = "https://www.drugs.com" + new_soup.find('a', class_="ddc-text-wordbreak")['href']

        rate = new_soup.find('td', class_="ddc-text-center").get_text(strip=True)
        rate = None if rate == "Rate" else rate

        rev = new_soup.find('a', class_="ddc-text-nowrap").get_text(strip=True).split()[0]
        rev = None if rev == "Add" else rev

        activity_div = new_soup.find(class_="ddc-rating-bar")
        act = re.search(r'(\d+)%', activity_div['aria-label']).group(1) if activity_div else None

        attributes = new_soup.find_all('td', class_="ddc-text-center")
        prescription = attributes[1].get_text(strip=True)
        preg = attributes[2].get_text(strip=True)
        csa = attributes[3].get_text(strip=True)
        alcohol = attributes[4].get_text(strip=True)

        brand_name, dosage, allergy = get_detailed_drug_info(dlink)

        results.append([drug_name, brand_name, dosage, rate, rev, act, prescription, preg, csa, alcohol, allergy, disease])

    return results

# Function to process each batch of links
def process_batch(links, diseases):
    batch_results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(scrape_drug_info, link, disease) for link, disease in zip(links, diseases)]
        for future in concurrent.futures.as_completed(futures):
            batch_results.extend(future.result())

    return batch_results

# Main function to get all treatment options and scrape data in batches
def get_each_treatment_options(url):
    disease, links = get_treatment_options(url)
    
    all_results = []
    batch_size = 50  # Number of links to process in each batch
    for i in range(0, len(links), batch_size):
        batch_links = links[i:i + batch_size]
        batch_diseases = disease[i:i + batch_size]
        all_results.extend(process_batch(batch_links, batch_diseases))

    return all_results

# Scrape the data and save it to a CSV
url = "https://www.drugs.com/medical_conditions.html"
all_results = get_each_treatment_options(url)

csv_file_path = 'drug_treatments.csv'

def convert_list_to_string(list_of_lists):
    # Flatten the list of lists, skip None values
    return '; '.join([item for sublist in list_of_lists if sublist is not None for item in sublist if item is not None])



with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow([
        'drug_name', 'brand_name', 'dosage', 'rating', 'review', 'activity',
        'prescription', 'preg', 'csa', 'alcohol', 'allergy', 'disease_list'
    ])

    for result in all_results:
        writer.writerow([
            result[0],
            result[1],  
            result[2],
            result[3],
            result[4],
            result[5],
            result[6],
            result[7],
            result[8],
            result[9],
            result[10],  
            result[11]
        ])

print(f"CSV file '{csv_file_path}' created successfully.")
