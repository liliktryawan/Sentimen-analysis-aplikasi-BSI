# Sentiment Analysis Aplikasi Beyond BSI - Machine Learning & Deep Learning

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://www.tensorflow.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Proyek analisis sentimen ulasan pengguna aplikasi **Beyond by BSI Mobile** dari Google Play Store menggunakan teknik Machine Learning dan Deep Learning.

---

## 📋 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis sentimen dari ulasan pengguna aplikasi Beyond (BSI Mobile Banking) yang dikumpulkan dari Google Play Store. Analisis dilakukan menggunakan berbagai algoritma Machine Learning dan Deep Learning untuk mengklasifikasikan sentimen menjadi kategori positif, negatif, atau netral.

### Fitur Utama:
- 🔍 **Web Scraping** ulasan dari Google Play Store
- 🧹 **Text Preprocessing** menggunakan NLP Indonesia (Sastrawi)
- 📊 **Exploratory Data Analysis (EDA)** dengan visualisasi
- 🤖 **Multiple ML/DL Models** untuk perbandingan performa
- 📈 **Model Evaluation** dengan berbagai metrik
- ☁️ **Word Cloud** untuk visualisasi kata-kata dominan

---

## 📁 Struktur Proyek

```
Playstore/
├── BMPL_Proyek_Sentiment_Analysis.ipynb  # Notebook utama analisis
├── Scraping_aplikasi_beyond.py           # Script scraping data
├── review_beyond_apps.csv                # Dataset ulasan (31MB+)
├── requirement.txt                       # Dependencies
└── README.md                             # Dokumentasi ini
```

---

## 🛠️ Teknologi & Library

### Core Libraries:
- **TensorFlow** - Deep Learning framework
- **Scikit-learn** - Machine Learning algorithms
- **Pandas & NumPy** - Data manipulation
- **Matplotlib** - Data visualization

### NLP Libraries:
- **NLTK** - Natural Language Toolkit
- **Sastrawi** - Indonesian text processing (stemming & stopwords)
- **WordCloud** - Visualisasi kata

### Data Collection:
- **google-play-scraper** - Scraping ulasan Google Play Store
- **imbalanced-learn** - Handling imbalanced dataset

---

## 📦 Instalasi

### 1. Clone Repository
```bash
git clone git@github-lilik:liliktryawan/Sentimen-analysis-aplikasi-BSI-ML-dan-DL-.git
cd Sentimen-analysis-aplikasi-BSI-ML-dan-DL-
```

### 2. Install Dependencies
```bash
pip install -r requirement.txt
```

### 3. Download NLTK Data (Jika diperlukan)
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 🚀 Cara Penggunaan

### 1. Scraping Data Ulasan
Jalankan script untuk mengumpulkan ulasan dari Google Play Store:

```bash
python Scraping_aplikasi_beyond.py
```

Script ini akan:
- Mengambil 10,000 ulasan terbaru aplikasi Beyond
- Menyimpan data ke file `review_beyond_apps.csv`
- Menggunakan sorting berdasarkan relevansi

### 2. Analisis Sentimen
Buka dan jalankan Jupyter Notebook:

```bash
jupyter notebook BMPL_Proyek_Sentiment_Analysis.ipynb
```

---

## 📊 Metodologi

### 1. **Data Collection**
- Sumber: Google Play Store
- Aplikasi: Beyond by BSI Mobile (`co.id.bankbsi.superapp`)
- Jumlah data: ~10,000 ulasan
- Bahasa: Indonesia

### 2. **Data Preprocessing**
- **Cleaning**: Menghapus missing values
- **Text Preprocessing**:
  - Case folding (lowercase)
  - Remove special characters & numbers
  - Tokenization
  - Stopword removal (Bahasa Indonesia)
  - Stemming menggunakan Sastrawi

### 3. **Feature Engineering**
- TF-IDF Vectorization
- Word Embeddings (untuk Deep Learning)
- Feature extraction dari rating dan metadata

### 4. **Modeling**
Proyek ini mengimplementasikan berbagai algoritma:

#### Machine Learning:
- Naive Bayes
- Support Vector Machine (SVM)
- Random Forest
- Logistic Regression

#### Deep Learning:
- LSTM (Long Short-Term Memory)
- CNN (Convolutional Neural Network)
- Hybrid Models

### 5. **Evaluation**
Metrik evaluasi yang digunakan:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 📈 Dataset

### Informasi Dataset
- **File**: `review_beyond_apps.csv`
- **Size**: ~31 MB
- **Rows**: ~10,000 ulasan
- **Columns**:
  - `reviewId`: ID unik ulasan
  - `userName`: Nama pengguna
  - `userImage`: URL foto profil
  - `content`: Isi ulasan (teks)
  - `score`: Rating (1-5 bintang)
  - `thumbsUpCount`: Jumlah likes
  - `reviewCreatedVersion`: Versi app saat review
  - `at`: Timestamp review
  - `replyContent`: Balasan developer
  - `repliedAt`: Timestamp balasan
  - `appVersion`: Versi aplikasi

---

## 🎯 Hasil & Insights

> **Note**: Hasil analisis lengkap dapat dilihat di notebook `BMPL_Proyek_Sentiment_Analysis.ipynb`

### Key Findings:
- Distribusi sentimen pengguna
- Kata-kata yang paling sering muncul (positif & negatif)
- Performa model terbaik
- Rekomendasi improvement untuk aplikasi

---

## 🔧 Troubleshooting

### SSH Connection Issues
Jika mengalami masalah koneksi SSH saat clone/push:

```bash
# Gunakan SSH over HTTPS (port 443)
git remote set-url origin git@github-lilik:liliktryawan/Sentimen-analysis-aplikasi-BSI-ML-dan-DL-.git
```

Pastikan SSH config di `~/.ssh/config` sudah dikonfigurasi:
```
Host github-lilik
  HostName ssh.github.com
  Port 443
  User git
  IdentityFile ~/.ssh/id_lilik_github
  IdentitiesOnly yes
```

---

## 👨‍💻 Author

**Lilik Triawan**
- GitHub: [@liliktryawan](https://github.com/liliktryawan)

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **BSI (Bank Syariah Indonesia)** - Aplikasi Beyond
- **Google Play Store** - Sumber data ulasan
- **Sastrawi** - Indonesian NLP library
- **TensorFlow & Scikit-learn** - ML/DL frameworks

---

## 📞 Contact & Support

Jika ada pertanyaan atau saran, silakan buat issue di repository ini atau hubungi melalui GitHub.

---

**Happy Analyzing! 🚀📊**