import csv
import os
from datetime import datetime, timedelta

def generate_dates_csv():
    # Inisialisasi list untuk menyimpan tanggal
    dates_list = []
    
    # INPUT TANGGAL MULAI DAN TANGGAL AKHIR
    print("=" * 50)
    print("GENERATOR DAFTAR PASSWORD TANGGAL")
    print("=" * 50)
    
    while True:
        try:
            print("\nMasukkan TANGGAL MULAI (format: DD/MM/YYYY)")
            start_input = input("Contoh: 01/01/2000 : ")
            start_date = datetime.strptime(start_input, "%d/%m/%Y")
            break
        except ValueError:
            print("❌ Format salah! Gunakan format DD/MM/YYYY (contoh: 01/01/2000)")
    
    while True:
        try:
            print("\nMasukkan TANGGAL SELESAI (format: DD/MM/YYYY)")
            end_input = input("Contoh: 31/12/2003 : ")
            end_date = datetime.strptime(end_input, "%d/%m/%Y")
            
            if end_date < start_date:
                print("❌ Tanggal selesai tidak boleh lebih awal dari tanggal mulai!")
                continue
            break
        except ValueError:
            print("❌ Format salah! Gunakan format DD/MM/YYYY (contoh: 31/12/2003)")
    
    print(f"\n✓ Memproses tanggal dari {start_date.strftime('%d/%m/%Y')} hingga {end_date.strftime('%d/%m/%Y')}...")
    
    # Generate semua tanggal dalam rentang
    current_date = start_date
    while current_date <= end_date:
        # Format tanggal menjadi ddmmyyyy (8 digit)
        formatted_date = current_date.strftime("%d%m%Y")
        dates_list.append([formatted_date])  # Format sebagai list untuk CSV
        current_date += timedelta(days=1)
    
    # Dapatkan path folder dimana script ini berada
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Buat nama file dinamis berdasarkan rentang tanggal
    start_year = start_date.strftime("%Y")
    end_year = end_date.strftime("%Y")
    filename = f"tanggal_{start_year}_{end_year}.csv"
    file_path = os.path.join(script_dir, filename)
    
    # Simpan ke file CSV di folder yang sama
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
       # writer.writerow(['Tanggal'])  # Fungsi Untuk Menambahkan Header
        writer.writerows(dates_list)
    
    print("\n" + "=" * 50)
    print(f"✓ File '{filename}' berhasil dibuat!")
    print(f"✓ Lokasi file: {file_path}")
    print(f"✓ Total {len(dates_list)} tanggal telah disimpan.")
    print("=" * 50)
    
    # Tampilkan beberapa contoh
    print("\nContoh 5 tanggal pertama:")
    for i in range(min(5, len(dates_list))):
        print(f"  {dates_list[i][0]}")
    
    if len(dates_list) > 5:
        print("\nContoh 5 tanggal terakhir:")
        for i in range(-5, 0):
            print(f"  {dates_list[i][0]}")

# Jalankan fungsi
if __name__ == "__main__":
    generate_dates_csv()
# ```

# **Perubahan yang dilakukan:**

# 1. ✅ Format input berubah dari `YYYY/MM/DD` menjadi `DD/MM/YYYY`
# 2. ✅ Parser datetime diubah dari `"%Y/%m/%d"` menjadi `"%d/%m/%Y"`
# 3. ✅ Contoh input diperbarui menjadi `01/01/2000` dan `31/12/2003`
# 4. ✅ Pesan error juga diperbarui dengan format yang baru

# **Contoh penggunaan sekarang:**
# ```
# Masukkan TANGGAL MULAI (format: DD/MM/YYYY)
# Contoh: 01/01/2000 : 01/01/2020

# Masukkan TANGGAL SELESAI (format: DD/MM/YYYY)
# Contoh: 31/12/2003 : 31/12/2020
