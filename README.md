# 🐺 Captain Ginyu Script

Organiza automáticamente archivos **.stl** en una estructura de carpetas definida.  
Automatiza, ordena y agiliza tu flujo de trabajo con un solo clic.

---

## 📦 Tecnologías y herramientas

![Static Badge](https://img.shields.io/badge/Python-3.12-F6D346?logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/Script-Automation-blue)
![Static Badge](https://img.shields.io/badge/Windows-Supported-00A4EF?logo=windows&logoColor=white)
![Static Badge](https://img.shields.io/badge/Tests-Pytest-0A9EDC?logo=pytest&logoColor=white)

---

## 🧩 ¿Qué hace este script?

Este proyecto permite **organizar archivos STL** dentro de una estructura predefinida de carpetas, facilitando la gestión, el orden y el acceso a tus archivos 3D.  
Ideal para flujos de trabajo de impresión 3D, modelado y proyectos CAD.

---

## ⚙️ Requisitos

- Python **3.12**
- Pip
- PyInstaller
- Pytest
- Windows OS

---

## 🚀 Uso

```bash
# Instalar dependencias
pip install -r requirements.txt

# Generar ejecutable (.exe)
pyinstaller --onefile --icon=favicon.ico app.py

# Ejecutar tests con cobertura
pytest --cov -v

# Generar reporte de cobertura en HTML
pytest --cov --cov-report=html:coverage_re
```
