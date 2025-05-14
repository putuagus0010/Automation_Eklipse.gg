# 🔍 Automation Testing - Eklipse.gg

Project ini merupakan automation script menggunakan **Python + Selenium + pytest** untuk menguji fitur **Login dan Registrasi** pada website [Eklipse.gg](https://eklipse.gg).

## Struktur Folder

```
Automation_Eklipse.gg/
├── Register - Login/
│   └── Reg_1.py
├── requirements.txt
└── README.md
```

## 🚀 Cara Menjalankan Project

### 1. Clone Repository

```bash
git clone https://github.com/putuagus0010/Automation_Eklipse.gg.git
cd Automation_Eklipse.gg
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)

```bash
python -m venv venv
source venv/bin/activate      # Untuk Linux/Mac
venv\Scripts\activate         # Untuk Windows
```

### 3. Install Library yang Dibutuhkan

```bash
pip install -r requirements.txt
```

### 4. Jalankan Automation Test

Masuk ke folder `Register - Login` dan jalankan script:

```bash
cd "Register - Login"
pytest Reg_1.py
```

Atau bisa juga langsung:

```bash
python "Register - Login/Reg_1.py"
```

> 💡 Disarankan menggunakan `pytest` untuk hasil laporan yang lebih rapi.

---

## 🧪 Teknologi yang Digunakan

- Python 3.x
- Selenium WebDriver
- Pytest

## 📌 Catatan

- Pastikan browser (misal: Chrome) dan **driver-nya (chromedriver)** sudah ter-install dan sesuai versi.
- Untuk testing website live, pastikan koneksi internet aktif.
- Bila terjadi error path, pastikan penulisan folder sesuai OS (Windows/Linux).

---

## 🙋 Tentang Saya

I Putu Agus Adi Artha Saputra  
Quality Assurance Engineer | Manual & Automation Tester  
📫 [LinkedIn](https://www.linkedin.com/in/agusadi/)
