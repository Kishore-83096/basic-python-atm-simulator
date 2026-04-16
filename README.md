# 🏦 Basic ATM Simulator

This is a **Basic ATM Simulator** project built with **Python**, **Tkinter** (for GUI), and **MySQL** (as the database).  
It demonstrates how a simple ATM system works, including account creation, login, and basic banking operations.

---

## 🚀 Features

### 🔑 Superuser (Admin)
- Only **one admin** exists in the system.
- Admin can **create ATM accounts** for users.
- Admin assigns a **card number** and **password** when creating accounts.

### 👤 User
Once the account is created by the admin, a user can:
- Login using **card number** and **password**.
- Check account **balance**.
- **Deposit (Credit)** money.
- **Withdraw** money.
- View **Mini Statement** (recent transactions).
- View **Bank Statement** (all transactions).

---

## 🛠️ Tech Stack
- **Python** (Core logic)
- **Tkinter** (GUI)
- **MySQL** (Database)

---

## 📂 Project Structure
```
📦 basic-python-atm-simulator
 ┣ 📜 homepage.py           # Main entry point run this page  create admin manually
 ┣ 📜 adminlog.py           # Tkinter UI code  you can login as admin you will enter adminstrator page
 ┣ 📜 administrator.py      # You can create a card holder after creating a card holder go to homepage and enter banking section you will see a login page for card holders
 ┣ 📜 Login_window.py       # you can enter the creadentials and enter atm service page
 ┣ 📜 Atmservicespage.py    # in this page you can select the services that are avaliable
 ┣ 📜 requirements.txt      # Required dependencies
 ┗ 📜 README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Kishore-83096/basic-python-atm-simulator.git
cd basic-python-atm-simulator
```

### 2️⃣ Install dependencies
Make sure you have **Python 3.x** installed.

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup MySQL Database
- Install MySQL and create a database (e.g., `atm`).
- Update database credentials in `adminlog.py , Administrator.py , Login_window.py`.
- table will be automatically create but you have to insert an admin into the administrator table use the below query as reference
```bash
- INSERT INTO administrator (Admin_id, Admin_name, Pin)VALUES ('Kishore@Admin.bank', 'Kishore', '0000');
```


- Run the SQL script to create necessary tables.

### 4️⃣ Run the project
```bash
python Homepage.py
```
