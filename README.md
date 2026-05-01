# Analisis Performa Logistik dan Penjualan Kategori Produk pada E-Commerce
## Deskripsi Project
Proyek ini bertujuan untuk membangun sebuah dashboard interaktif menggunakan Streamlit sebagai media visualisasi hasil analisis data e-commerce. Data yang digunakan merupakan hasil proses data cleaning yang telah disimpan dalam file main_data.csv.

Dashboard ini dirancang untuk memberikan gambaran ringkas dan informatif mengenai karakteristik data, termasuk distribusi penjualan, performa kategori produk, serta hubungan antara variabel operasional seperti keterlambatan pengiriman dan tingkat kepuasan pelanggan.

Pada dashboard ini ditampilkan beberapa komponen utama, yaitu:

Tampilan data awal (data preview) untuk memberikan gambaran struktur dataset.
Visualisasi top kategori produk berdasarkan total revenue.
Analisis hubungan antara keterlambatan pengiriman dan review score pelanggan.

Dengan adanya dashboard ini, diharapkan proses analisis data menjadi lebih mudah dipahami secara visual serta dapat membantu dalam pengambilan keputusan berbasis data (data-driven decision making).
## 🗂️ Struktur Direktori
```submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───customers_dataset.csv
| ├───order_items_dataset.csv
| ├───order_payments_dataset.csv
| ├───order_reviews_dataset.csv
| ├───orders_dataset.csv
| └───products_dataset.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```
## 📦Setup Environment
## Pakai anaconda
```bash
conda create --name ecom-ds python=3.9
conda activate ecom-ds
pip install -r requirements.txt
```
## Menggunakan Terminal / Shell 
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
## 🚀 Panduan Menjalankan Aplikasi
### Clone Repositori
Langkah pertama, clone repositori:
```bash
git clone https://github.com/rafidjanur/Fundamental_analisis_data.git
```

### Instalasi Library
Instal semua dependensi yang dibutuhkan menggunakan pip:
```bash
pip install -r requirements.txt
```

### Menjalankan Dashboard
Jalankan perintah berikut pada terminal di dalam direktori proyek:
```bash
cd dashboard
```
lalu
```bash
streamlit run dashboard.py
```

atau

```bash
python -m streamlit run dashboard/dashboard.py
```
Aplikasi akan secara otomatis terbuka di browser default Anda.

