# Student Mental Health Assistant 🧠🤗

A data-driven mobile application that provides mental health screening, journaling with sentiment analysis, and personalized coping strategies for students. Built with a focus on privacy, ethical data handling, and iterative machine learning.

## 🚀 Features

- **DSM-based Screening:** PHQ-9 (Depression), GAD-7 (Anxiety), and PSS (Stress) questionnaires.
- **ML-Powered Analysis:** Instant severity classification and risk assessment.
- **Personalized Recommendations:** Context-aware coping strategies.
- **Secure Journaling:** Text journaling with automatic sentiment tracking.
- **Researcher Dashboard:** For analyzing anonymized, aggregated trends.
- **Iterative Learning:** Models retrain periodically on new anonymized data.

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL
- **Machine Learning:** Scikit-learn, Pandas, NLTK/TextBlob
- **Frontend:** React Native (To be developed)
- **Data Visualization:** Matplotlib, Seaborn, Streamlit

## 📁 Project Structure
student-mental-health-app/
│
├── README.md                     # Overview, setup guide, screenshots
├── requirements.txt              # Python dependencies
├── environment.yml               # Conda environment (optional)
├── .gitignore
├── .env.example                  # Example env vars (safe to share)
│
├── data/                         # Data (mock/anonymized only)
│   ├── raw/                      # Example survey responses, journaling text
│   ├── processed/                # Cleaned data for modeling
│   └── external/                 # Public datasets (if used)
│
├── notebooks/                    # Jupyter notebooks for exploration & ML
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_recommendation_system.ipynb
│   └── 05_nlp_sentiment.ipynb
│
├── src/                          # Core ML + data science logic
│   ├── data_preprocessing.py     # Cleaning, encoding, feature engineering
│   ├── train_model.py            # ML training pipeline
│   ├── retrain_pipeline.py       # Iterative retraining from DB
│   ├── recommend.py              # Recommendation engine logic
│   ├── sentiment_analysis.py     # NLP for journaling
│   └── utils.py                  # Helper functions
│
├── models/                       # Saved ML models
│   ├── depression_model.pkl
│   ├── anxiety_model.pkl
│   └── sentiment_model.pkl
│
├── app/                          # App (frontend + backend)
│   ├── backend/
│   │   ├── main.py               # FastAPI/Flask entrypoint
│   │   ├── routes/               # API endpoints
│   │   │   ├── questionnaire.py
│   │   │   ├── prediction.py
│   │   │   ├── recommendations.py
│   │   │   └── chat.py
│   │   ├── db/                   # Database layer
│   │   │   ├── connection.py     # Secure DB connection via env vars
│   │   │   ├── models.py         # SQLAlchemy models (users, responses, journals)
│   │   │   └── queries.py        # Insert/query student responses
│   │   └── ml/                   # Model inference wrappers
│   │       ├── predictor.py
│   │       └── retrainer.py
│   │
│   └── frontend/                 # React Native app
│       ├── screens/
│       │   ├── HomeScreen.js
│       │   ├── QuestionnaireScreen.js
│       │   ├── ResultsScreen.js
│       │   ├── JournalScreen.js
│       │   └── ChatScreen.js
│       ├── components/           # Reusable UI parts
│       └── App.js                # Entry point
│
├── dashboards/                   # Researcher/admin dashboards
│   └── mental_health_dashboard.ipynb
│
├── tests/                        # Unit tests
│   ├── test_data_preprocessing.py
│   ├── test_model.py
│   ├── test_recommend.py
│   ├── test_sentiment.py
│   └── test_db.py
│
└── docs/                         # Documentation
    ├── architecture.md           # System architecture diagram
    ├── db_schema.md              # Database schema & explanation
    ├── data_dictionary.md        # Feature/label dictionary
    ├── ethics_privacy.md         # Notes on data privacy/anonymization
    └── design_mockups/           # Figma exports/screenshots


⚠️ Data Privacy Notice
This project uses mock/anonymized datasets only. In a real-world setting, sensitive student data would be stored securely in a database with encryption and access controls.
The repository never contains private data or credentials. Instead, we provide example .env files and mock datasets so contributors can run the project safely.


## 🔧 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/student-mental-health-app.git
    cd student-mental-health-app
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your database:**
    - Install PostgreSQL and create a new database named `mhealth_db`.
    - Copy `.env.example` to a new file called `.env`.
    - Edit `.env` with your actual database credentials.

5.  **Run the backend API:**
    ```bash
    cd app/backend
    uvicorn main:app --reload
    ```
    The API will be running at `http://localhost:8000`. Check `http://localhost:8000/docs` for the interactive API documentation.

## 🤝 Contributing
[...]

## 📝 License
This project is licensed under the MIT License.