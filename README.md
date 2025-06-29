# TFM
# Ticket Classification & Assignment MVP

Este repositorio contiene el **Producto Mínimo Viable (MVP)** de una herramienta automática para la clasificación y asignación de tickets técnicos, desarrollada en Python y diseñada para integrarse fácilmente con flujos basados en Excel o plataformas como ServiceNow.

---

## 📂 Estructura del repositorio
.
├── data/
│   └── sample_tickets.xlsx         # Ejemplo de archivo de entrada
├── models/
│   └── tokenizer/                  # Tokenizer de Transformer (p. ej. BERT)
│   └── classifier/                 # Pesos del modelo de clasificación
├── src/
│   ├── classify_assign.py          # Script principal de clasificación y asignación
│   ├── preprocessing.py            # Módulo de preprocesamiento (CoreNLP + spaCy)
│   ├── model.py                    # Definición del pipeline de Transformer
│   └── utils.py                    # Funciones auxiliares (I/O, Excel, configuración)
├── notebooks/
│   └── exploration.ipynb           # Análisis exploratorio y pruebas interactivas
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Documentación principal


---

## 🚀 Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/ticket-mvp.git
   cd ticket-mvp
