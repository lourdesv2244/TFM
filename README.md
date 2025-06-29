![imagen](https://github.com/user-attachments/assets/725e914e-8f9f-41bb-af7d-c9e8c92e83a8)


# TFM: Clasificación automática de tickets de solicitudes en área de Operaciones D&A
Sistema de clasificación y asignación automática de tickets en ServiceNow para el área de Data & Analytics de MAZ. Este sistema se desarrolló en el marco del Trabajo de Fin de Máster en Ciencia de Datos e Inteligencia Artificial (curso 2024-2025)

# Resumen
El presente Trabajo de Fin de Máster (TFM) tiene como objetivo entregar un Producto Mínimo Viable (MVP) que consiste en un prototipo inicial para la clasificación y asignación automática de tickets técnicos en el equipo de soporte de Data & Analytics MAZ. Esta propuesta responde a la creciente demanda de soluciones operativas que permitan gestionar de manera eficiente el volumen de solicitudes recibidas, caracterizadas por un alto grado de complejidad técnica y una nomenclatura específica del dominio, lo que exige una clasificación precisa y una asignación óptima a agentes especializados.

La metodología se basó en la combinación de técnicas de aprendizaje automático supervisado y procesamiento del lenguaje natural. Inicialmente, se realizó una recolección y etiquetado manual de 500 tickets reales, distribuidos en seis categorías definidas por expertos. Posteriormente, se implementó un preprocesamiento lingüístico especializado, con normalización, lematización y conservación de términos técnicos clave. Se probaron diversos algoritmos tradicionales (Random Forest, SVM, Gradient Boosting), así como una red neuronal profunda y un modelo BERT ajustado mediante fine-tuning. A partir de este último se desarrolló BERT con tokens, una versión optimizada que incorpora tokens especiales, capa de atención personalizada y generación de explicaciones automáticas.

Los resultados muestran que BERT con tokens alcanza una precisión del 92,1 % en clasificación técnica, mejorando en más de 5 puntos porcentuales respecto a BERT estándar (86,7 %) y acercándose al rendimiento de los modelos tradicionales más precisos (93,4 %), con la ventaja añadida de ofrecer explicaciones interpretables sobre cada decisión. Finalmente, el sistema se integró en un flujo automatizado que no solo clasifica el ticket, sino que asigna dinámicamente al agente óptimo en función de su especialidad y carga de trabajo. Se concluye que la arquitectura propuesta representa una solución robusta, explicable y lista para su incorporación al proceso de soporte técnico de D&A.

Keywords: Aprendizaje automático supervisado, Procesamiento del lenguaje natural (PLN), Red neuronal profunda, BERT, Fine-tuning, BERT con tokens, Tokens especiales, Clasificación y asignación automática, Modelos tradicionales (Random Forest, SVM, Gradient Boosting). Producto Mínimo Viable (MVP), Prototipo inicial, Recolección de tickets reales, Etiquetado manual, Preprocesamiento lingüístico, Normalización, Lematización.

Este repositorio contiene el **Producto Mínimo Viable (MVP)** de una herramienta automática para la clasificación y asignación de tickets técnicos, desarrollada en Python y diseñada para integrarse fácilmente con flujos basados en Excel.


# 📂 Estructura del repositorio
La estructura de carpetas con la documentación de Github es la presentada a continuación:

        01 Documentación Github
         └── 00_Codigo
             ├── DOCUMENTACIÓN GITHUB.docx
             ├── ejemplo (1).py
             ├── Modelo_binario_ (1) (1).ipynb
             ├── obtener_caracteristicas (1).py
             └── Recursos-20231027T110710Z-001 (1).zip

Se detalla a continuación el contenido de cada fichero:

- DOCUMENTACIÓN GITHUB.docx:
- DOS


# 📈 Ejemplo de flujo

   1. Lectura y preprocesamiento – Limpieza de texto, lematización y extracción de entidades con spaCy/CoreNLP.
   2. Clasificación – Transformer fine-tuned que devuelve categorías (multietiqueta si está configurado).
   3. Asignación – Algoritmo basado en carga de trabajo, especialidad y reglas definidas en config.yaml.
   4. Exportación – Generación de un archivo Excel 
       * Ticket ID
       * Texto original
       * Categorías asignadas
       * Agente sugerido



# 📚 Recursos adicionales

   * Stanford CoreNLP – Para extracción de entidades y análisis sintáctico.
   * Hugging Face Transformers – Para modelos BERT, GPT y fine-tuning.
   * spaCy – Para tokenización y procesamiento rápido en Python.

