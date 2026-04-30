import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Konfigurasi Halaman
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# 2. Judul Dashboard
st.title("E-Commerce Dashboard")
st.markdown("Dashboard ini menampilkan analisis performa e-commerce berdasarkan data transaksi historis.")

# 3. Fungsi untuk load dan pra-pemrosesan data
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/main_data.csv")
    # Konversi kolom waktu ke tipe datetime
    if 'order_purchase_timestamp' in df.columns:
        df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

try:
    df = load_data()

    # --- Bagian Data Preview ---
    with st.expander("Klik untuk melihat Preview Data"):
        st.write("Berikut adalah 5 baris pertama dari dataset:")
        st.dataframe(df.head())
    
    st.divider()

    # --- TREN REVENUE BULANAN (Full Width) ---
    st.header("1. Tren Performa Penjualan")
    
    # Agregasi data revenue bulanan
    monthly_revenue = df.groupby(df['order_purchase_timestamp'].dt.to_period('M'))['revenue'].sum()
    monthly_revenue.index = monthly_revenue.index.astype(str) # Ubah ke string agar rapi di plot

    fig1, ax1 = plt.subplots(figsize=(12, 5))
    monthly_revenue.plot(kind='line', color='navy', linewidth=2.5, marker='o', markersize=6, ax=ax1)
    ax1.set_title('Tren Revenue Bulanan', fontsize=16, fontweight='bold', color='darkblue')
    ax1.set_xlabel('Periode (Bulan)', fontsize=12)
    ax1.set_ylabel('Total Revenue', fontsize=12)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    plt.xticks(rotation=45)
    sns.despine(ax=ax1)
    
    st.pyplot(fig1)
    st.info("Insight: Terjadi pertumbuhan revenue yang sangat signifikan sepanjang tahun 2017, mencapai puncaknya pada akhir tahun (November). Pada tahun 2018, revenue cenderung stabil tinggi dengan sedikit fluktuasi yang mengindikasikan adanya faktor musiman dalam perilaku belanja.")

    st.divider()

    # --- KATEGORI & REVIEW (2 Kolom) ---
    st.header("2. Analisis Produk & Kepuasan Pelanggan")
    col1, col2 = st.columns(2)

    with col1:
        # Top 10 Kategori Produk
        category_analysis = df.groupby('product_category_name')['revenue'].sum().reset_index()
        top10 = category_analysis.sort_values(by='revenue', ascending=False).head(10)
        
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        colors = sns.color_palette('viridis', len(top10))
        ax2.barh(top10['product_category_name'], top10['revenue'], color=colors)
        ax2.set_title('Top 10 Kategori Produk Berdasarkan Revenue', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Total Revenue', fontsize=12)
        ax2.set_ylabel('Kategori Produk', fontsize=12)
        ax2.invert_yaxis()
        
        st.pyplot(fig2)
        st.info("Insight: Kategori seperti 'cama_mesa_banho' dan 'beleza_saude' adalah penyumbang revenue terbesar. Namun, analisis sebelumnya menunjukkan bahwa tingginya penjualan tidak selalu sejalan dengan tingginya kepuasan pelanggan.")

    with col2:
        # Distribusi Review Score
        review_counts = df['review_score'].value_counts().sort_index()
        
        fig3, ax3 = plt.subplots(figsize=(8, 6))
        colors = sns.color_palette('magma', len(review_counts))
        review_counts.plot(kind='bar', color=colors, edgecolor='black', ax=ax3)
        ax3.set_title('Distribusi Review Score', fontsize=14, fontweight='bold')
        ax3.set_xlabel('Review Score', fontsize=12)
        ax3.set_ylabel('Jumlah', fontsize=12)
        ax3.tick_params(axis='x', rotation=0)
        ax3.grid(axis='y', linestyle='--', alpha=0.7)
        
        st.pyplot(fig3)
        st.info("Insight: Mayoritas pelanggan merasa puas (skor 4 dan 5). Akan tetapi, volume skor 1 yang cukup terlihat menandakan masih ada porsi pelanggan yang mengalami masalah serius saat bertransaksi.")

    st.divider()

    # --- ANALISIS KETERLAMBATAN PENGIRIMAN (2 Kolom) ---
    st.header("3. Analisis Performa Pengiriman Logistik")
    col3, col4 = st.columns(2)

    with col3:
        # Distribusi Delivery Delay
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        sns.histplot(data=df, x='delivery_delay', bins=30, color='teal', edgecolor='black', kde=True, alpha=0.8, ax=ax4)
        ax4.set_title('Distribusi Waktu Pengiriman (Delivery Delay)', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Selisih Hari (Aktual - Estimasi)', fontsize=12)
        ax4.set_ylabel('Frekuensi', fontsize=12)
        ax4.grid(axis='y', linestyle='--', alpha=0.7)
        
        st.pyplot(fig4)
        st.info("Insight: Distribusi menunjukkan bahwa sistem logistik sebenarnya berjalan sangat baik karena mayoritas pengiriman (nilai negatif) tiba jauh sebelum batas estimasi. Namun, ada *outlier* keterlambatan parah di sisi kanan grafik.")

    with col4:
        # Hubungan Delay vs Review
        delay_review = df.groupby('delivery_delay')['review_score'].mean().reset_index()
        delay_review_sorted = delay_review.sort_values('delivery_delay')
        
        fig5, ax5 = plt.subplots(figsize=(10, 6))
        ax5.plot(delay_review_sorted['delivery_delay'], delay_review_sorted['review_score'],
                 color='navy', linewidth=2.5, marker='o', markersize=5, markerfacecolor='white', markeredgewidth=1.5)
        ax5.set_title('Hubungan Keterlambatan vs Kepuasan', fontsize=14, fontweight='bold', color='navy')
        ax5.set_xlabel('Keterlambatan Pengiriman (hari)', fontsize=12)
        ax5.set_ylabel('Rata-rata Review Score', fontsize=12)
        ax5.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.3)
        sns.despine(ax=ax5)
        
        st.pyplot(fig5)
        st.info("Insight: Ada tren penurunan garis yang jelas. Semakin tinggi angka *delivery delay* (semakin lama barang sampai melewati batas estimasi), semakin menurun pula rata-rata review score yang diberikan oleh pelanggan.")

except FileNotFoundError:
    st.error("File main_data.csv tidak ditemukan. Pastikan Anda menyimpan dataset dengan nama yang tepat pada folder yang sama dengan file dashboard ini.")