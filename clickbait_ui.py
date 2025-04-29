import streamlit as st
import joblib

# Configuring stmlit app page
st.set_page_config(
    page_title="Clickbait Detection",
    page_icon="",
    layout="centered",
)

# Loading vectorizer
@st.cache_resource
def load_best_model():
    return joblib.load("best_stack_model.joblib")

@st.cache_resource
def load__downloaded_vectorizer():
    return joblib.load("tfidf_vectorizer.joblib")

bestStackingModel = load_best_model()
vectorizer = load__downloaded_vectorizer()

# Add background image + style
def add_background_image(image_url):
    st.markdown()

background_image_url = "https://img.freepik.com/premium-vector/clickbait-icon-vector-image-can-be-used-digital-marketing_120816-131031.jpg"
add_background_image(background_image_url)


# Input
st.markdown('<p style="font-size: 1.4rem; font-weight: bold; color: white;">🔍 Type or paste a headline:</p>', unsafe_allow_html=True)
headline_input = st.text_input("")

# Prediction
if headline_input:
   
Contact bibinamolj@gmail.com for full code