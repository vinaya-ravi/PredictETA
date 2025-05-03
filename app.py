import joblib
import pandas as pd
import numpy as np

def load_model():
    """Load the trained model"""
    pipeline = joblib.load('toolkit/pipeline.joblib')
    return pipeline

def predict_eta(data):
    """
    Predict the estimated time of arrival
    
    Args:
        data: DataFrame with the required features
    
    Returns:
        Predictions in minutes
    """
    model = load_model()
    predictions = model.predict(data)
    return predictions

if __name__ == "__main__":
    print("ETA Prediction Model by Bhargavi Ravilla")
    print("Load the model and make predictions using predict_eta() function") 