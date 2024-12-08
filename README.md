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

The pdf's are present inside the pdf folder and the source files are present inside the exp folder directly.
A short explanation video is inside the root folder.

### Instructions to Build and Run the App from Source Code

This project consists of two components:  
1. **Flask API** (`app.py`) for generating drug recommendations.
2. **Streamlit UI** (`backend.py`) for user input, symptom selection, and database interaction.

---

#### Prerequisites
1. **Python Environment**:
   - Ensure Python 3.8 or higher is installed.
   - Create and activate a virtual environment:
     ```bash
     python -m venv env
     source env/bin/activate  # On Windows: env\Scripts\activate
     ```

2. **Install Dependencies**:
   - Install the required libraries and dependencies include:
     - `flask`
     - `streamlit`
     - `pandas`
     - `numpy`
     - `scikit-learn`
     - `tensorflow`
     - `psycopg2`
     - `pyspark`
     - `imblearn`

3. **Database Setup**:
   - Set up a PostgreSQL database with these details:
     - Host: `192.168.1.27`
     - Database: `DIC`
     - Username: `postgres`
     - Password: `1234`
   - Create necessary tables:
     - `drug_treatments`
     - `symptoms`
   - Populate the tables with appropriate data.

4. **Pre-trained Model and Files**:
   - Place the following files in the root directory:
     - `my_model.h5` - TensorFlow model for predictions.
     - `tokenizer.pkl`, `label_encoder.pkl`, `scaler.pkl` - Supporting files for preprocessing.

---

#### Running the Flask API (`app.py`)
1. **Start the API**:
   - Navigate to the directory containing `app.py` and run:
     ```bash
     python app.py
     ```
   - The API will be hosted at `http://127.0.0.1:5000`.

2. **API Functionality**:
   - The API processes user input and generates drug recommendations.
   - Verify functionality by sending a POST request to the `/recommend` endpoint using tools like Postman or `curl`.

---

#### Running the Streamlit UI (`app1.py`)
1. **Start the Streamlit App**:
   - Run the app using:
     ```bash
     streamlit run backend.py
     ```
   - The app will open in your default browser at `http://localhost:8501`.

2. **UI Features**:
   - Input personal details (e.g., username, age, gender).
   - Select symptoms and medical history.
   - Insert and delete records from the database.
   - Fetch and display drug recommendations using the Flask API.

---
