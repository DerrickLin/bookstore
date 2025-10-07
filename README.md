修正內容
# Bookstore / 圖書管理系統

這是一個以 Django 為框架、結合前後端技術的圖書管理系統（Bookstore / Library Management System）。  
可以用來管理書籍、讀者、借閱記錄等。
- [Demo影片連結](https://drive.google.com/file/d/1ZlGdQ_HcI8s69R3dgvp2nMGoTbS5NpS1/view?usp=drive_link)
---

## 主要功能

- 書籍的 **新增 / 刪除 / 編輯 / 查詢**  
- 讀者 / 借閱人管理  
- 借閱記錄：借書、還書、逾期管理  
- 支援查詢篩選功能  
- 在操作成功或失敗時顯示提示訊息（前端 UI 提示）  
- 使用 jQuery 增強前端互動性  
- 網頁版前端 UI (HTML / CSS / JavaScript)  
- Django Forms 處理表單驗證、資料處理  

---

## 專案架構（範例）

```
bookstore/
├── BookMaintenanceSystem/        ← Django 專案目錄
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── …  
├── templates/                    ← 前端 HTML 模板們
├── static/                       ← CSS / JS / 圖片等靜態資源
├── requirements.txt              ← 專案相依套件
├── .gitignore
└── README.md
```

---

## 安裝與啟動指南

使用 Python 及虛擬環境：

```bash
# 1. Clone 這個 repo
git clone https://github.com/DerrickLin/bookstore.git
cd bookstore

# 2. 建立虛擬環境
python3 -m venv venv
source venv/bin/activate   # 在 Windows 上用 venv\Scripts\activate

# 3. 安裝套件
pip install -r requirements.txt

# 4. 執行資料庫遷移
python manage.py makemigrations
python manage.py migrate

# 5. 建立 superuser（管理帳戶，可登入 Django admin）
python manage.py createsuperuser

# 6. 啟動伺服器
python manage.py runserver
```

啟動後，可以在瀏覽器打開 `http://127.0.0.1:8000/` （或 `http://localhost:8000/`）查看系統。

---


## Tech Stack

| 類別 | 技術 / 工具 |
|------|----------------|
| 後端 | Python, Django |
| 表單 / 驗證 | Django Forms |
| 前端 | HTML, CSS, JavaScript, jQuery |
| 資料庫 | SQLite |
| 相依套件 | 在 `requirements.txt` 中 |

---



