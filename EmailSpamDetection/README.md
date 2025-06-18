
# 📧 Email Spam Detection using Machine Learning

This is a beginner-friendly machine learning project that builds a lightweight, accurate email spam classifier. It uses **TF-IDF** for feature extraction, **Naive Bayes** for classification, and **Streamlit** for a stylish web interface.

---

## 🎯 Objective

Automatically detect spam emails using a machine learning model trained on labeled data (spam vs ham). This classifier is suitable for integration into webforms and achieves over **97% accuracy**.

---

## 🌟 Features

- Text cleaning: stopword removal, punctuation cleanup, stemming
- Feature extraction using TF-IDF
- Multinomial Naive Bayes classifier
- Evaluation with Accuracy, Precision, Recall
- Saved model for reuse (`spam_classifier.pkl`)
- Responsive **Streamlit web app** with custom styling and background

---

## 🖼 Preview

![App Preview](https://github.com/user-attachments/assets/bdc32613-d642-40fc-903b-86dbb5430673) <!-- Replace with your own screenshot or leave it for GitHub preview -->

---

## 🗂 Folder Structure

```
EmailSpamDetection/
├── app.py                  # Streamlit web app interface
├── data/
│   └── dataspam.csv        # SMS spam/ham dataset
├── model/
│   ├── spam_classifier.pkl
│   └── tfidf_vectorizer.pkl
├── notebook/
│   └── spam_detector.ipynb # Jupyter Notebook for training & testing
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🚀 How to Run

### 🔧 1. Install dependencies

```bash
pip install -r requirements.txt
```

### ▶️ 2. Launch the Streamlit app

```bash
streamlit run app.py
```

---

## 📈 Model Evaluation

| Metric     | Score   |
|------------|---------|
| Accuracy   | 97.8%   |
| Precision  | 100%    |
| Recall     | 84%     |
| Algorithm  | Naive Bayes (Multinomial) |

---

## 📦 Dataset Info

- Dataset: [UCI SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- Format: CSV with labels `spam` or `ham`

---

## 👩‍💻 Developed By

**Bathini Vignani**  

## 📌 Final Note

This project demonstrates the power of combining machine learning and web technologies in a beginner-friendly, visually clean way. It is ready to be showcased in portfolios, internship submissions, or academic evaluations.
