import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Contoh data produk dan pengguna
data_produk = {
    'produk_id': [1, 2, 3, 4, 5],
    'harga': [100, 200, 150, 300, 250],
    'rating': [4.5, 4.0, 4.5, 5.0, 4.0]
}

data_pengguna = {
    'user_id': [1, 2, 3],
    'produk_id': [1, 2, 3]  # Produk yang dibeli oleh pengguna
}

# Mengonversi data ke dalam format DataFrame
produk_df = pd.DataFrame(data_produk)
pengguna_df = pd.DataFrame(data_pengguna)

# Menyiapkan data untuk KNN
X = produk_df[['harga', 'rating']]  # Fitur yang digunakan untuk rekomendasi

# Membuat model KNN untuk mencari produk yang mirip
model_knn = NearestNeighbors(n_neighbors=2, metric='euclidean')
model_knn.fit(X)

# Mencari produk yang serupa dengan produk yang dipilih pengguna
produk_dipilih = [1]  # Produk yang dibeli pengguna, misalnya produk ID 1
produk_pilihan = produk_df[produk_df['produk_id'] == produk_dipilih[0]]
produk_pilihan_features = produk_pilihan[['harga', 'rating']]

# Mendapatkan rekomendasi produk serupa
distances, indices = model_knn.kneighbors(produk_pilihan_features)
print(f"Rekomendasi produk untuk pengguna berdasarkan produk yang dipilih {produk_dipilih}:")
for idx in indices[0]:
    print(f"Produk ID: {produk_df.iloc[idx]['produk_id']} dengan harga {produk_df.iloc[idx]['harga']} dan rating {produk_df.iloc[idx]['rating']}")
