import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

st.set_page_config(page_title="Next Word Prediction", layout="centered")

st.title("Next Word Prediction")
st.markdown("Enter a sequence of words and the model will predict the next likely word.")

@st.cache_resource
def load_resources():
    try:
        # Load the model
        model = load_model('lstm_model.h5')
        
        with open('tokenizer.pkl', 'rb') as f:
            tokenizer = pickle.load(f)
            
        with open('max_len.pkl', 'rb') as f:
            max_len = pickle.load(f)
            
        return model, tokenizer, max_len, None
    except Exception as e:
        return None, None, None, e

model, tokenizer, max_len, error = load_resources()

if error:
    st.error(f"Error loading files: {error}")
    st.stop()

input_text = st.text_input("Enter your text here:", placeholder="Type something...")

if st.button("Predict Next Word"):
    if input_text.strip():
        try:
            token_list = tokenizer.texts_to_sequences([input_text])[0]
            token_list = pad_sequences([token_list], maxlen=max_len, padding='pre')
            
            if not hasattr(tokenizer, 'index_word'):
                tokenizer.index_word = {v: k for k, v in tokenizer.word_index.items()}

            predicted = model.predict(token_list, verbose=0)
            predicted_index = np.argmax(predicted, axis=-1)[0]

            output_word = tokenizer.index_word.get(predicted_index, "")
            
            if output_word:
                st.success(f"Predicted Next Word: **{output_word}**")
            else:
                st.warning("Model predicted an unknown word index.")
                
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.warning("Please enter some text to predict.")
