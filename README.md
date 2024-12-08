# personalised-general-drug-prescriptions
Applying Data-Driven Insights and ML to Personalize General Drug Prescriptions &amp; Enhance Healthcare.
</br> </br> Team Members : </br> 
Shreyas Bellary Manjunath (50604230) </br> 
Shishir Hebbar (50594522) </br> 
Jahnavi Gubbala(50604125) </br> 
Ruthvik Vasantha Kumar (50592560) </br> 

Questions listed: </br> 
Shreyas Bellary Manjunath: - </br> 
1)Is there a relationship between drug dosage, CSA classification, alcohol interaction, and user ratings and reviews? </br> 
2)Is there a significant difference in the total number of reviews between drugs marketed under multiple brand names compared to those marketed under a single brand name? </br>
Shishir Hebbar: - </br> 
1)Is there a significant correlation between the dosage of drugs given for pain and their effectiveness in treating the pain? </br> 
2)How does the frequency of a drug's prescription relate to its perceived effectiveness (rating)? </br> 
Jahnavi Gubbala: - </br> 
1)How do specific symptoms (e.g., fever, cough, difficulty breathing) combined with health indicators (e.g., blood pressure, cholesterol level) affect the likelihood of patients being diagnosed with severe respiratory conditions such as asthma or influenza? </br> 
2)Are older age groups more likely to have higher cholesterol levels compared to younger age groups? </br> 
Ruthvik Vasantha Kumar: - </br> 
1)What is the impact of pregnancy safety categories on the prescription patterns of drugs for women of childbearing age? </br> 
2)What is the correlation between drug activity levels (percentage of patients who experience effectiveness) and prescription status (Rx vs. OTC)? </br> 

Location of Code and Analysis: </br> 
Shreyas Bellary Manjunath: - /shreyas_phase2.ipynb </br> 
Shishir Hebbar: - /shishir_phase2.ipynb </br> 
Jahnavi Gubbala: - /jahnavi_phase2.ipynb </br> 
Ruthvik Vasantha Kumar: - /ruthvik_phase2.ipynb </br> 

The pdf's are present inside the pdf folder and the source files are present inside the main folder directly.

Location of Code and Analysis (PDF format): </br> 
Shreyas Bellary Manjunath: - /pdf/shreyas_phase2.pdf </br> 
Shishir Hebbar: - /pdf/shishir_phase2.pdf </br> 
Jahnavi Gubbala: - /pdf/jahnavi_phase2.pdf </br> 
Ruthvik Vasantha Kumar: - /pdf/ruthvik_phase2.pdf </br> 

### Instructions to Build and Run the App from Source Code

#### Prerequisites
1. **Python Environment**: Ensure you have Python 3.8 or higher installed.
2. **Libraries**: Install required Python packages, you will need libraries such as:
   - `streamlit`
   - `pandas`
   - `numpy`
   - `plotly`
   - `scikit-learn`
   - `tensorflow`
   - `psycopg2`
   - `imblearn`
   - `requests`

3. **Database Setup**:
   - **PostgreSQL**: Set up a PostgreSQL database with the following details:
     - Host: `192.168.1.27`
     - Database: `DIC`
     - Username: `postgres`
     - Password: `1234`
   - Ensure the `drug_treatments` and `symptoms` tables are created and populated as per the app's requirements.

4. **Pre-trained Model Files**:
   - Place the following files in the same directory as the app:
     - `my_model.h5`: TensorFlow model file.
     - `tokenizer.pkl`: Preprocessing tokenizer.
     - `label_encoder.pkl`: Encoder for class labels.
     - `scaler.pkl`: Scaler for numerical inputs.

5. **Server Endpoint**:
   - The app communicates with a recommendation API hosted at `http://192.168.1.164:8000/recommend`. This server will be running and accessible if the database host is active.

---

#### Steps to Run the App
1. **Clone or Download the Source Code**:
   - Place `app1.py` and `i_requests.py` in a working directory.

2. **Run the Streamlit Application**:
   - Start the app using Streamlit:
     ```bash
     streamlit run app1.py
     ```

3. **Verify Connectivity**:
   - Ensure the app can connect to the PostgreSQL database and the recommendation API.
   - Check for any errors in the Streamlit logs during initialization.

4. **Using the App**:
   - Open the URL displayed in your terminal, typically `http://localhost:8501`.
   - Enter the required inputs on the interface:
     - Personal details (username, age, gender).
     - Symptoms and medical history.
   - Use buttons for inserting/deleting rows or fetching recommendations.

5. **Testing the API**:
   - Run `i_requests.py` to validate the API functionality:
     ```bash
     python i_requests.py
     ```
   - Modify `user_input` in `i_requests.py` as needed to test with different scenarios.

---
