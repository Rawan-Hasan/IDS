import joblib
import pandas as pd

def load_model_and_features(model_name):
    model = joblib.load(f"models/{model_name}_model.joblib")
    selected_features = ['dur', 'proto', 'service', 'state', 'sbytes', 'dbytes']
    return model, selected_features

def preprocess_input(input_data, selected_features):
    df = pd.DataFrame([input_data])
    return df[selected_features]
