import os
import pandas as pd

# Calculate root directory dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_symptoms():
    file_path = os.path.join(
        BASE_DIR,
        "database",
        "AshaCare_AI_symptom_dataset_PDF_transcription.csv",
    )
    # Fill NaN values with empty string to prevent JSON 500 error
    df = pd.read_csv(file_path).fillna("")
    return df.head(20).to_dict(orient="records")


def get_questions():
    file_path = os.path.join(
        BASE_DIR, "database", "AshaCare_AI_questionnaire_symptom_map.csv"
    )
    df = pd.read_csv(file_path).fillna("")
    return df.head(20).to_dict(orient="records")