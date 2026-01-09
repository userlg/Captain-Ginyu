<div align="center">

# 🐺 Captain Ginyu Script

### _Intelligent automation for STL file organization_

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-81_passing-success?style=for-the-badge&logo=pytest&logoColor=white)](.)
[![Coverage](https://img.shields.io/badge/Coverage-91%25-success?style=for-the-badge)](.)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE.md)

_Automatically organize your dental STL files with a single click._  
_Save time, avoid errors, and streamline your workflow._

[Features](#-key-features) •
[Installation](#-installation) •
[Usage](#-usage) •
[Architecture](#-architecture) •
[Tests](#-tests)

</div>

---

## 📖 Description

**Captain Ginyu Script** is an automation tool designed to organize STL files used in digital orthodontics. The script processes dental treatment folders (Subsetup1, Subsetup2, etc.) and reorganizes Maxillary and Mandibular files with correct sequential numbering.

### 🎯 Problem It Solves

When working with orthodontic treatment STL files, it's common to have multiple disorganized folders with complex names. This script:

- ✅ Automatically identifies the correct order of Subsetups
- ✅ Renames Maxillary and Mandibular files with sequential indexes
- ✅ Handles special cases like "Malocclusion" folders
- ✅ Prevents human errors in repetitive processes

---

## ✨ Key Features

### 🏗️ Professional Architecture

- **Clean Architecture** with layer separation (UI, Services, Models)
- **Dependency injection** for testable code
- **Complete type hints** for type safety
- **Robust error handling** with custom exceptions

### ⚙️ Flexible Configuration

- Environment variables via `.env` file
- Customizable file patterns
- Configurable logging system
- Adjustable processing limits

### 📝 Professional Logging

- Automatic log file rotation (10MB max)
- Configurable logging levels (DEBUG, INFO, WARNING, ERROR)
- Logs to both file and console
- History of up to 5 backup files

### 🧪 Heavily Tested

- **81 tests** with 91% coverage
- Parametrized tests for multiple scenarios
- Reusable fixtures with pytest
- Edge case and error handling tests

### 🔄 Compatibility

- 100% backward compatible
- Works on Windows 10/11
- Generates standalone executable (.exe)

---

## 🚀 Installation

### Prerequisites

```
✓ Python 3.12+
✓ pip (package manager)
✓ Windows OS
```

### Installation Steps

1. **Clone or download the repository**

   ```bash
   git clone https://github.com/userlg/Captain-Ginyu
   cd captain-ginyu
   ```

2. **Create virtual environment (recommended)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Configure environment variables**
   ```bash
   copy .env.example .env
   # Edit .env with your preferences
   ```

---

## 💻 Usage

### Script Mode (Python)

1. **Place the script** in the root folder containing your Subsetup subfolders
2. **Run the script**

   ```bash
   python app.py
   ```

3. **The script automatically:**
   - 🔍 Detects all Subsetup folders
   - 📊 Orders them correctly
   - 📁 Extracts Maxillary and Mandibular files
   - 🔢 Renames them with sequential indexes
   - ✅ Shows a process summary

### Executable Mode (.exe)

#### **Generate the executable:**

```bash
pyinstaller --onefile --icon=favicon.ico --collect-all emoji --name ginyu app.py
```

The executable will be generated in the `dist/ginyu.exe` folder

#### **Use the executable:**

1. Copy `ginyu.exe` to the folder with your files
2. Double click on `ginyu.exe`
3. Done! The process runs automatically

---

## 📁 Project Structure

```
captain-ginyu/
│
├── 📄 app.py                    # Main entry point
├── 🎨 favicon.ico               # Executable icon
├── 📋 requirements.txt          # Python dependencies
├── ⚙️ .env.example              # Configuration template
├── 📖 README.md                 # This file
│
├── 📂 src/                      # Source code
│   ├── config.py                # ⚙️ Configuration system
│   ├── exceptions.py            # 🛡️ Custom exceptions
│   ├── logger.py                # 📝 Logging system
│   ├── models.py                # 📊 Data models
│   ├── ordering.py              # 🔢 Sorting algorithms
│   ├── phrases_list.py          # 💬 Random phrases
│   ├── utils.py                 # 🔧 General utilities
│   │
│   ├── 📂 services/             # Business logic layer
│   │   ├── file_service.py      # 📁 File management
│   │   └── ordering_service.py  # 🔄 Ordering service
│   │
│   └── 📂 ui/                   # Presentation layer
│       └── console.py           # 🖥️ Console interface
│
└── 📂 tests/                    # Test suite
    ├── conftest.py              # 🔧 Shared fixtures
    ├── test_utils.py            # ✅ Utility tests
    ├── test_ordering.py         # ✅ Sorting tests
    ├── test_file_service.py     # ✅ File service tests
    ├── test_ordering_service.py # ✅ Ordering tests
    └── test_console.py          # ✅ UI tests
```

---

## 🏛️ Architecture

The project follows **Clean Architecture** principles:

```
┌─────────────────────────────────────────────┐
│            UI Layer (console.py)            │
│  • display_welcome()                        │
│  • display_folders()                        │
│  • display_result()                         │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│       Service Layer (services/)             │
│  • file_service.py                          │
│  • ordering_service.py                      │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│      Models & Core (models.py, config.py)   │
│  • FolderInfo, FileInfo, ProcessingResult   │
│  • Config, Logger, Exceptions               │
└─────────────────────────────────────────────┘
```

### Applied Principles

✅ **SRP** (Single Responsibility Principle): Each module has a single responsibility  
✅ **DIP** (Dependency Inversion): We depend on abstractions, not implementations  
✅ **OCP** (Open/Closed): Open for extension, closed for modification  
✅ **Separation of Concerns**: UI, business logic, and data separated

---

## ⚙️ Advanced Configuration

Create a `.env` file in the project root to customize behavior:

```env
# File patterns
MAXILLARY_PATTERN=Maxillary      # Maxillary file name
MANDIBULAR_PATTERN=Mandibular    # Mandibular file name
FILE_EXTENSION=.stl              # File extension to process
BACKUP_KEYWORD=backup            # Keyword to ignore backups

# Folder patterns
SUBSETUP_PATTERN=Subsetup        # Subsetup folder pattern
MALOCCLUSION_KEYWORD=Malocclusion # Keyword for initial folder

# Processing limits
MAX_INDEX=100                    # Maximum index to search

# Logging configuration
LOG_LEVEL=INFO                   # DEBUG, INFO, WARNING, ERROR
LOG_FILE=captain_ginyu.log       # Log file
LOG_MAX_BYTES=10485760          # Max size (10MB)
LOG_BACKUP_COUNT=5              # Number of backups
```

---

## 🧪 Tests

The project has a complete test suite of **81 tests** with **91% coverage**.

### Run Tests

```bash
# Run all tests
pytest -v

# With coverage report
pytest --cov=src --cov-report=term-missing -v

# Generate HTML report
pytest --cov=src --cov-report=html -v

# View report in browser
start htmlcov/index.html
```

### Test Structure

| File                       | Tests  | Description                     |
| -------------------------- | ------ | ------------------------------- |
| `test_utils.py`            | 24     | Utility and compatibility tests |
| `test_ordering.py`         | 10     | Sorting algorithm tests         |
| `test_file_service.py`     | 20     | File service tests              |
| `test_ordering_service.py` | 25     | Ordering service tests          |
| `test_console.py`          | 12     | Console interface tests         |
| **TOTAL**                  | **81** | **Coverage: 91%**               |

---

## 📊 Usage Example

### Before the Script

```
📁 Project/
├── 📁 Patient_Name_2024-01-09_Subsetup3/
│   ├── Maxillary_complicated_name.stl
│   └── Mandibular_complicated_name.stl
├── 📁 Patient_Name_2024-01-09_Subsetup1/
│   ├── Maxillary_complicated_name.stl
│   └── Mandibular_complicated_name.stl
└── 📁 Patient_Name_2024-01-09_Subsetup2/
    ├── Maxillary_complicated_name.stl
    └── Mandibular_complicated_name.stl
```

### After the Script

```
📁 Project/
├── 📁 Patient_Name_2024-01-09_Subsetup1/    (empty)
├── 📁 Patient_Name_2024-01-09_Subsetup2/    (empty)
├── 📁 Patient_Name_2024-01-09_Subsetup3/    (empty)
├── Maxillary1.stl   ✨
├── Mandibular1.stl  ✨
├── Maxillary2.stl   ✨
├── Mandibular2.stl  ✨
├── Maxillary3.stl   ✨
└── Mandibular3.stl  ✨
```

---

## 🛠️ Development

### Install development dependencies

```bash
pip install -r requirements.txt
pip install pytest pytest-cov
```

### Run in development mode

```bash
# Normal mode
python app.py

# With detailed logging
# Edit .env: LOG_LEVEL=DEBUG
python app.py
```

### Generate executable

```bash
pyinstaller --onefile --icon=favicon.ico --collect-all emoji --name ginyu app.py
```

The executable will be generated in `dist/ginyu.exe`

---

### Code Quality (Ruff)

The project uses **Ruff** for linting and formatting.

```bash
# Check for errors
ruff check .

# Fix errors automatically
ruff check --fix .

# Format code
ruff format .
```

---

## 📈 Future Roadmap

- [ ] Graphical User Interface (GUI) with Tkinter/PyQt
- [ ] Support for other file formats (OBJ, PLY)
- [ ] Integration with case management systems
- [ ] REST API for integration with other systems
- [ ] Batch mode to process multiple projects
- [ ] Email notifications on completion
- [ ] Web dashboard for statistics

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. **Fork** the project
2. Create a **branch** for your feature (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. Open a **Pull Request**

### Before making a PR:

- ✅ Make sure all tests pass
- ✅ Add tests for new features
- ✅ Update documentation if necessary
- ✅ Follow the existing code style

```bash
# Verify everything works
pytest --cov=src -v
```

---

## 📝 License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for more details.

---

## 👨‍💻 Author

Developed with ❤️ to optimize workflows in digital orthodontics.

---

## 📞 Support

Problems or questions?

- 📧 Email: [your-email@example.com]
- 🐛 Issues: [GitHub Issues](../../issues)
- 📖 Documentation: See [walkthrough.md](docs/walkthrough.md)

---

<div align="center">

### 🌟 If this project was useful to you, give it a star!

**Captain Ginyu Script** © 2026

</div>
