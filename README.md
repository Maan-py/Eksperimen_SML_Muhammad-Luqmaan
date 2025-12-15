## Deskripsi Dataset

Dataset UNSW-NB15 merupakan dataset cybersecurity yang digunakan untuk membangun sistem Intrusion Detection System (IDS). Dataset ini dikembangkan oleh Australian Centre for Cyber Security (ACCS) dan berisi data lalu lintas jaringan yang mencakup aktivitas normal serta berbagai jenis serangan (attack).

Setiap baris data merepresentasikan satu aliran koneksi jaringan (network flow) yang diekstraksi dari traffic nyata menggunakan kombinasi tools seperti Argus dan Bro-IDS. Dataset ini terdiri dari fitur numerik dan kategorikal yang menggambarkan karakteristik koneksi jaringan, pola paket, serta perilaku komunikasi antar host.

## Penjelasan Fitur

Berikut adalah penjelasan fitur utama yang digunakan pada dataset UNSW-NB15:

### 1. Identitas Data
- **id**  
  Identifier unik untuk setiap record. Fitur ini tidak memiliki makna prediktif terhadap serangan dan umumnya tidak digunakan dalam pemodelan.

### 2. Informasi Dasar Koneksi
- **dur**  
  Durasi koneksi jaringan dalam satuan detik.
- **proto**  
  Protokol jaringan yang digunakan (misalnya TCP, UDP, ICMP).
- **service**  
  Jenis layanan jaringan yang diakses, seperti HTTP, FTP, DNS, dan lainnya.
- **state**  
  Status koneksi jaringan yang menggambarkan kondisi akhir koneksi (misalnya FIN, CON, INT).

### 3. Statistik Paket dan Byte
- **spkts**  
  Jumlah paket yang dikirim dari source ke destination.
- **dpkts**  
  Jumlah paket yang dikirim dari destination ke source.
- **sbytes**  
  Total byte yang dikirim dari source ke destination.
- **dbytes**  
  Total byte yang dikirim dari destination ke source.
- **rate**  
  Laju pengiriman paket dalam satuan paket per detik.

### 4. Time-To-Live (TTL) dan Beban Data
- **sttl**  
  Nilai TTL paket dari source.
- **dttl**  
  Nilai TTL paket dari destination.
- **sload**  
  Beban data dari source dalam bit per detik.
- **dload**  
  Beban data dari destination dalam bit per detik.

### 5. Perilaku Flow dan Interval Waktu
- **sinpkt**  
  Rata-rata interval waktu antar paket yang dikirim dari source.
- **dinpkt**  
  Rata-rata interval waktu antar paket yang dikirim dari destination.
- **sjit**  
  Jitter (variasi waktu) pengiriman paket dari source.
- **djit**  
  Jitter pengiriman paket dari destination.

### 6. Fitur Agregasi Koneksi
- **ct_srv_src**  
  Jumlah koneksi ke layanan yang sama dari source dalam periode waktu tertentu.
- **ct_state_ttl**  
  Jumlah kombinasi state dan TTL yang sama pada koneksi jaringan.
- **ct_dst_ltm**  
  Jumlah koneksi ke destination dalam jangka waktu tertentu.
- **ct_src_ltm**  
  Jumlah koneksi dari source dalam jangka waktu tertentu.

### 7. Informasi Login dan Port
- **is_ftp_login**  
  Menunjukkan apakah terjadi login FTP yang berhasil.
- **is_sm_ips_ports**  
  Menunjukkan apakah source dan destination memiliki IP dan port yang sama.

### 8. Target Klasifikasi
- **label**  
  Label target biner, dengan nilai 0 untuk traffic normal dan 1 untuk traffic serangan.
- **attack_cat**  
  Kategori jenis serangan, seperti Fuzzers, DoS, Exploit, Reconnaissance, dan lainnya.
