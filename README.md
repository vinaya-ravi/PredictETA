# Estimated Time of Arrival (ETA) Prediction

## Project Overview
This project implements a machine learning model to predict the estimated time of arrival (ETA) for journeys in a ride-hailing application. The implementation compares baseline models with advanced ML models to demonstrate improved prediction accuracy.

## Dataset
The dataset contains ride information including:
- Pickup and dropoff coordinates
- Distance and duration
- Timestamp information
- Weather conditions
- Traffic patterns

## Models Implemented
- **Baseline Models**:
  - Mean prediction
  - Median prediction
- **Advanced Models**:
  - Linear Regression
  - Decision Tree
  - Random Forest
  - XGBoost (best performing)

## Project Structure
- `dataset/`: Contains the dataset files
- `dev/`: Jupyter notebook with full end-to-end ML pipeline
- `toolkit/`: Pipeline with trained ML model
- `requirements.txt`: Required libraries and dependencies

## How to Run the Project

### Prerequisites
- Python 3.7+
- Git

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Bhargavi701/Working_Code.git
cd Working_Code
```

2. Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Open and run the Jupyter notebook:
```bash
jupyter notebook dev/ETA_Prediction.ipynb
```

### Key Notebook Sections
The notebook contains the following key sections that satisfy the project requirements:

1. **Data Loading and Preprocessing**
   - Loading the dataset
   - Feature engineering
   - Data cleaning and transformation
   - Train/test split

2. **Baseline Model Implementation**
   - Mean-based prediction
   - Median-based prediction
   - Evaluation metrics for baselines

3. **Advanced Model Implementation**
   - Model selection and hyperparameter tuning
   - Training multiple models
   - Cross-validation

4. **Model Evaluation**
   - RMSE comparison across all models
   - Residual analysis
   - Feature importance visualization

5. **Results Visualization**
   - Model performance comparison
   - Actual vs. Predicted plots
   - Feature importance charts

## Results
The models achieved the following RMSE scores on the test set:

| Model | RMSE |
|-------|------|
| Mean Baseline | 567.64 |
| Median Baseline | 570.59 |
| Linear Regression | 217.90 |
| Decision Tree | 254.35 |
| Random Forest | 236.54 |
| XGBoost | 154.01 |

XGBoost performed best with a 72.9% improvement over the baseline models.

## Key Visualizations

### Model Comparison
The notebook includes visualizations comparing all model performances:
- Bar charts of RMSE values
- Training and validation curves
- Error distribution analysis

### Prediction Analysis
- Scatter plots of actual vs. predicted values
- Residual plots
- Error distribution by feature values

### Feature Importance
- Bar charts showing the most influential features
- SHAP value analysis for XGBoost model

## Author
Bhargavi Ravilla

© 2024 Bhargavi Ravilla. All rights reserved. Last updated: March 2024.
