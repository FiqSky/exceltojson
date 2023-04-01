import pandas as pd
import json

# Ganti 'file_excel.xlsx' dengan nama file Excel Anda
file_excel = 'datagejaladanbotot.xlsx'

# Ganti 'Sheet1' dengan nama sheet yang berisi data Anda dalam file Excel
sheet_name = 'Sheet1'

# Membaca data dari file Excel
data = pd.read_excel(file_excel, sheet_name=sheet_name, engine='openpyxl')

# Mengonversi data ke dalam format JSON
result = data.to_dict(orient='records')

# Menyimpan hasil dalam file JSON
with open('hasil.json', 'w') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

print('Konversi Excel ke JSON berhasil!')