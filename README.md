# Next Word Prediction System

An **LSTM-powered Next Word Prediction** application that intelligently predicts the next word in a sequence based on user input. The system combines **deep learning (LSTM)** with **Streamlit** for a user-friendly interface, delivering fast and accurate word predictions trained on curated quote datasets.

This project is built with production-oriented mindset, focusing on ease of deployment, robust error handling, and seamless user experience.

---

## 🚀 Key Features

* **Deep Learning Model**
  Leverages **LSTM (Long Short-Term Memory)** neural networks to understand contextual patterns and dependencies in word sequences, enabling accurate next-word predictions.

* **Fast Inference**
  Pre-trained model with optimized inference using TensorFlow/Keras, delivering predictions in milliseconds.

* **Interactive Web Interface**
  Built with **Streamlit**, providing an intuitive, responsive UI for real-time predictions without code.

* **Robust Data Pipeline**
  * Tokenization of text using TensorFlow's Tokenizer
  * Sequence padding for consistent input shapes
  * Support for quotes and narrative text datasets
  * Vocabulary size of 10,000 most frequent words

* **Production-Ready Deployment**
  * Containerized with `requirements.txt` for dependency management
  * Supports deployment on **Streamlit Cloud**, **Docker**, or local servers
  * Streamlined error handling with fallback mechanisms

* **Efficient Model Storage**
  * Pre-trained LSTM model saved as `lstm_model.h5` (Keras format)
  * Tokenizer and max_length stored as pickled Python objects for quick loading

---

## 🧠 System Architecture

1. **Data Ingestion Layer**
   Processes quote dataset (CSV format), cleaning and normalizing text for training preparation.

2. **Tokenization & Preprocessing**
   Converts text into numerical sequences using TensorFlow Tokenizer, applying padding to ensure consistent input dimensions.

3. **Embedding & LSTM Layer**
   * Embedding layer (50 dimensions) converts token IDs to dense vectors
   * LSTM layer (128 units) captures long-range dependencies and contextual patterns
   * Dense output layer (softmax activation) predicts next word probabilities

4. **Inference Engine**
   Loads pre-trained model, tokenizer, and config; processes user input and generates predictions in real-time.

5. **Streamlit UI**
   Provides interactive interface for end-users to input text and receive predictions instantly.

---

## 📁 Project Structure

```
next-word-prediction/
├── data/                     # Data storage
│   └── qoute_dataset.csv     # Source quote dataset
├── models/                   # Model artifacts
│   ├── lstm_model.h5         # Pre-trained LSTM model
│   ├── tokenizer.pkl         # Tokenizer object
│   └── max_len.pkl           # Maximum sequence length
├── app.py                    # Streamlit application
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules
├── README.md                 # Project documentation
└── .env                      # Environment variables (if needed)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/adityat22/Next-Word-Prediction-System.git
cd Next-Word-Prediction-System
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**Mac / Linux**

```bash
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Verify Model Files

Ensure the following files exist in the project root:
- `lstm_model.h5` – Pre-trained LSTM model
- `tokenizer.pkl` – Tokenizer object
- `max_len.pkl` – Maximum sequence length (default: 748)

---

## ▶️ Usage

### 🔹 Run the Streamlit App Locally

```bash
streamlit run app.py
```

Or using Python module:

```bash
python -m streamlit run app.py
```

The app will open at `http://localhost:8501`

**How to Use:**
1. Enter a sequence of words in the text input box
2. Click **"Predict Next Word"**
3. View the predicted next word displayed below

**Example Inputs:**
- `"the quick brown"`
- `"machine learning is"`
- `"artificial intelligence and"`

---

## 🛠 Tech Stack

* **Language:** Python 3.8+
* **Deep Learning:** TensorFlow / Keras
* **Web Framework:** Streamlit
* **Embeddings:** TensorFlow Tokenizer & Embedding Layer
* **Data Processing:** NumPy, Pandas
* **Model Format:** HDF5 (.h5)

---

## 📊 Model Details

**Architecture:**
```
Input (Sequence of tokens) 
    ↓
Embedding Layer (vocab_size=10000, embedding_dim=50)
    ↓
LSTM Layer (128 units, activation='relu')
    ↓
Dense Output Layer (vocab_size=10000, activation='softmax')
    ↓
Output (Next word prediction)
```

**Training Details:**
- **Dataset:** Quote dataset (qoute_dataset.csv)
- **Epochs:** 100
- **Batch Size:** 128
- **Optimizer:** Adam
- **Loss Function:** Categorical Crossentropy
- **Train/Val Split:** 90% / 10%

---

## 🚀 Deployment

### Deploy on Streamlit Cloud

1. Push code to GitHub repository
2. Go to [streamlit.io](https://streamlit.io)
3. Click **"New app"**
4. Select your GitHub repository and branch
5. Streamlit will auto-detect `requirements.txt` and install dependencies
6. App will be live within minutes!

### Deploy with Docker

```bash
docker build -t next-word-prediction .
docker run -p 8501:8501 next-word-prediction
```

---

## 📌 Use Cases

* **Text Completion & Autocomplete** - Mobile keyboards, search engines
* **Content Generation Assistance** - Writing tools, email composition
* **Accessibility Tools** - Word prediction for users with disabilities
* **Educational Purposes** - Learning NLP and LSTM fundamentals
* **Interactive Chatbots** - Enhancing response generation

---

## ⚠️ Important Notes

* The model is trained on quotes; predictions work best with quote-like narratives
* Vocabulary is limited to 10,000 most frequent words; rare words won't be recognized
* Requires TensorFlow 2.13+ for compatibility
* Ensure all `.pkl` and `.h5` files are in the project root directory

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 👨‍💻 Author

**Aditya Tiwari**  
GitHub: [@adityat22](https://github.com/adityat22)

---

## 🙋 Support

For issues, questions, or suggestions, please open an [Issue](https://github.com/adityat22/Next-Word-Prediction-System/issues) on GitHub.
