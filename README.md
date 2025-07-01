# test-hemis Telegram Bot

Bu bot foydalanuvchidan `.txt`, `.docx`, yoki `.json` test faylini qabul qiladi va testni interaktiv tarzda o'tkazadi.

## Ishga tushirish

### 1. Kutubxonalarni o'rnating

```bash
pip install -r requirements.txt
```

### 2. Bot tokenni o'zgartiring
`main.py` faylidagi `TOKEN` ni o'zgartiring yoki `BOT_TOKEN` atrof-muhit o'zgaruvchisi sifatida belgilang.

### 3. Ishga tushurish

```bash
python main.py
```

### 4. Render uchun

`start.sh`, `Procfile` mavjud. Render.com’da Background Worker sifatida deploy qiling.
