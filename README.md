# The Bangalore Home Price Wizard

This project is a **machine learning-powered web application** built using **Streamlit** to predict the price of a house in Bangalore based on:
- 📏 Square footage
- 🛏 Number of BHKs
- 🚿 Number of bathrooms
- 📍 Location within Bangalore

---

## 🚀 Demo

![App Screenshot](https://github.com/rituparna25/The-Bangalore-Home-Price-Wizard/blob/main/Screenshot%202025-07-01%20172532.png?raw=true)

Live demo (host yourself or deploy on Streamlit Cloud)

---

## 🔍 How It Works

1. User inputs:
   - Total square feet
   - Number of bathrooms
   - Number of BHKs
   - Location from dropdown

2. App constructs a one-hot encoded feature vector using the trained data columns

3. The feature vector is passed to a **Linear Regression model** trained on real Bangalore housing data

4. Price is predicted and shown in 💰 Lakhs

---

## ✅ Model Info

- 📊 **Algorithm:** Linear Regression
- 📈 **Accuracy (R² score on test set):** ~79-82%
- 🧹 Outliers removed using Z-score filtering
- 🏠 Location column one-hot encoded for ~240+ localities

---

## 📦 Installation & Setup

### 🔧 Requirements

Create a file called `requirements.txt`:

```txt
streamlit
numpy
scikit-learn
pandas
```

### ▶️ Run Locally

```bash
git clone https://github.com/<your-username>/bangalore-home-price-predictor.git
cd bangalore-home-price-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📊 Data Source

- 📂 Dataset: [Bengaluru House Price Data (Kaggle)](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)

---
