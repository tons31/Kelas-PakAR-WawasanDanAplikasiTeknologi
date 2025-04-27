
# User Manual: Sistem Rekomendasi Produk Berbasis K-Nearest Neighbors (KNN)

## Pendahuluan
Sistem rekomendasi berbasis **K-Nearest Neighbors (KNN)** ini digunakan untuk memberikan saran produk yang mirip berdasarkan produk yang telah dibeli oleh pengguna. Dengan menggunakan fitur-fitur seperti **harga** dan **rating**, sistem ini dapat memberikan rekomendasi produk yang relevan, meningkatkan pengalaman belanja online dengan cara yang lebih personal.

---

## Panduan Sebelum Menjalankan Program

Sebelum menjalankan program Python ini, pastikan Anda telah menyiapkan hal-hal berikut:

1. **Instalasi Python**: 
   - Program ini membutuhkan **Python 3.x**. Pastikan Anda sudah menginstal Python di sistem Anda. Anda bisa mengunduhnya di [situs resmi Python](https://www.python.org/downloads/).
   
2. **Instalasi Library yang Diperlukan**:
   - Program ini menggunakan **pandas** dan **scikit-learn** (untuk KNN). Anda perlu menginstal library ini menggunakan **pip**.
   - Buka terminal atau command prompt dan jalankan perintah berikut:
     ```bash
     pip install pandas scikit-learn
     ```

3. **Persiapkan Data**:
   - Anda perlu menyiapkan data **produk** dan **pengguna** dalam format yang sesuai. Berikut adalah contoh data produk dan pengguna yang dapat Anda gunakan dalam sistem ini.

   **Contoh Data Produk**:
   | produk_id | harga | rating |
   |-----------|-------|--------|
   | 1         | 100   | 4.5    |
   | 2         | 200   | 4.0    |
   | 3         | 150   | 4.5    |
   | 4         | 300   | 5.0    |
   | 5         | 250   | 4.0    |

   **Contoh Data Pengguna**:
   | user_id | produk_id |
   |---------|-----------|
   | 1       | 1         |
   | 2       | 2         |
   | 3       | 3         |

4. **Menyiapkan File Kode Python**:
   - Salin kode Python berikut ke dalam file Python (.py) di editor teks seperti VS Code, PyCharm, atau Jupyter Notebook.

---

## Langkah-langkah Penggunaan

### 1. Menyiapkan Data Produk dan Pengguna
Sistem ini memerlukan dua jenis data:
- **Data Produk**: Berisi informasi tentang produk, seperti **produk_id**, **harga**, dan **rating**.
- **Data Pengguna**: Menyimpan informasi tentang produk yang telah dibeli oleh pengguna.

Contoh format data:
- **Data Produk**:
    | produk_id | harga | rating |
    |-----------|-------|--------|
    | 1         | 100   | 4.5    |
    | 2         | 200   | 4.0    |
    | 3         | 150   | 4.5    |
    | 4         | 300   | 5.0    |
    | 5         | 250   | 4.0    |

- **Data Pengguna**:
    | user_id | produk_id |
    |---------|-----------|
    | 1       | 1         |
    | 2       | 2         |
    | 3       | 3         |

### 2. Mengonversi Data ke Format yang Sesuai
Data produk dan pengguna perlu dikonversi menjadi format **DataFrame** menggunakan **pandas**. DataFrame adalah struktur data yang mudah digunakan dalam analisis.

```python
produk_df = pd.DataFrame(data_produk)
pengguna_df = pd.DataFrame(data_pengguna)
```

### 3. Menyiapkan Model KNN
Model **K-Nearest Neighbors (KNN)** digunakan untuk menemukan produk yang paling mirip berdasarkan fitur yang diberikan (dalam hal ini **harga** dan **rating**). 
- **n_neighbors=2**: Menyatakan bahwa kita akan mencari 2 produk yang paling mirip.
- **metric='euclidean'**: Menggunakan jarak Euclidean untuk mengukur kesamaan antar produk.

```python
X = produk_df[['harga', 'rating']]  # Fitur yang digunakan untuk rekomendasi

model_knn = NearestNeighbors(n_neighbors=2, metric='euclidean')
model_knn.fit(X)
```

### 4. Mencari Rekomendasi Berdasarkan Produk yang Dipilih Pengguna
Sistem ini mencari produk yang mirip dengan produk yang telah dibeli oleh pengguna, berdasarkan **harga** dan **rating** produk yang dipilih. Pengguna memilih produk, misalnya **produk ID 1**, dan sistem akan mencari produk yang paling mirip.

```python
produk_dipilih = [1]  # Produk yang dibeli pengguna, misalnya produk ID 1
produk_pilihan = produk_df[produk_df['produk_id'] == produk_dipilih[0]]
produk_pilihan_features = produk_pilihan[['harga', 'rating']]
```

### 5. Mendapatkan Rekomendasi Produk
Setelah memilih produk, sistem menggunakan model KNN untuk mencari produk serupa. Hasil rekomendasi akan mencakup **produk_id**, **harga**, dan **rating** produk yang serupa dengan produk yang dipilih.

```python
distances, indices = model_knn.kneighbors(produk_pilihan_features)
```

Hasilnya akan dicetak di layar sebagai berikut:

```python
print(f"Rekomendasi produk untuk pengguna berdasarkan produk yang dipilih {produk_dipilih}:")
for idx in indices[0]:
    print(f"Produk ID: {produk_df.iloc[idx]['produk_id']} dengan harga {produk_df.iloc[idx]['harga']} dan rating {produk_df.iloc[idx]['rating']}")
```

---

### **Contoh Hasil Rekomendasi**
Jika pengguna memilih **Produk ID 1**, sistem akan menampilkan produk-produk yang paling mirip berdasarkan **harga** dan **rating**:

```
Rekomendasi produk untuk pengguna berdasarkan produk yang dipilih [1]:
Produk ID: 3 dengan harga 150 dan rating 4.5
Produk ID: 5 dengan harga 250 dan rating 4.0
```

---

### **Fitur Utama**
- **Personalisasi Rekomendasi**: Memberikan saran produk yang relevan berdasarkan produk yang telah dibeli oleh pengguna.
- **Metode Penghitungan**: Menggunakan metode **K-Nearest Neighbors (KNN)** dengan **jarak Euclidean** untuk mengukur kesamaan antara produk.
- **Pencarian Rekomendasi**: Mencari 2 produk terdekat dengan produk yang dipilih oleh pengguna.

### **Catatan Penting**
- **Data yang Dibutuhkan**: Pastikan Anda sudah menyiapkan data yang valid untuk produk dan pengguna sebelum menjalankan model.
- **Skalabilitas**: Sistem ini cocok untuk dataset kecil hingga menengah. Untuk dataset besar, disarankan untuk menggunakan teknik yang lebih canggih atau sistem distribusi.

### **Kesimpulan**
Sistem rekomendasi berbasis **K-Nearest Neighbors (KNN)** ini memberikan rekomendasi produk yang relevan bagi pengguna, meningkatkan pengalaman belanja online. Dengan menggunakan **harga** dan **rating** sebagai fitur, sistem ini dapat memberikan saran produk yang lebih personal dan meningkatkan konversi di e-commerce.
