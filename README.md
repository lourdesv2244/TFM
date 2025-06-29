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
preprocessing:
  nlp_pipeline: "spacy"              # "spacy" o "corenlp"
  lemmatize: true

classification:
  model_path: "../models/classifier"
  threshold: 0.5

assignment:
  strategy: "load_balance"           # "load_balance", "skill_match"
  agent_metadata: "../data/agents.json"


📈 Ejemplo de flujo

    Lectura y preprocesamiento – Limpieza de texto, lematización y extracción de entidades con spaCy/CoreNLP.

    Clasificación – Transformer fine-tuned que devuelve categorías (multietiqueta si está configurado).

    Asignación – Algoritmo basado en carga de trabajo, especialidad y reglas definidas en config.yaml.

    Exportación – Generación de un archivo Excel con columnas:

        Ticket ID

        Texto original

        Categorías asignadas

        Agente sugerido

        Score de confianza

📚 Recursos adicionales

    Stanford CoreNLP – Para extracción de entidades y análisis sintáctico.

    Hugging Face Transformers – Para modelos BERT, GPT y fine-tuning.

    spaCy – Para tokenización y procesamiento rápido en Python.

🤝 Contribuciones

    Haz un fork del repositorio.

    Crea una rama con tu mejora:
    ```bash
    git checkout -b feature/nueva-caracteristica
