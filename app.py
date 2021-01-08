## Importing Packages
import pickle
import streamlit as st
from utils import *

@st.cache
def get_predictions(input_tokens, starts, k = 1.0):
    n_gram_counts_list = pickle.load(open('data/en_counts.txt', 'rb'))
    vocabulary = pickle.load(open('data/vocab.txt', 'rb'))
    suggestion = get_suggestions(input_tokens, n_gram_counts_list, vocabulary, k=k, start_with = starts)
    return suggestion

## Page Title
st.set_page_config(page_title = "Autocompletion using n-gram",
    page_icon = "💬")
st.title("Auto-Completion using N-Gram models")
st.markdown("---")

## Sidebar
st.sidebar.header("An Auto Completion program using N-Gram Models")
st.sidebar.markdown("---")
st.sidebar.markdown("Here's the [link](https://www.kaggle.com/sauravmaheshkar/auto-completion-using-n-gram-models) to the kaggle kernel, which was used for training and extracting the counts list and the vocabulary.")

## Input Fields
sentence = st.text_input("Enter a sentence")
st.subheader("Optional Inputs")
starts = st.text_input("The starting letter of the expected next word")
k = st.number_input("Enter smoothing factor k")

tokenized = sentence.split()

if st.button("Predict"):
    suggestion = get_predictions(tokenized, starts, k)
    st.write(suggestion[0])


st.markdown("---")
st.markdown("If you liked this project and would like to read the code and see some of my other work, don't forget to ⭐the [repository](https://github.com/SauravMaheshkar/Auto-Completion-using-N-Gram-Models) and follow [me](https://github.com/SauravMaheshkar).")
