# Heart Disease Prediction Web Application

A machine learning-powered web application that predicts the likelihood of heart disease based on medical parameters using a Random Forest classifier.

## Project Overview

This Flask-based web application allows users to input various health metrics and receive a prediction about their heart disease risk. The system uses a trained Random Forest model that analyzes 11 key medical features to provide binary classification results.

## Features

- **Interactive Web Interface**: User-friendly form for inputting medical parameters
- **Real-time Predictions**: Instant heart disease risk assessment
- **Robust Data Processing**: Handles both numerical and categorical input data
- **Error Handling**: Comprehensive validation and error reporting

## Medical Parameters Used

The model evaluates the following health indicators:

- **Age**: Patient's age
- **Sex**: Gender classification
- **ChestPainType**: Type of chest pain experienced
- **RestingBP**: Resting blood pressure
- **Cholesterol**: Serum cholesterol level
- **FastingBS**: Fasting blood sugar
- **RestingECG**: Resting electrocardiogram results
- **MaxHR**: Maximum heart rate achieved
- **ExerciseAngina**: Exercise induced angina
- **Oldpeak**: ST depression induced by exercise
- **ST_Slope**: Slope of peak exercise ST segment

## Model Architecture

- **Algorithm**: Random Forest Classifier (100 estimators)
- **Preprocessing**: StandardScaler for numerical features, OneHotEncoder for categorical features
- **Data Split**: 70% training, 30% testing with stratified sampling
- **Output**: Binary classification (Heart Disease / Heart Normal)

## Project Structure

```
├── app.py              # Flask web application
├── model_training.py   # Machine learning pipeline
├── model.pkl          # Trained model (generated)
├── heart.csv          # Training dataset
├── templates/
│   ├── index.html     # Main prediction interface
│   └── about.html     # About page
```

## Technology Stack

- **Backend**: Flask (Python web framework)
- **ML Libraries**: scikit-learn, pandas, matplotlib, seaborn
- **Frontend**: HTML templates (Jinja2)

## Model Performance

The Random Forest classifier processes both numerical and categorical features through a preprocessing pipeline that ensures optimal model performance and handles unknown categorical values gracefully.
