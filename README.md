# 🚀 Student Registration System

A simple and easy-to-use web application built with Django to manage student registrations. Users can add, view, and manage student details with an intuitive interface.

## 📌 Features

- **Student Registration**: Allows users to register students with details such as name, email, phone, and date of birth.
- **Student List**: View all registered students along with their details.
- **Student Profile**: Access individual student profiles for detailed information.
- **Responsive UI**: Clean, simple, and mobile-friendly design using Bootstrap.
  
## 🛠 Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, Bootstrap
- **Database**: SQLite (default)

## 🚀 Getting Started

Follow the steps below to get the project up and running on your local machine:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vikasgj/Student-Registration.git
cd Student-Registration
```

### 2️⃣ Create a Virtual Environment

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

Install all the required Python packages:

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

Apply the database migrations to set up the database schema:

```bash
python manage.py migrate
```

### 5️⃣ Run the Server

Start the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to view the application.

## 📂 Project Structure

```
Student-Registration/
│
├── students/              # Django app for student management
├── templates/             # HTML templates for the frontend
├── static/                # Static files (CSS, JS)
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
```

## 👨‍💻 Usage

1. **Register a New Student**: Use the registration form to add a student.
2. **View Student List**: View a list of all registered students.
3. **View Student Profile**: Click on a student's name to see their profile details.
4. **Admin Panel**: 
   - To manage records, create an admin user by running:
     ```bash
     python manage.py createsuperuser
     ```
   - Then, log in at `http://127.0.0.1:8000/admin/` with your admin credentials.

## 📜 License

This project is open-source and free to use 😊. Feel free to modify and contribute!
