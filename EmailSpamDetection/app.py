import streamlit as st
import pickle
import numpy as np

# Load the trained model and vectorizer
with open('model/spam_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Streamlit page configuration
st.set_page_config(page_title="📧 Email Spam Detection", layout="centered")

# 🌟 Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1603791440384-56cd371ee9a7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: black !important;
    }

    .main {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 10px;
        margin-top: 50px;
        color: #000000 !important; /* Black text */
    }

    h1, h2, h3, p, label, .stTextArea label {
        color: #000000 !important; /* Ensure all text and labels are black */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    textarea, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    textarea::placeholder {
        color: #333333 !important;
        font-style: italic;
        opacity: 1;
    }

    .stButton>button {
        background-color: #ffffff;
        color: #ffffff;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        margin-top: 10px;
    }

    .stButton>button:hover {
        background-color: #444444;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main app UI
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.title("📧 Email Spam Detection")
    st.write("Check if your email message is spam or not using Machine Learning.")

    # Email input
    email_text = st.text_area("✉️ Paste your email text here", height=200, placeholder="Type or paste your email content...")

    # Predict button
    if st.button("🔍 Check Spam"):
        if email_text.strip() == "":
            st.warning("⚠️ Please enter some text to analyze.")
        else:
            input_vector = vectorizer.transform([email_text])
            prediction = model.predict(input_vector)

            if prediction[0] == 1:
                st.error("🚨 This email is classified as **SPAM**.")
            else:
                st.success("✅ This email is classified as **NOT SPAM**.")

    st.markdown('</div>', unsafe_allow_html=True)
