import re

# Ruta del archivo de chat exportado
file_path = "chat.txt"

# Criterios para filtrar información específica
keywords = ["laboral", "trabajo"]  # Cambiar por las palabras o frases que buscas

# Leer el archivo
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Procesar las líneas
filtered_messages = []
for line in lines:
    # Ajustar al nuevo formato: dd/m/yyyy, hh:mm - Usuario:
    if re.match(r"^\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2} - .+?:", line):
        # Filtrar por palabras clave
        if any(keyword.lower() in line.lower() for keyword in keywords):
            filtered_messages.append(line)

# Guardar los mensajes filtrados en un nuevo archivo
output_file = "filtered_chat.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(filtered_messages)

print(f"Mensajes filtrados guardados en {output_file}")
