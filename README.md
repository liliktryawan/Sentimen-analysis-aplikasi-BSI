# Sentiment Analysis Aplikasi Beyond BSI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Proyek analisis sentimen ulasan pengguna aplikasi Beyond by BSI Mobile dari Google Play Store menggunakan pendekatan Machine Learning dan Deep Learning.**

[Deskripsi](#-deskripsi-proyek) •
[Dataset](#-dataset) •
[Metodologi](#-metodologi-pemodelan) •
[Hasil Analisis](#-performa--hasil-analisis) •
[Cara Penggunaan](#-cara-penggunaan)

</div>

---

## Deskripsi Proyek

Aplikasi perbankan digital memiliki peran krusial dalam kepuasan nasabah. Proyek ini bertujuan untuk mengekstraksi wawasan berharga dari ulasan pengguna aplikasi **Beyond by BSI Mobile** di Google Play Store. Dengan menerapkan teknik pengolahan bahasa alami (NLP) dan pemodelan prediktif, proyek ini mengklasifikasikan sentimen ulasan menjadi kategori **Positif, Negatif, atau Netral**.

Analisis ini membantu mengidentifikasi fitur yang disukai pengguna, masalah teknis yang sering terjadi, serta sentimen keseluruhan terhadap aplikasi secara otomatis.

### Fitur Utama
- 🔍 **Automated Web Scraping**: Pengumpulan data ulasan langsung dari Google Play Store.
- 🧹 **Indonesian NLP Pipeline**: Prapemrosesan teks khusus bahasa Indonesia (termasuk *stemming* dengan Sastrawi).
- 📊 **Exploratory Data Analysis (EDA)**: Visualisasi distribusi rating dan sentimen.
- 🤖 **Multi-Model Comparison**: Evaluasi performa berbagai algoritma ML dan DL.
- ☁️ **Word Cloud**: Visualisasi kata-kata dominan untuk ekstraksi topik.

---

## Struktur Proyek

```
├── 📓 BMPL_Proyek_Sentiment_Analysis.ipynb    # Notebook utama (Eksplorasi & Modeling)
├── 🕷️ Scraping_aplikasi_beyond.py             # Script otomatisasi scraping data
├── 📄 review_beyond_apps.csv                  # Dataset ulasan hasil scraping (~31MB)
├── 📋 requirement.txt                         # Daftar dependensi library
└── 📖 README.md                               # Dokumentasi proyek (file ini)
```

---

## Teknologi yang Digunakan

Proyek ini dibangun menggunakan berbagai library standar industri untuk Data Science dan Machine Learning:

| Kategori | Teknologi | Fungsi Utama |
|----------|-----------|--------------|
| **Core Frameworks** | TensorFlow, Keras | Pembuatan arsitektur Deep Learning (LSTM) |
| **Machine Learning** | Scikit-learn | Algoritma ML klasik (Logistic Regression, Random Forest), evaluasi metrik |
| **Data Processing** | Pandas, NumPy | Manipulasi DataFrame dan komputasi numerik |
| **Natural Language** | NLTK, Sastrawi | Tokenisasi, stopword removal, stemming bahasa Indonesia |
| **Data Collection** | google-play-scraper | Pengumpulan data ulasan aplikasi |
| **Visualization** | Matplotlib, WordCloud | Visualisasi grafik EDA dan kata dominan |

---

## Dataset

Dataset diperoleh dengan melakukan scraping mandiri menggunakan script `Scraping_aplikasi_beyond.py`.

| Informasi | Deskripsi |
|-----------|-----------|
| **Sumber Data** | Google Play Store (`co.id.bankbsi.superapp`) |
| **Jumlah Baris** | ~10.000 ulasan |
| **Ukuran File** | ~31 MB (`review_beyond_apps.csv`) |
| **Bahasa** | Indonesia |

**Atribut Utama Dataset:**
- `content`: Teks ulasan dari pengguna (Target klasifikasi)
- `score`: Rating bintang 1 hingga 5
- `at`: Timestamp waktu ulasan diberikan
- `thumbsUpCount`: Jumlah *likes* yang diterima ulasan

---

## Metodologi Pemodelan

Proyek ini mengikuti siklus standar *Data Science*:

1. **Pengumpulan Data**: Scraping ulasan terbaru dari Play Store.
2. **Data Cleaning**: Penanganan *missing values* dan data duplikat.
3. **Text Preprocessing**: 
   - *Case folding* (huruf kecil)
   - Penghapusan tanda baca, angka, dan karakter khusus
   - *Tokenization* (pemisahan kata)
   - *Stopword removal* (menghapus kata hubung/tidak penting)
   - *Stemming* (pengembalian ke kata dasar menggunakan Sastrawi)
4. **Feature Engineering**: 
   - TF-IDF Vectorization untuk model Machine Learning klasik.
   - Word Embeddings untuk arsitektur Deep Learning.
5. **Pemodelan**:
   - **Machine Learning**: Decision Tree (Baseline), Random Forest, dan Logistic Regression.
   - **Deep Learning**: Recurrent Neural Network menggunakan **LSTM** (*Long Short-Term Memory*).
6. **Evaluasi**: Menggunakan metrik *Accuracy, Precision, Recall*, dan *Confusion Matrix*.

---

## Performa & Hasil Analisis

Proyek ini mengevaluasi beberapa pendekatan algoritma dan menghasilkan model Deep Learning dengan performa yang superior.

### Tabel Komparasi Akurasi Model

| Algoritma / Arsitektur | Kategori | Akurasi Data Uji (Test) | Status |
|------------------------|----------|-------------------------|--------|
| **LSTM (Deep Learning)** | Neural Network | **~95.69%** | 🥇 **Best Model** |
| **Logistic Regression** | Machine Learning | **86.48%** | 🥈 Runner Up (ML) |
| **Random Forest** | Machine Learning | **84.26%** | 🥉 |
| **Decision Tree** | Machine Learning | 79.88% | Baseline |

> **Detail Arsitektur LSTM:** Model terbaik menggunakan kombinasi *Embedding Layer* untuk representasi densitas kata, *LSTM Layer* untuk menangkap konteks kalimat dan dependensi jarak jauh, serta *Dense Layer* untuk klasifikasi akhir dengan *Adam Optimizer*.

### Wawasan Bisnis (*Business Insights*)
Berdasarkan visualisasi *Word Cloud* dan ekstraksi teks:
- **Pendorong Kepuasan (Positif)**: Ulasan positif didominasi oleh kata-kata terkait kemudahan dalam bertransaksi, UI/UX baru yang lebih segar (Beyond), dan kelengkapan fitur perbankan syariah.
- **Titik Lemah (Negatif)**: Keluhan nasabah paling banyak berkaitan dengan kendala gagal *login*, pembaruan paksa yang memberatkan, serta isu server *timeout*.
- **Rekomendasi**: Model LSTM yang dikembangkan ini siap untuk di-*deploy* sebagai *pipeline* analisis *real-time*, sehingga tim Layanan Pelanggan (CS) BSI dapat segera mendeteksi komplain berat (*churn risk*) secara otomatis tanpa membaca ulasan satu per satu.

---

## Cara Penggunaan

### 1. Clone Repository

Unduh proyek ini ke dalam mesin lokal Anda:

```bash
git clone git@github.com:liliktryawan/Sentimen-analysis-aplikasi-BSI.git
cd Sentimen-analysis-aplikasi-BSI
```

*(Catatan: Pastikan Anda menjalankan perintah ini dari terminal yang mendukung Git)*

### 2. Instalasi Dependensi

Instal semua library yang dibutuhkan melalui `pip`:

```bash
pip install -r requirement.txt
```

Jika Anda baru pertama kali menggunakan NLTK, unduh resource yang diperlukan melalui Python:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 3. Mengumpulkan Data Baru (Opsional)

Jika Anda ingin melakukan pembaruan dataset dengan ulasan terbaru:

```bash
python Scraping_aplikasi_beyond.py
```
*(Script ini akan menimpa/memperbarui file `review_beyond_apps.csv`)*

### 4. Menjalankan Analisis

Buka dan jalankan semua cell di Jupyter Notebook untuk melihat proses EDA, pelatihan model, dan hasil evaluasi secara detail:

```bash
jupyter notebook BMPL_Proyek_Sentiment_Analysis.ipynb
```

---

## Author

**Lilik Triawan**  
GitHub: [@liliktryawan](https://github.com/liliktryawan)

---
