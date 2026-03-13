import pickle
import os

try:
    with open('max_len.pkl', 'rb') as f:
        max_len = pickle.load(f)
    print(f"Type of max_len: {type(max_len)}")
    print(f"Value of max_len: {max_len}")
except Exception as e:
    print(f"Error loading max_len.pkl: {e}")

try:
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    print(f"Type of tokenizer: {type(tokenizer)}")
    # print(tokenizer.word_index) # might be too large
except Exception as e:
    print(f"Error loading tokenizer.pkl: {e}")
