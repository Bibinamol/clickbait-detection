# Clickbait Detection with Machine Learning

This project detects whether a given headline is clickbait or not, using Natural Language Processing and a stacked machine learning model. It includes a user-friendly Streamlit web app for real-time predictions.

## Dataset
The dataset used is publicly available on Kaggle:  
[Clickbait Dataset – by Aman Anand Rai](https://www.kaggle.com/datasets/amananandrai/clickbait-dataset )  
It contains thousands of headlines labeled as either clickbait or non-clickbait.
#  Model & Approach

**Preprocessing**:Headlines are tokenized using a pre-trained tokenizer (`tokenizer.joblib`)
**Model:** A stacked ensemble model trained on the processed features (`best_stack_model.joblib`)
**Persistence:** Both model and tokenizer are saved using `joblib` for fast loading
****UI**: A simple Streamlit app (`clickbaitui.py`) is provided for interactive use

## Installation & Setup

### 1. Clone this repository
git clone https://github.com/Bibinamol/clickbait-detection.git
cd clickbait-detection
Install dependencies Manually:
pip install streamlit scikit-learn pandas numpy joblib

Run the Streamlit App

streamlit run clickbait_ui.py


**Author**
Bibina Jacob
Email: bibinamolj@gmail.com 
