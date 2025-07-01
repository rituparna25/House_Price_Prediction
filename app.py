import streamlit as st
import pickle
import json
import numpy as np

# Load model and column metadata
model = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))

with open("banglore_home_prices_columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']

location_names = data_columns[3:]

# Page config
st.set_page_config(page_title="The Bangalore Home Price Wizard", layout="centered")

# Custom CSS for background and styling
st.markdown("""
    <style>
        .stApp {
            background-image: url('https://wallpapercave.com/wp/wp13763230.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
        }
        
        /* Main container styling */
        .block-container {
            background-color: rgba(0, 0, 0, 0.85) !important;
            padding: 40px !important;
            border-radius: 20px !important;
            margin: 20px auto !important;
            max-width: 600px !important;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
            backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        
        .title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            font-family: 'Arial', sans-serif;
        }
        
        .stNumberInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
            border-radius: 8px !important;
        }
        
        .stSelectbox > div > div > div {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
            border-radius: 8px !important;
        }
        
        .stButton > button {
            background: linear-gradient(45deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 25px !important;
            padding: 12px 30px !important;
            font-size: 16px !important;
            font-weight: bold !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3) !important;
        }
        
        /* Style input labels */
        .stNumberInput > label, .stSelectbox > label {
            color: white !important;
            font-weight: 900 !important;
            font-size: 25px !important;
        }
        
        /* Style success and warning messages */
        .stAlert {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
        }
    </style>
""", unsafe_allow_html=True)

# Stylish title
st.markdown('<div class="title">The Bangalore Home Price Wizard</div>', unsafe_allow_html=True)

# Input fields
sqft = st.number_input("📏 Total Square Feet", min_value=100.0, max_value=10000.0, value=1000.0)
bath = st.number_input("🚿 Number of Bathrooms", min_value=1, max_value=10, value=2)
bhk = st.number_input("🛏 Number of BHK", min_value=1, max_value=10, value=2)
location = st.selectbox("📍 Select Location", sorted(location_names))

# Predict button
if st.button("🔮 Predict Price"):
    x = np.zeros(len(data_columns))
    
    try:
        x[data_columns.index('total_sqft')] = sqft
        x[data_columns.index('bath')] = bath
        x[data_columns.index('bhk')] = bhk
    except ValueError as e:
        st.error(f"Input field mismatch: {e}")
        st.stop()
    
    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1
    else:
        st.warning(f"Location '{location}' not found in model columns.")
    
    predicted_price = model.predict([x])[0]
    st.success(f"💰 Estimated Price: ₹{round(predicted_price, 2)} Lakhs")