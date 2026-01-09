<div align="center">

# 🐺 Captain Ginyu Script

### _Automatización inteligente para organización de archivos STL_

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-81_passing-success?style=for-the-badge&logo=pytest&logoColor=white)](.)
[![Coverage](https://img.shields.io/badge/Coverage-91%25-success?style=for-the-badge)](.)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE.md)

_Organiza automáticamente tus archivos STL dental con un solo clic._  
_Ahorra tiempo, evita errores y agiliza tu flujo de trabajo._

[Características](#-características-principales) •
[Instalación](#-instalación) •
[Uso](#-uso) •
[Arquitectura](#-arquitectura) •
[Tests](#-tests)

</div>

---

## 📖 Descripción

**Captain Ginyu Script** es una herramienta de automatización diseñada para organizar archivos STL utilizados en ortodoncia digital. El script procesa carpetas de tratamientos dentales (Subsetup1, Subsetup2, etc.) y reorganiza los archivos Maxillary y Mandibular con numeración secuencial correcta.

### 🎯 Problema que resuelve

Al trabajar con archivos STL de tratamientos ortodónticos, es común tener múltiples carpetas desordenadas con nombres complejos. Este script:

- ✅ Identifica automáticamente el orden correcto de los Subsetups
- ✅ Renombra archivos Maxilares y Mandibulares con índices secuenciales
- ✅ Maneja casos especiales como carpetas "Malocclusion"
- ✅ Evita errores humanos en procesos repetitivos

---

## ✨ Características Principales

### 🏗️ Arquitectura Profesional

- **Clean Architecture** con separación de capas (UI, Servicios, Modelos)
- **Inyección de dependencias** para código testeable
- **Type hints completos** para type safety
- **Manejo robusto de errores** con excepciones personalizadas

### ⚙️ Configuración Flexible

- Variables de entorno mediante archivo `.env`
- Patrones de archivos personalizables
- Sistema de logging configurable
- Límites de procesamiento ajustables

### 📝 Logging Profesional

- Rotación automática de archivos de log (10MB máx)
- Niveles de logging configurables (DEBUG, INFO, WARNING, ERROR)
- Logs tanto en archivo como en consola
- Historial de hasta 5 archivos de backup

### 🧪 Altamente Testeado

- **81 tests** con cobertura del 91%
- Tests parametrizados para múltiples escenarios
- Fixtures reutilizables con pytest
- Tests de casos edge y manejo de errores

### 🔄 Compatibilidad

- 100% compatible con versiones anteriores
- Funciona en Windows 10/11
- Genera ejecutable standalone (.exe)

---

## 🚀 Instalación

### Requisitos Previos

```
✓ Python 3.12+
✓ pip (gestor de paquetes)
✓ Windows OS
```

### Pasos de Instalación

1. **Clonar o descargar el repositorio**

   ```bash
   git clone https://github.com/userlg/Captain-Ginyu
   cd captain-ginyu
   ```

2. **Crear entorno virtual (recomendado)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **(Opcional) Configurar variables de entorno**
   ```bash
   copy .env.example .env
   # Editar .env con tus preferencias
   ```

---

## 💻 Uso

### Modo Script (Python)

1. **Coloca el script** en la carpeta raíz que contiene tus subcarpetas de Subsetup
2. **Ejecuta el script**

   ```bash
   python app.py
   ```

3. **El script automáticamente:**
   - 🔍 Detecta todas las carpetas Subsetup
   - 📊 Las ordena correctamente
   - 📁 Extrae archivos Maxillary y Mandibular
   - 🔢 Los renombra con índices secuenciales
   - ✅ Muestra un resumen del proceso

### Modo Ejecutable (.exe)

#### **Generar el ejecutable:**

```bash
pyinstaller --onefile --icon=favicon.ico --collect-all emoji --name ginyu app.py
```

El ejecutable se generará en la carpeta `dist/ginyu.exe`

#### **Usar el ejecutable:**

1. Copia `ginyu.exe` a la carpeta con tus archivos
2. Doble clic en `ginyu.exe`
3. ¡Listo! El proceso se ejecuta automáticamente

---

## 📁 Estructura del Proyecto

```
captain-ginyu/
│
├── 📄 app.py                    # Punto de entrada principal
├── 🎨 favicon.ico               # Icono del ejecutable
├── 📋 requirements.txt          # Dependencias Python
├── ⚙️ .env.example              # Plantilla de configuración
├── 📖 README.md                 # Este archivo
│
├── 📂 src/                      # Código fuente
│   ├── config.py                # ⚙️ Sistema de configuración
│   ├── exceptions.py            # 🛡️ Excepciones personalizadas
│   ├── logger.py                # 📝 Sistema de logging
│   ├── models.py                # 📊 Modelos de datos
│   ├── ordering.py              # 🔢 Algoritmos de ordenamiento
│   ├── phrases_list.py          # 💬 Frases aleatorias
│   ├── utils.py                 # 🔧 Utilidades generales
│   │
│   ├── 📂 services/             # Capa de lógica de negocio
│   │   ├── file_service.py      # 📁 Gestión de archivos
│   │   └── ordering_service.py  # 🔄 Servicio de ordenamiento
│   │
│   └── 📂 ui/                   # Capa de presentación
│       └── console.py           # 🖥️ Interfaz de consola
│
└── 📂 tests/                    # Suite de pruebas
    ├── conftest.py              # 🔧 Fixtures compartidas
    ├── test_utils.py            # ✅ Tests de utilidades
    ├── test_ordering.py         # ✅ Tests de ordenamiento
    ├── test_file_service.py     # ✅ Tests de servicio de archivos
    ├── test_ordering_service.py # ✅ Tests de ordenamiento
    └── test_console.py          # ✅ Tests de UI
```

---

## 🏛️ Arquitectura

El proyecto sigue los principios de **Clean Architecture**:

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

### Principios Aplicados

✅ **SRP** (Single Responsibility Principle): Cada módulo tiene una única responsabilidad  
✅ **DIP** (Dependency Inversion): Dependemos de abstracciones, no de implementaciones  
✅ **OCP** (Open/Closed): Abierto para extensión, cerrado para modificación  
✅ **Separation of Concerns**: UI, lógica de negocio y datos separados

---

## ⚙️ Configuración Avanzada

Crea un archivo `.env` en la raíz del proyecto para personalizar el comportamiento:

```env
# Patrones de archivos
MAXILLARY_PATTERN=Maxillary      # Nombre de archivos maxilares
MANDIBULAR_PATTERN=Mandibular    # Nombre de archivos mandibulares
FILE_EXTENSION=.stl              # Extensión de archivos a procesar
BACKUP_KEYWORD=backup            # Palabra clave para ignorar backups

# Patrones de carpetas
SUBSETUP_PATTERN=Subsetup        # Patrón de carpetas de subsetup
MALOCCLUSION_KEYWORD=Malocclusion # Keyword para carpeta inicial

# Límites de procesamiento
MAX_INDEX=100                    # Índice máximo a buscar

# Configuración de logging
LOG_LEVEL=INFO                   # DEBUG, INFO, WARNING, ERROR
LOG_FILE=captain_ginyu.log       # Archivo de log
LOG_MAX_BYTES=10485760          # Tamaño máximo (10MB)
LOG_BACKUP_COUNT=5              # Número de backups
```

---

## 🧪 Tests

El proyecto cuenta con una suite completa de **81 tests** con **91% de cobertura**.

### Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest -v

# Con reporte de cobertura
pytest --cov=src --cov-report=term-missing -v

# Generar reporte HTML
pytest --cov=src --cov-report=html -v

# Ver reporte en navegador
start htmlcov/index.html
```

### Estructura de Tests

| Archivo                    | Tests  | Descripción                          |
| -------------------------- | ------ | ------------------------------------ |
| `test_utils.py`            | 24     | Tests de utilidades y compatibilidad |
| `test_ordering.py`         | 10     | Tests de algoritmos de ordenamiento  |
| `test_file_service.py`     | 20     | Tests del servicio de archivos       |
| `test_ordering_service.py` | 25     | Tests del servicio de ordenamiento   |
| `test_console.py`          | 12     | Tests de la interfaz de consola      |
| **TOTAL**                  | **81** | **Cobertura: 91%**                   |

---

## 📊 Ejemplo de Uso

### Antes del Script

```
📁 Proyecto/
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

### Después del Script

```
📁 Proyecto/
├── 📁 Patient_Name_2024-01-09_Subsetup1/    (vacía)
├── 📁 Patient_Name_2024-01-09_Subsetup2/    (vacía)
├── 📁 Patient_Name_2024-01-09_Subsetup3/    (vacía)
├── Maxillary1.stl   ✨
├── Mandibular1.stl  ✨
├── Maxillary2.stl   ✨
├── Mandibular2.stl  ✨
├── Maxillary3.stl   ✨
└── Mandibular3.stl  ✨
```

---

## 🛠️ Desarrollo

### Instalar dependencias de desarrollo

```bash
pip install -r requirements.txt
pip install pytest pytest-cov
```

### Ejecutar en modo desarrollo

```bash
# Modo normal
python app.py

# Con logging detallado
# Editar .env: LOG_LEVEL=DEBUG
python app.py
```

### Generar ejecutable

```bash
pyinstaller --onefile --icon=favicon.ico --collect-all emoji --name ginyu app.py
```

El ejecutable se generará en `dist/ginyu.exe`

---

### Calidad de Código (Ruff)

El proyecto utiliza **Ruff** para linting y formateo.

```bash
# Verificar errores
ruff check .

# Corregir errores automáticamente
ruff check --fix .

# Formatear código
ruff format .
```

---

## 📈 Roadmap Futuro

- [ ] Interfaz gráfica (GUI) con Tkinter/PyQt
- [ ] Soporte para otros formatos de archivo (OBJ, PLY)
- [ ] Integración con sistemas de gestión de casos
- [ ] API REST para integración con otros sistemas
- [ ] Modo batch para procesar múltiples proyectos
- [ ] Notificaciones por email al completar
- [ ] Dashboard web de estadísticas

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir:

1. **Fork** el proyecto
2. Crea una **rama** para tu feature (`git checkout -b feature/amazing-feature`)
3. **Commit** tus cambios (`git commit -m 'Add amazing feature'`)
4. **Push** a la rama (`git push origin feature/amazing-feature`)
5. Abre un **Pull Request**

### Antes de hacer un PR:

- ✅ Asegúrate de que todos los tests pasen
- ✅ Agrega tests para nuevas funcionalidades
- ✅ Actualiza la documentación si es necesario
- ✅ Sigue el estilo de código existente

```bash
# Verificar que todo funciona
pytest --cov=src -v
```

---

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver [LICENSE.md](LICENSE.md) para más detalles.

---

## 👨‍💻 Autor

Desarrollado con ❤️ para optimizar flujos de trabajo en ortodoncia digital.

---

## 📞 Soporte

¿Problemas o preguntas?

- 📧 Email: [tu-email@ejemplo.com]
- 🐛 Issues: [GitHub Issues](../../issues)
- 📖 Documentación: Ver [walkthrough.md](docs/walkthrough.md)

---

<div align="center">

### 🌟 Si este proyecto te fue útil, ¡dale una estrella!

**Captain Ginyu Script** © 2026

</div>
