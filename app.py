# ✅ Set page config first
import streamlit as st
st.set_page_config(page_title="House Price Predictor", layout="centered", page_icon="🏠")

# 📦 Imports
import pandas as pd
import joblib
import json
from streamlit_lottie import st_lottie

# 🎨 CSS Styling
st.markdown("""
    <style>
    h1, h3 {
        color: #003566;
        text-align: center;
    }
    .stButton > button {
        background-color: #0077b6;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stNumberInput input, .stSlider {
        border-radius: 5px;
        padding: 5px;
    }
    .stForm {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 🔁 Load Lottie Animations
@st.cache_data
def load_lottiefile(path: str):
    with open(path, "r") as f:
        return json.load(f)

# 💾 Load Model
@st.cache_resource
def load_model():
    return joblib.load("house_price_model.pkl")

# ✅ Load model and animations
model = load_model()
lottie_top = load_lottiefile("animation_main.json")
lottie_result = load_lottiefile("animation_success.json")

# 🏠 App Header
st_lottie(lottie_top, height=250, key="top_anim")
st.title("🏠 House Price Prediction App")
# ✨ Centered intro text
st.markdown("""
    <div style='text-align: center; font-size: 18px;'>
        Estimate your house value based on living area, bedrooms, and bathrooms.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; font-style: italic; color: #4a4a4a;'>
        🧠 Predicting tomorrow’s price with today’s features.
    </div>
""", unsafe_allow_html=True)

# 📋 Input Form
with st.form("input_form"):
    st.markdown("### Enter House Features:")
    col1, col2 = st.columns(2)
    with col1:
        grlivarea = st.number_input("Ground Living Area (sq ft)", 100, 10000, value=1500)
    with col2:
        bedroom = st.number_input("Number of Bedrooms", 0, 10, value=3)

    fullbath = st.slider("Number of Full Bathrooms", 0, 5, value=2)
    submitted = st.form_submit_button("Predict Price 💰")

# 🔮 Prediction Result
if submitted:
    input_data = pd.DataFrame([[grlivarea, bedroom, fullbath]], columns=["GrLivArea", "BedroomAbvGr", "FullBath"])
    prediction = model.predict(input_data)[0]

    st.success(f"🏡 Estimated House Price: **${prediction:,.2f}**")
    st_lottie(lottie_result, height=200, key="result_anim")
    st.balloons()
