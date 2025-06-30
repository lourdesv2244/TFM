![imagen](https://github.com/user-attachments/assets/725e914e-8f9f-41bb-af7d-c9e8c92e83a8)


# TFM: Clasificación automática de tickets de solicitudes en área de Operaciones D&A
Sistema de clasificación y asignación automática de tickets recibidos en ServiceNow y extraidos de forma manual para ser atendidos por el equipo de Operaciones del área de Data & Analytics MAZ. Este sistema se desarrolló en el marco del Trabajo de Fin de Máster en Ciencia de Datos e Inteligencia Artificial (curso 2024-2025)

# Resumen
El presente Trabajo de Fin de Máster (TFM) tiene como objetivo entregar un Producto Mínimo Viable (MVP) que consiste en un prototipo inicial para la clasificación y asignación automática de tickets técnicos en el equipo de soporte de Data & Analytics MAZ. Esta propuesta responde a la creciente demanda de soluciones operativas que permitan gestionar de manera eficiente el volumen de solicitudes recibidas, caracterizadas por un alto grado de complejidad técnica y una nomenclatura específica del dominio, lo que exige una clasificación precisa y una asignación óptima a agentes especializados.

La metodología se basó en la combinación de técnicas de aprendizaje automático supervisado y procesamiento del lenguaje natural. Inicialmente, se realizó una recolección y etiquetado manual de 500 tickets reales, distribuidos en seis categorías definidas por expertos. Posteriormente, se implementó un preprocesamiento lingüístico especializado, con normalización, lematización y conservación de términos técnicos clave. Se probaron diversos algoritmos tradicionales (Random Forest, SVM, Gradient Boosting), así como una red neuronal profunda y un modelo BERT ajustado mediante fine-tuning. A partir de este último se desarrolló BERT con tokens, una versión optimizada que incorpora tokens especiales, capa de atención personalizada y generación de explicaciones automáticas.

Los resultados muestran que BERT con tokens alcanza una precisión del 92,1 % en clasificación técnica, mejorando en más de 5 puntos porcentuales respecto a BERT estándar (86,7 %) y acercándose al rendimiento de los modelos tradicionales más precisos (93,4 %), con la ventaja añadida de ofrecer explicaciones interpretables sobre cada decisión. Finalmente, el sistema se integró en un flujo automatizado que no solo clasifica el ticket, sino que asigna dinámicamente al agente óptimo en función de su especialidad y carga de trabajo. Se concluye que la arquitectura propuesta representa una solución robusta, explicable y lista para su incorporación al proceso de soporte técnico de D&A.

Keywords: Aprendizaje automático supervisado, Procesamiento del lenguaje natural (PLN), Red neuronal profunda, BERT, Fine-tuning, BERT con tokens, Tokens especiales, Clasificación y asignación automática, Modelos tradicionales (Random Forest, SVM, Gradient Boosting). Producto Mínimo Viable (MVP), Prototipo inicial, Recolección de tickets reales, Etiquetado manual, Preprocesamiento lingüístico, Normalización, Lematización.

Este repositorio contiene el **Producto Mínimo Viable (MVP)** de una herramienta automática para la clasificación y asignación de tickets técnicos, desarrollada en Python y diseñada para integrarse fácilmente con flujos basados en Excel.


# 📂 Estructura del repositorio
La estructura de carpetas con la documentación de Github es la presentada a continuación:

        01 Documentación Github
         └── data
             ├── Mensajes_Clasificados_Manual.xlsx
             ├── data_entrada.xlsx
             └── resultado_BERT_tokens.xlsx
         └── Instalacion
             ├── check_system.py
             └── modelo_bert_tokens
                 ├── added_tokens.json
                 ├── bert2_weights.pt
                 ├── label_encoder.pkl
                 ├── special_tokens_map.json
                 └── vocab.txt
         └── codigo
             └── Clasificacion Mensajes v2.ipynb
                 
               

Se detalla a continuación el contenido de cada fichero:

- added_tokens.json: Contiene el mapeo de los tokens personalizados que se han añadido al vocabulario original de BERT. Cada clave es el nuevo token (p. ej. nombres de herramientas o acrónimos del dominio) y su valor es el índice (entero) que ocupa dentro de la nueva tabla de vocabulario. Se usa en el BertTokenizer para que reconozca y trate correctamente estos tokens durante la tokenización.
- special_tokens_map.json: Define el conjunto de “tokens especiales” (por ejemplo [CLS], [SEP], [PAD], [UNK], etc.) y, opcionalmente, otros tokens propios ([AADS], [DELTA],…) que se consideraron relevantes. Mapea cada tipo de token especial a la cadena que lo representa, de modo que el tokenizer sepa insertarlos o sustituirlos de forma coherente en el texto de entrada.
- bert2_weights.pt: Contiene el state_dict completo del modelo BertForSequenceClassification tras el proceso de fine-tuning. Incluye los pesos de todas las capas Transformer, la capa de clasificación y cualquier módulo añadido (p. ej. capa de atención extra). Se carga con model.load_state_dict(torch.load("bert2_weights.pt")) para restaurar el modelo en memoria.
- VOCAB.TXT: Lista el vocabulario completo que utiliza el tokenizer: empieza con los tokens originales de bert-base-uncased y, a continuación, incorpora en las últimas líneas los tokens introducidos (los mismos que se reflejan en added_tokens.json). El orden y la posición de cada línea corresponden al índice que el tokenizer asigna en los tensores de entrada.
- label_encoder.pkl: Almacena el objeto LabelEncoder de scikit-learn que traduce las categorías de texto (p. ej. "AADS Group - Acceso", "Delta Share") a sus códigos numéricos internos (0, 1, …). • Se recupera con label_encoder = pickle.load(open("label_encoder.pkl","rb")) para decodificar las predicciones numéricas del modelo de vuelta a su nombre de categoría original.


# 📈 Ejemplo de flujo

   1. Lectura y preprocesamiento – Limpieza de texto, lematización y extracción de entidades con spaCy/CoreNLP.
   2. Clasificación – Transformer fine-tuned que devuelve categorías (multietiqueta si está configurado).
   3. Asignación – Algoritmo basado en carga de trabajo, especialidad y reglas definidas en config.yaml.
   4. Exportación – Generación de un archivo Excel 


# 📚 Recursos adicionales

   * Stanford CoreNLP – Para extracción de entidades y análisis sintáctico.
   * Hugging Face Transformers – Para modelos BERT, GPT y fine-tuning.
   * spaCy – Para tokenización y procesamiento rápido en Python.


# 🔧 Instalación
## Paso a Paso: Cargar y Verificar el Modelo

A continuación se describe cómo cargar el sistema de clasificación y comprobar que todo está listo para realizar predicciones.

### 1. Clona el repositorio  

        git clone https://github.com/tu-usuario/ticket-mvp.git
        cd ticket-mvp

### 2. Crea y activa un entorno virtual  

        python3 -m venv venv
        source venv/bin/activate       # macOS / Linux
        venv\Scripts\activate          # Windows

### 3. Instala las dependencias  

        pip install -r requirements.txt

### 4. Carga el modelo y muestra el estado del sistema
Abre un intérprete de Python o crea un script (check_system.py) con el siguiente contenido:  

        pip install -r Requirements.txt

### 5. Carga el modelo y muestra el estado del sistema 
        
        python check_system.py


### 6.  Interpreta la salida

- Tokenizer cargado…: número de tokens en el vocabulario.
- LabelEncoder…: lista de categorías que reconoce el modelo.
- Modo evaluación: True indica que el modelo está listo para predecir (sin activar gradientes).

# 👤 Autor
Lourdes Villafaña

  

