# 💰 Expense Tracker (Python)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Project-Expense%20Tracker-success?style=for-the-badge" alt="Expense Tracker">
  <img src="https://img.shields.io/badge/JSON-Data%20Storage-orange?style=for-the-badge" alt="JSON">
  <img src="https://img.shields.io/badge/Beginner-Friendly-brightgreen?style=for-the-badge" alt="Beginner Friendly">
</p>

<p align="center">
A simple and efficient <strong>command-line Expense Tracker</strong> built with Python that helps users record, organize, and manage daily expenses. The application stores expense data in a JSON file, making it lightweight, portable, and easy to use.
</p>

---

## 📖 About

**Expense Tracker** is a Python-based console application developed to help users keep track of their daily spending. It provides an easy way to record expenses, categorize them, and maintain financial records using a JSON file for persistent storage.

This project demonstrates practical Python concepts such as file handling, JSON operations, input validation, loops, functions, and date handling.

---

## ✨ Features

- 💸 Add new expenses
- 📅 Record expense dates
- 🏷️ Categorize expenses
- 💰 Store expense amounts
- 📝 Add descriptions or notes
- 📂 Save data using JSON
- 🔍 View recorded expenses
- ✅ Input validation for user entries
- ⚡ Fast and lightweight command-line interface

---

## 📂 Project Structure

```text
Expense_Tracker-python/
│
├── main.py
│   └── Main entry point of the Expense Tracker application
│
├── month_expense.py
│   └── Handles monthly expense calculations and analysis
│
├── demo.json
│   └── Stores expense records in JSON format
│
├── validations/
│   ├── Date_validate.py
│   │   └── Validates expense dates
│   │
│   ├── Item_validate.py
│   │   └── Validates expense/item information
│   │
│   ├── Money_validate.py
│   │   └── Validates expense amounts
│   │
│   └── feedback_validate.py
│       └── Validates user feedback
│
└── README.md
    └── Project documentation
```

### 📌 File & Module Overview

| File / Directory       | Description                                            |
| ---------------------- | ------------------------------------------------------ |
| `main.py`              | Main program that runs the Expense Tracker             |
| `month_expense.py`     | Handles monthly expense-related operations             |
| `demo.json`            | JSON file used for persistent expense storage          |
| `validations/`         | Contains modules responsible for validating user input |
| `Date_validate.py`     | Validates date input                                   |
| `Item_validate.py`     | Validates expense/item input                           |
| `Money_validate.py`    | Validates monetary values                              |
| `feedback_validate.py` | Validates feedback input                               |
| `README.md`            | Documentation and usage instructions                   |

> **Note:** `__pycache__/` is intentionally excluded from the documented structure because Python generates it automatically when running the application. It should also generally be added to `.gitignore`.


---

## 🛠️ Technologies Used

- Python 3.x
- JSON
- Datetime Module
- File Handling

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/jillasrivardhan/Expense_Tracker-python.git
```

### 2. Navigate to the Project Folder

```bash
cd Expense_Tracker-python
```

### 3. Run the Application

```bash
python main.py
```

---

## 💻 Example Usage

```text
=========================
      Expense Tracker
=========================

Enter date (DD-MM-YYYY): 29-07-2026
What did you spend on? Food
Enter amount: 250
Enter category: Lunch

✅ Expense recorded successfully.
```

---

## 📊 Sample JSON Output

```json
[
  {
    "date": "29-07-2026",
    "category": "Food",
    "description": "Lunch",
    "amount": 250
  },
  {
    "date": "30-07-2026",
    "category": "Transport",
    "description": "Bus Ticket",
    "amount": 40
  }
]
```

---

## ⚙️ How It Works

1. The application prompts the user to enter expense details.
2. User input is validated before being processed.
3. Expense data is converted into a Python dictionary.
4. The data is appended to the existing JSON file.
5. Expenses are saved for future access and analysis.

---

## 📚 Concepts Demonstrated

- Python Dictionaries
- Lists
- Functions
- Loops
- Conditional Statements
- Exception Handling
- File Handling
- JSON Serialization
- Date Validation
- User Input Validation

---

## 🎯 Learning Outcomes

This project helps you understand how to:

- Build a real-world command-line application
- Read and write JSON files
- Validate user input
- Work with dates using Python
- Organize Python code effectively
- Store structured data persistently

---

## 🚀 Future Improvements

- 📈 Monthly and yearly expense reports
- 📊 Expense analytics with charts
- 🔍 Search and filter expenses
- ✏️ Edit existing expense records
- ❌ Delete expenses
- 💵 Budget planning
- 📤 Export data to CSV or Excel
- 🖥️ GUI version using Tkinter or CustomTkinter
- 🌐 Web version using Flask or Django
- 🗄️ Database integration with SQLite or PostgreSQL

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub. Your support motivates future improvements and helps others discover the project.

---

## 📄 License

This project is open-source and intended for educational and learning purposes.

---

## 👨‍💻 Author

**Sri Vardhan**

**Python Developer | AI Enthusiast | Data Science Learner**

Passionate about building practical Python applications, automation tools, data-driven solutions, and AI-powered projects while continuously learning modern technologies.

---

<p align="center">
  ⭐ <strong>If you enjoyed this project, don't forget to Star the repository!</strong> ⭐
</p>
