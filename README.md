# 🧹 Cursor AI Cleaner (Windows)

Cursor AI (Cursor Editor) dasturining **kesh (cache)** va **login/session** ma’lumotlarini tozalash uchun mo‘ljallangan **oddiy GUI dastur**.  
Tozalashdan so‘ng Cursor qayta ochilganda **login qayta so‘raladi** (amaliy sign out).

> ⚠️ Dastur Cursor’ning **rasmiy API**sidan foydalanmaydi.  
> Ma’lumotlar **local cache va storage** papkalarini o‘chirish orqali tozalanadi.

---

## ✨ Xususiyatlari

- 🧹 Cursor AI **cache** ni tozalaydi
- 🔐 Login / session ma’lumotlarini o‘chiradi (sign out)
- 🖥 Oddiy va qulay **Tkinter GUI**
- 🚀 **Portable `.exe`** ko‘rinishida ishlaydi
- ❌ Cursor dasturini o‘chirmaydi

---

## 📂 O‘chiriladigan papkalar (Windows)

Dastur quyidagi papkalarni tekshiradi va mavjud bo‘lsa o‘chiradi:

- `%APPDATA%\Cursor`
- `%LOCALAPPDATA%\Cursor`

> ℹ️ Cursor’ning o‘zi joylashgan papka (`Programs\Cursor`) **o‘chirilmaydi**.

---

## ▶️ Foydalanish

### 1️⃣ EXE orqali (tavsiya etiladi)
1. Cursor AI **yopiq** ekaniga ishonch hosil qiling
2. `cursor_cleaner.exe` ni ishga tushiring
3. **“Tozalash (Sign out)”** tugmasini bosing
4. Cursor’ni qayta oching — login so‘raladi

---

### 2️⃣ Python orqali ishga tushirish

```bash
python cursor_cleaner.py
