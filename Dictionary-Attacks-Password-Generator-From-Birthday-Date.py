import csv
import os
from datetime import datetime, timedelta

def generate_dates_csv():
    # Inisialisasi list untuk menyimpan tanggal
    dates_list = []
    
    # UBAH TANGGAL MULAI DAN TANGGAL AKHIR (YYYY, MM, DD)
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2003, 12, 31)
    
    # Generate semua tanggal dalam rentang
    current_date = start_date
    while current_date <= end_date:
        # Format tanggal menjadi ddmmyyyy (8 digit)
        formatted_date = current_date.strftime("%d%m%Y")
        dates_list.append([formatted_date])  # Format sebagai list untuk CSV
        current_date += timedelta(days=1)
    
    # Dapatkan path folder dimana script ini berada
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = "tanggal_2000_2003.csv"
    file_path = os.path.join(script_dir, filename)
    
    # Simpan ke file CSV di folder yang sama
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
       # writer.writerow(['Tanggal'])  # Fungsi Untuk Menambahkan Header
        writer.writerows(dates_list)
    
    print(f"File '{filename}' berhasil dibuat!")
    print(f"Lokasi file: {file_path}")
    print(f"Total {len(dates_list)} tanggal telah disimpan.")
    
    # Tampilkan beberapa contoh
    print("\nContoh 5 tanggal pertama:")
    for i in range(5):
        print(dates_list[i][0])
    
    print("\nContoh 5 tanggal terakhir:")
    for i in range(-5, 0):
        print(dates_list[i][0])

# Jalankan fungsi
if __name__ == "__main__":
    generate_dates_csv()