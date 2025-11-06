# Generator Daftar Password Tanggal

Program Python sederhana untuk menghasilkan daftar password berbasis tanggal dalam format CSV. Program ini membuat daftar tanggal berurutan dari tanggal mulai hingga tanggal akhir dengan format `ddmmyyyy` (8 digit).

## 📋 Deskripsi

Program ini berguna untuk membuat wordlist/daftar password yang berisi kombinasi tanggal. Setiap tanggal diformat menjadi 8 digit (contoh: `01012000` untuk 1 Januari 2000) dan disimpan dalam file CSV.

## 🚀 Fitur

- Generate tanggal otomatis dari rentang yang ditentukan
- Format output: `ddmmyyyy` (8 digit)
- Export ke file CSV
- Menampilkan preview 5 tanggal pertama dan terakhir
- File CSV disimpan di folder yang sama dengan script

## 📦 Requirements

- Python 3.x
- Module bawaan Python:
  - `csv`
  - `os`
  - `datetime`

## 💻 Cara Penggunaan

### 1. Download atau Copy Script

Simpan kode program dengan nama file, misalnya `generate_dates.py`

### 2. Edit Tanggal

Buka file `generate_dates.py` dan ubah bagian berikut sesuai kebutuhan:

```python
# UBAH TANGGAL MULAI DAN TANGGAL AKHIR (YYYY, MM, DD)
start_date = datetime(2000, 1, 1)    # Tanggal mulai
end_date = datetime(2003, 12, 31)    # Tanggal akhir
```

**Format:** `datetime(TAHUN, BULAN, TANGGAL)`

**Contoh:**
- `datetime(2020, 1, 1)` = 1 Januari 2020
- `datetime(2025, 12, 31)` = 31 Desember 2025

### 3. Jalankan Program

Buka terminal/command prompt di folder tempat file disimpan, lalu jalankan:

```bash
python generate_dates.py
```

### 4. Output

Program akan menghasilkan file CSV dengan nama `tanggal_2000_2003.csv` (sesuai rentang tahun yang ditentukan) di folder yang sama dengan script.

## 📄 Format Output

File CSV yang dihasilkan berisi satu kolom tanpa header, dengan format:

```
01012000
02012000
03012000
04012000
...
31122003
```

Setiap baris berisi satu tanggal dalam format `ddmmyyyy` (8 digit).

## 🔧 Kustomisasi

### Menambahkan Header CSV

Jika ingin menambahkan header pada file CSV, hilangkan tanda `#` pada baris berikut:

```python
# writer.writerow(['Tanggal'])  # Fungsi Untuk Menambahkan Header
```

Menjadi:

```python
writer.writerow(['Tanggal'])  # Fungsi Untuk Menambahkan Header
```

### Mengubah Format Tanggal

Untuk mengubah format output tanggal, edit bagian berikut:

```python
formatted_date = current_date.strftime("%d%m%Y")
```

**Contoh format lain:**
- `"%Y%m%d"` = YYYYMMDD (contoh: 20000101)
- `"%m%d%Y"` = MMDDYYYY (contoh: 01012000)
- `"%d-%m-%Y"` = DD-MM-YYYY (contoh: 01-01-2000)

## 📊 Contoh Output Program

```
File 'tanggal_2000_2003.csv' berhasil dibuat!
Lokasi file: /path/to/your/folder/tanggal_2000_2003.csv
Total 1461 tanggal telah disimpan.

Contoh 5 tanggal pertama:
01012000
02012000
03012000
04012000
05012000

Contoh 5 tanggal terakhir:
27122003
28122003
29122003
30122003
31122003
```

## ⚠️ Catatan Penting

- Semakin besar rentang tanggal, semakin besar ukuran file CSV yang dihasilkan
- Rentang 1 tahun ≈ 365 baris
- Rentang 4 tahun (2000-2003) ≈ 1461 baris
- Pastikan memiliki cukup ruang penyimpanan untuk file output

## 📝 Lisensi

Program ini bersifat open source dan dapat digunakan secara bebas untuk keperluan pembelajaran dan penggunaan pribadi.

## 🤝 Kontribusi

Jika ingin mengembangkan program ini, beberapa ide fitur tambahan:
- Input interaktif untuk tanggal
- Pilihan format output (CSV, TXT, JSON)
- Opsi untuk menambahkan variasi (dengan/tanpa separator)
- Generate dengan pola tertentu (hanya hari kerja, dll)

---

**Dibuat dengan Python 🐍**
