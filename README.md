# 📁 project_template

A simple Python project that demonstrates:

- 📦 Clean project structure with `pipenv`  
- 🧩 Modular code with packages and submodules  
- 📄 Reading/writing files (`txt`, `csv`)  
- 🧪 Unit testing with `unittest`  
- 🌐 Git and GitHub integration  

---

## 📂 Project Structure

project_template/  
├── app/  
│   └── io/  
│       ├── input.py          # Functions for reading from console, txt, and CSV  
│       └── output.py         # Functions for writing to console and file  
├── data/  
│   ├── input.txt             # Sample plain text file  
│   ├── input.csv             # Sample CSV file  
│   └── output.txt            # Output generated by main.py  
├── main.py                   # Main function to run all logic  
├── tests/  
│   └── test_io/  
│       └── test_input.py     # Unit tests for input functions  
├── Pipfile                   # pipenv dependency manager  
├── Pipfile.lock              # Lockfile for reproducible builds  
└── .gitignore                # Files/folders excluded from version control  

---

## 🚀 How to Run

### 1. Activate virtual environment and run main script
```bash
pipenv shell  
python main.py
```
This will:  
- 🧑 Ask for text input from console  
- 📖 Read from input.txt and input.csv  
- 📤 Print results to console  
- 💾 Save everything into data/output.txt  

---

## 🧪 Running Tests

Tests are written using the built-in unittest module.

To run all tests:
```bash
pipenv run python -m unittest discover
```
Or run a specific test file:
```bash
pipenv run python -m unittest tests.test_io.test_input
```
---

## 📦 Dependencies

All dependencies are managed via pipenv.

### 🔧 Install everything:
```bash
pipenv install --dev
```
### 🔍 Includes:

- pandas, numpy, matplotlib – core libraries  
- pytest, pylint, black – development tools  

---

## 🛑 .gitignore

These folders and files are excluded from version control:
```gitignore
.venv/  
__pycache__/  
*.pyc  
.idea/  
data/  
.DS_Store  
```
---

## 👤 Author

GitHub: https://github.com/kepeld

---
