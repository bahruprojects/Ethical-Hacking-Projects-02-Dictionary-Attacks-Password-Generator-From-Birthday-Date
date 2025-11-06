# Dictionary Attacks Password Generator From Birthday Date

Program Python interaktif untuk menghasilkan daftar password berbasis tanggal dalam format CSV. Program ini meminta input tanggal mulai dan tanggal selesai dari pengguna, kemudian membuat daftar tanggal berurutan dengan format `ddmmyyyy` (8 digit).

## 📋 Deskripsi

Program ini berguna untuk membuat wordlist/daftar password yang berisi kombinasi tanggal. Pengguna dapat menentukan rentang tanggal secara interaktif melalui input, dan setiap tanggal akan diformat menjadi 8 digit (contoh: `01012000` untuk 1 Januari 2000) dan disimpan dalam file CSV.

## 🚀 Fitur

- ✅ **Input interaktif** - Pengguna dapat memasukkan tanggal mulai dan selesai
- ✅ **Validasi otomatis** - Memvalidasi format tanggal dan logika rentang
- ✅ **Format DD/MM/YYYY** - Format input sesuai standar Indonesia
- ✅ **Generate tanggal otomatis** - Membuat semua tanggal dalam rentang
- ✅ **Format output ddmmyyyy** - Password 8 digit tanpa separator
- ✅ **Export ke CSV** - File disimpan otomatis di folder script
- ✅ **Nama file dinamis** - Nama file menyesuaikan dengan rentang tahun
- ✅ **Preview hasil** - Menampilkan 5 tanggal pertama dan terakhir
- ✅ **User-friendly interface** - Tampilan dengan border dan emoji

## 📦 Requirements

- Python 3.x
- Module bawaan Python (tidak perlu instalasi tambahan):
  - `csv`
  - `os`
  - `datetime`

## 💻 Cara Penggunaan

### 1. Download Script

Simpan kode program dengan nama file, misalnya `Dictionary-Attacks-Password-Generator-From-Birthday-Date.py`

### 2. Jalankan Program

Buka terminal/command prompt di folder tempat file disimpan, lalu jalankan:

```bash
Dictionary-Attacks-Password-Generator-From-Birthday-Date.py
```

### 3. Input Tanggal

Program akan meminta input dari pengguna:

**a. Input Tanggal Mulai**
```
Masukkan TANGGAL MULAI (format: DD/MM/YYYY)
Contoh: 01/01/2000 : 
```
Ketik tanggal mulai, misalnya: `01/01/2020`

**b. Input Tanggal Selesai**
```
Masukkan TANGGAL SELESAI (format: DD/MM/YYYY)
Contoh: 31/12/2003 : 
```
Ketik tanggal selesai, misalnya: `31/12/2020`

### 4. Output

Program akan otomatis:
- Memproses semua tanggal dalam rentang
- Membuat file CSV dengan nama dinamis (contoh: `tanggal_2020_2020.csv`)
- Menyimpan file di folder yang sama dengan script
- Menampilkan informasi hasil dan preview

## 📺 Contoh Penggunaan Lengkap

```
==================================================
GENERATOR DAFTAR PASSWORD TANGGAL
==================================================

Masukkan TANGGAL MULAI (format: DD/MM/YYYY)
Contoh: 01/01/2000 : 01/01/2020

Masukkan TANGGAL SELESAI (format: DD/MM/YYYY)
Contoh: 31/12/2003 : 05/01/2020

✓ Memproses tanggal dari 01/01/2020 hingga 05/01/2020...

==================================================
✓ File 'tanggal_2020_2020.csv' berhasil dibuat!
✓ Lokasi file: /path/to/folder/tanggal_2020_2020.csv
✓ Total 5 tanggal telah disimpan.
==================================================

Contoh 5 tanggal pertama:
  01012020
  02012020
  03012020
  04012020
  05012020
```

## 📄 Format Output CSV

File CSV yang dihasilkan berisi satu kolom tanpa header, dengan format:

```
01012020
02012020
03012020
04012020
05012020
...
```

Setiap baris berisi satu tanggal dalam format `ddmmyyyy` (8 digit).

## ✅ Validasi Input

Program memiliki beberapa validasi otomatis:

### 1. Format Tanggal
❌ Input salah:
```
Masukkan TANGGAL MULAI (format: DD/MM/YYYY)
Contoh: 01/01/2000 : 2020-01-01
❌ Format salah! Gunakan format DD/MM/YYYY (contoh: 01/01/2000)
```

✅ Input benar:
```
Masukkan TANGGAL MULAI (format: DD/MM/YYYY)
Contoh: 01/01/2000 : 01/01/2020
```

