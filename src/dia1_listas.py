lotes = [120, 98, 105]   # una bandeja con la etiqueta "lotes"
lotes_revisados = lotes  # NO crea otra bandeja: pega una 2.ª etiqueta en la MISMA
lotes_revisados.append(110) # agrega 110 al FINAL de esa única bandeja
print("1:", lotes)

copia = lotes.copy()   # AHORA sí: una bandeja NUEVA con el mismo contenido
copia.append(99)       # el 99 entra solo en la bandeja nueva
print("2:", lotes)
print("3:", copia)

print("4:", lotes is lotes_revisados, lotes is copia)