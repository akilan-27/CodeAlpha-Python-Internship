# 📧 Email Extractor Automation Script

A Python-based automation tool that extracts email addresses from text files using Regular Expressions (Regex) and stores them in a separate output file. This project demonstrates the practical application of text processing, pattern matching, and file handling in Python.

---

## 🚀 Features

* Extracts valid email addresses from text files
* Uses Regular Expressions (Regex) for pattern matching
* Reads data from an input file automatically
* Saves extracted emails to a separate output file
* Displays extracted emails in the console
* Simple and lightweight automation solution

---

## 🛠️ Technologies Used

* Python 3
* Regular Expressions (`re` module)
* File Handling
* Text Processing

---

## 📂 Project Structure

```text
CodeAlpha_EmailExtractor/
│
├── email_extractor.py
├── input.txt
├── extracted_emails.txt
└── README.md
```

---

## ⚙️ How It Works

1. The program reads the contents of a text file.
2. A Regular Expression pattern is used to identify email addresses.
3. All matching emails are extracted and stored.
4. The extracted emails are displayed in the terminal.
5. Results are saved to an output file for future use.

---

## 📋 Example Input

Contents of `input.txt`:

```text
Hello,

For support, contact support@gmail.com

For HR queries:
hr@company.org

For sales:
sales@yahoo.com
```

---

## 📤 Example Output

Terminal Output:

```text
Extracted Emails:

support@gmail.com
hr@company.org
sales@yahoo.com

Emails saved successfully!
```

Contents of `extracted_emails.txt`:

```text
support@gmail.com
hr@company.org
sales@yahoo.com
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/yourusername/CodeAlpha_EmailExtractor.git
```

### Navigate to Project Directory

```bash
cd CodeAlpha_EmailExtractor
```

### Run the Script

```bash
python email_extractor.py
```

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Regular Expressions (Regex)
* Pattern Matching
* File Handling in Python
* Text Processing
* Automation Scripting
* Data Extraction Techniques

---

## 🔮 Future Enhancements

* Extract phone numbers and URLs
* Export results to CSV or Excel
* Build a graphical user interface (GUI) using Tkinter
* Support multiple input file formats
* Add duplicate email detection and removal

---

## 💼 Internship Project

This project was developed as part of the **CodeAlpha Python Programming Internship** to demonstrate automation and data extraction techniques using Python.

---

## 👨‍💻 Author

**Your Name**

Python Programming Intern – CodeAlpha

GitHub: https://github.com/akilan-27/