### 2. Logika Rentang Tanggal
❌ Tanggal selesai lebih awal dari tanggal mulai:
```
Masukkan TANGGAL SELESAI (format: DD/MM/YYYY)
Contoh: 31/12/2003 : 01/01/2019
❌ Tanggal selesai tidak boleh lebih awal dari tanggal mulai!
```

Program akan terus meminta input ulang sampai format dan logika benar.

## 🔧 Kustomisasi

### 1. Menambahkan Header CSV

Jika ingin menambahkan header "Tanggal" di baris pertama CSV, hilangkan tanda `#`:

```python
# Dari:
# writer.writerow(['Tanggal'])

# Menjadi:
writer.writerow(['Tanggal'])
```

**Hasil CSV dengan header:**
```
Tanggal
01012020
02012020
...
```

### 2. Mengubah Format Output Tanggal

Edit bagian ini untuk mengubah format output:

```python
formatted_date = current_date.strftime("%d%m%Y")
```

**Contoh format lain:**
- `"%Y%m%d"` → `20200101` (YYYYMMDD)
- `"%m%d%Y"` → `01012020` (MMDDYYYY)
- `"%d-%m-%Y"` → `01-01-2020` (DD-MM-YYYY dengan separator)
- `"%Y/%m/%d"` → `2020/01/01` (YYYY/MM/DD dengan separator)

### 3. Mengubah Format Nama File

Edit bagian ini untuk mengubah pola nama file:

```python
filename = f"tanggal_{start_year}_{end_year}.csv"
```

**Contoh:**
```python
# Dengan tanggal lengkap:
filename = f"passwords_{start_date.strftime('%d%m%Y')}_{end_date.strftime('%d%m%Y')}.csv"
# Hasil: passwords_01012020_31122020.csv

# Dengan timestamp:
filename = f"wordlist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
# Hasil: wordlist_20231115_143052.csv
```

## 📊 Estimasi Ukuran File

| Rentang Waktu | Jumlah Baris | Ukuran File (approx) |
|---------------|--------------|----------------------|
| 1 hari        | 1            | < 1 KB               |
| 1 bulan       | ~30          | < 1 KB               |
| 1 tahun       | ~365         | 3-4 KB               |
| 5 tahun       | ~1,825       | 15-20 KB             |
| 10 tahun      | ~3,650       | 30-40 KB             |
| 20 tahun      | ~7,300       | 60-80 KB             |

*Catatan: Ukuran aktual tergantung pada format output dan encoding*

## ⚠️ Catatan Penting

- Pastikan format input tanggal benar: **DD/MM/YYYY**
- Tanggal selesai harus sama atau lebih besar dari tanggal mulai
- File output akan **menimpa** file dengan nama yang sama
- Rentang tanggal besar akan menghasilkan file besar
- Program berjalan di memori, rentang sangat besar (>50 tahun) mungkin lambat

## 🛡️ Penggunaan Etis

Program ini dibuat untuk tujuan:
- ✅ Pembelajaran pemrograman Python
- ✅ Testing keamanan sistem sendiri
- ✅ Riset keamanan dengan izin
- ✅ Analisis pola password

**JANGAN** digunakan untuk:
- ❌ Meretas akun orang lain
- ❌ Aktivitas ilegal
- ❌ Melanggar privasi orang lain

## 🐛 Troubleshooting

### Error: "Invalid date format"
**Penyebab:** Format input tanggal salah  
**Solusi:** Gunakan format DD/MM/YYYY (contoh: 31/12/2020)

### Error: "Permission denied"
**Penyebab:** Tidak ada izin menulis di folder  
**Solusi:** Jalankan program di folder dengan hak akses penuh

### Program berjalan sangat lambat
**Penyebab:** Rentang tanggal terlalu besar (>30 tahun)  
**Solusi:** Kurangi rentang atau bagi menjadi beberapa file

## 📝 Lisensi

Program ini bersifat open source dan dapat digunakan secara bebas untuk keperluan pembelajaran dan penggunaan yang etis.

## 💡 Ide Pengembangan

Beberapa fitur yang bisa ditambahkan:
- [ ] Opsi format output lainnya (TXT, JSON)
- [ ] Progress bar untuk rentang tanggal besar
- [ ] Opsi menambahkan variasi separator (-, /, .)
- [ ] Generate hanya hari kerja atau akhir pekan
- [ ] Kombinasi dengan format lain (YYYYMMDD, MMDDYYYY)
- [ ] Opsi reverse order (terbaru ke terlama)
- [ ] Multi-format dalam satu file
- [ ] Enkripsi output file

## 🤝 Kontribusi

Kontribusi dan saran pengembangan sangat diterima! Silakan fork dan submit pull request.

---

**Dibuat dengan Python 🐍 | Version 2.0 - Interactive Edition**
