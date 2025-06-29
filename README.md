# TFM
# Ticket Classification & Assignment MVP

# Resumen
El presente Trabajo de Fin de Máster (TFM) tiene como objetivo entregar un Producto Mínimo Viable (MVP) que consiste en un prototipo inicial para la clasificación y asignación automática de tickets técnicos en el equipo de soporte de Data & Analytics MAZ. Esta propuesta responde a la creciente demanda de soluciones operativas que permitan gestionar de manera eficiente el volumen de solicitudes recibidas, caracterizadas por un alto grado de complejidad técnica y una nomenclatura específica del dominio, lo que exige una clasificación precisa y una asignación óptima a agentes especializados.

La metodología se basó en la combinación de técnicas de aprendizaje automático supervisado y procesamiento del lenguaje natural. Inicialmente, se realizó una recolección y etiquetado manual de 500 tickets reales, distribuidos en seis categorías definidas por expertos. Posteriormente, se implementó un preprocesamiento lingüístico especializado, con normalización, lematización y conservación de términos técnicos clave. Se probaron diversos algoritmos tradicionales (Random Forest, SVM, Gradient Boosting), así como una red neuronal profunda y un modelo BERT ajustado mediante fine-tuning. A partir de este último se desarrolló BERT con tokens, una versión optimizada que incorpora tokens especiales, capa de atención personalizada y generación de explicaciones automáticas.

Los resultados muestran que BERT con tokens alcanza una precisión del 92,1 % en clasificación técnica, mejorando en más de 5 puntos porcentuales respecto a BERT estándar (86,7 %) y acercándose al rendimiento de los modelos tradicionales más precisos (93,4 %), con la ventaja añadida de ofrecer explicaciones interpretables sobre cada decisión. Finalmente, el sistema se integró en un flujo automatizado que no solo clasifica el ticket, sino que asigna dinámicamente al agente óptimo en función de su especialidad y carga de trabajo. Se concluye que la arquitectura propuesta representa una solución robusta, explicable y lista para su incorporación al proceso de soporte técnico de D&A.

Keywords: Aprendizaje automático supervisado, Procesamiento del lenguaje natural (PLN), Red neuronal profunda, BERT, Fine-tuning, BERT con tokens, Tokens especiales, Clasificación y asignación automática, Modelos tradicionales (Random Forest, SVM, Gradient Boosting). Producto Mínimo Viable (MVP), Prototipo inicial, Recolección de tickets reales, Etiquetado manual, Preprocesamiento lingüístico, Normalización, Lematización.

Este repositorio contiene el **Producto Mínimo Viable (MVP)** de una herramienta automática para la clasificación y asignación de tickets técnicos, desarrollada en Python y diseñada para integrarse fácilmente con flujos basados en Excel o plataformas como ServiceNow.



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



## 🎯 Uso
python src/classify_assign.py \
  --input data/sample_tickets.xlsx \
  --output results/assigned_tickets.xlsx \
  --config src/config.yaml

  ```bash
   mkdir -p models/tokenizer models/classifier
   cd models/tokenizer
   git clone https://huggingface.co/tu-usuario/bert-tokenizer.git .
   cd ../classifier
   git clone https://huggingface.co/tu-usuario/bert-classifier.git .
   python src/classify_assign.py \
        --input data/sample_tickets.xlsx \
        --output results/assigned_tickets.xlsx \
        --config src/config.yaml


* --input: Ruta al archivo Excel que contiene los tickets sin procesar.
* --output: Ruta donde se generará el archivo con categoría y agente asignado.
* --config: Opcional, archivo YAML con parámetros de umbral, reglas de asignación y estructura de columnas.



⚙️ Configuración

El archivo src/config.yaml permite ajustar:

 ```bash
 preprocessing:
    nlp_pipeline: "spacy"    # "spacy" o "corenlp"
    lemmatize: true

 classification:
    model_path: "../models/classifier"
    threshold: 0.5
   
 assignment:
    strategy: "load_balance"  # "load_balance", "skill_match"
    agent_metadata: "../data/agents.json"


📈 Ejemplo de flujo

   1. Lectura y preprocesamiento – Limpieza de texto, lematización y extracción de entidades con spaCy/CoreNLP.
   2. Clasificación – Transformer fine-tuned que devuelve categorías (multietiqueta si está configurado).
   3. Asignación – Algoritmo basado en carga de trabajo, especialidad y reglas definidas en config.yaml.
   4. Exportación – Generación de un archivo Excel con columnas:
       * Ticket ID
       * Texto original
       * Categorías asignadas
       * Agente sugerido

     

📚 Recursos adicionales

   * Stanford CoreNLP – Para extracción de entidades y análisis sintáctico.
   * Hugging Face Transformers – Para modelos BERT, GPT y fine-tuning.
   * spaCy – Para tokenización y procesamiento rápido en Python.

     

🤝 Contribuciones
1. **Haz un fork del repositorio**
2. **Crea una rama con tu mejora:**
   ```bash
   git checkout -b feature/nueva-caracteristica
3. **Haz tus commits:**
   ```bash
   git commit -m "Añade X funcionalidad"
4. **Envía un pull request.**


   
📄 Licencia
Este proyecto está bajo la licencia MIT. 
