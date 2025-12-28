import pytesseract
from PIL import Image, ImageOps
import os

img_path = "images/english_handwritten.png"

# 1️⃣ Cek apakah file ada
if not os.path.exists(img_path):
    print("File tidak ditemukan:", img_path)
    exit()

print("File ditemukan:", img_path)

# 2️⃣ Buka gambar, konversi grayscale
try:
    img = Image.open(img_path).convert("L")
    print("Gambar berhasil dibuka, ukuran:", img.size)
except Exception as e:
    print("Gagal membuka gambar:", e)
    exit()

# 3️⃣ Invert dan enhance (agar Tesseract lebih mudah membaca)
img = ImageOps.invert(img)
img = ImageOps.autocontrast(img)

# 4️⃣ Jalankan OCR
try:
    text = pytesseract.image_to_string(img, lang="eng", config="--psm 7")
    print("\nOCR English Result:")
    print("--------------------")
    print(repr(text.strip()))  # pakai repr() supaya terlihat jika kosong
except Exception as e:
    print("Gagal menjalankan OCR:", e)
