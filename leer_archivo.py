# Lectura de archivo de texto
# Abrimos el archivo en modo lectura ('r')
with open('mis_notas.txt', 'r') as file:
    # Leemos línea por línea usando readline() en un bucle
    line = file.readline()
    while line:
        print(line.strip())  # Mostramos la línea en consola sin saltos de línea extra
        line = file.readline()

