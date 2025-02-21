# 🚀 Student Registration System

A web application built with *Django* to manage student registrations. Users can add, view, and manage student details easily.

## 📌 Features
- Student registration with fields like name, email, phone, and date of birth.  
- List all registered students with their details.  
- View individual student profiles.  
- Simple and responsive UI using Bootstrap.  

## 🛠 Technologies Used
- *Backend:* Django, Python  
- *Frontend:* HTML, Bootstrap  
- *Database:* SQLite (default)  

## 🚀 Getting Started

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/vikasgj/Student-Registration.git
cd Student-Registration

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Apply Migrations

python manage.py migrate

5️⃣ Run the Server

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.

📂 Project Structure

Student-Registration/
│-- students/              # Django app for student management
│-- templates/             # HTML templates
│-- static/                # Static files (CSS, JS)
│-- db.sqlite3             # SQLite database
│-- manage.py              # Django management script

👨‍💻 Usage

1. Register a new student using the registration form.


2. View the student list and click on a name to see details.


3. Access the Django admin panel to manage records:

python manage.py createsuperuser

Then log in at http://127.0.0.1:8000/admin/.


📜 License

This project is open-source and Free to Use 😊.
