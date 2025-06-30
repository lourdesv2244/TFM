from src.model_utils import load_model_system

# Carga el modelo completo, el tokenizer y el codificador de etiquetas
bert2, tokenizer, label_encoder = load_model_system()

# Verificación del estado
print("MODELO CARGADO CORRECTAMENTE")
print("-" * 50)
print(f"Tokenizer cargado con vocabulario de tamaño: {len(tokenizer)}")
print(f"LabelEncoder con {len(label_encoder.classes_)} clases:")
print("    →", list(label_encoder.classes_))
print("-" * 50)
print("El modelo está en modo evaluación:", not bert2.training)
