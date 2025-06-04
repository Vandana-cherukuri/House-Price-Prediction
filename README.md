# 🏠 House Price Prediction App

This project is a **web-based house price prediction tool** built using **Streamlit** and a **Linear Regression** model. The app takes in key features of a house — such as living area, bedrooms, and bathrooms — and predicts an estimated sale price.

## 🔍 Features

- ✨ User-friendly web interface
- 🎥 Beautiful Lottie animations
- 📊 Real-time price predictions using a trained model
- ✅ Clean UI with CSS styling
- 🎈 Balloons and animations on prediction

## 🧠 Model Details

- **Model Type:** Linear Regression
- **Trained With:** Scikit-learn
- **Features Used:**
  - `GrLivArea` (Above ground living area in sq. ft.)
  - `BedroomAbvGr` (Number of bedrooms)
  - `FullBath` (Number of full bathrooms)

Model was trained using housing data and saved as a `.pkl` file.

## 🚀 Demo

To see a live demo, run the following command in your terminal:

```bash
streamlit run app.py

🌐 Deploying
You can deploy this app for free using Streamlit Cloud.
Just connect your GitHub repo and deploy app.py.

📜 License
This project is licensed under the MIT License.

🙋‍♀️ Author
Vandana Cherukuri
GitHub: @Vandana-cherukuriS

🧠 Quote
"Predicting tomorrow’s price with today’s features."
