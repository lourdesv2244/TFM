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

2. **Crea un entorno virtual (recomendado)**
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows

3. **Instala las dependencias**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt

4. **Descarga el modelo preentrenado Copia los pesos del tokenizer y el clasificador en models/tokenizer/ y models/classifier/ respectivamente. Si usas un modelo de Hugging Face, por ejemplo BERT fine-tuned:**
   ```bash
   mkdir -p models/tokenizer models/classifier
   cd models/tokenizer
   git clone https://huggingface.co/tu-usuario/bert-tokenizer.git .
   cd ../classifier
   git clone https://huggingface.co/tu-usuario/bert-classifier.git .


---

## 🎯 Uso

python src/classify_assign.py \
  --input data/sample_tickets.xlsx \
  --output results/assigned_tickets.xlsx \
  --config src/config.yaml

--input: Ruta al archivo Excel que contiene los tickets sin procesar.
--output: Ruta donde se generará el archivo con categoría y agente asignado.
--config: Opcional, archivo YAML con parámetros de umbral, reglas de asignación y estructura de columnas.


⚙️ Configuración

El archivo src/config.yaml permite ajustar:
yaml
