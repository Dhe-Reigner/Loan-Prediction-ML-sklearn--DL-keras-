# Loan-Prediction-ML-sklearn--DL-keras-
A complete end-to-end loan prediction system built using Scikit-learn and Keras (TensorFlow). The project includes exploratory data analysis (EDA), feature engineering, classical ML models, and a deep neural network (DNN) for classifying whether a loan applicant is likely to be approved.

# 🏦 Loan Prediction System — ML + Deep Learning

A complete machine learning and deep learning project for predicting whether a loan application will be approved.  
Built with **Python, Scikit-learn, Pandas, Matplotlib, and Keras (TensorFlow)**.

Loan prediction is a common real-world problem in banking and fintech where institutions want to automate and improve the decision-making process using data-driven models.

---

## 🚀 Project Overview

This project develops a classification model that predicts loan approval based on customer details such as:

- Gender  
- Married Status  
- Education  
- Applicant Income  
- Co-applicant Income  
- Loan Amount  
- Credit History  
- Property Area  
- Employment Information  
- Loan Term  

Two pipelines were created:

### **1. Machine Learning Models (Scikit-learn)**
- Logistic Regression  
- Random Forest  
- Support Vector Machine  
- Gradient Boosting  
- XGBoost (optional)

### **2. Deep Learning Model (Keras/TensorFlow)**
- Multi-Layer Perceptron (MLP) / Dense Neural Network  
- Batch Normalization  
- Dropout Regularization  
- ReLU activation and Softmax output  

Both pipelines include:

✔ Data cleaning  
✔ Handling missing values  
✔ Encoding categorical variables  
✔ Feature scaling  
✔ Train/test split  
✔ Model evaluation (Accuracy, F1-Score, Confusion Matrix, ROC-AUC)

---

## 📊 Dataset

You may use:

- The Kaggle **Loan Prediction Dataset**, or  
- Your own curated dataset  

Include fields like demographics, financial status, loan history, and eligibility criteria.

---

## 🧠 Deep Learning Architecture (Keras)

Example architecture:

```python
model = Sequential([
    Dense(64, activation='relu', input_shape=(input_dim,)),
    BatchNormalization(),
    Dropout(0.3),

    Dense(32, activation='relu'),
    Dropout(0.2),

    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])


Optimizer: Adam
Loss: Binary Crossentropy
Metrics: Accuracy, AUC

📈 Model Performance

You can add your final results here, for example:

Random Forest: 82% accuracy

XGBoost: 85% accuracy

Deep Learning Model: 88% accuracy
