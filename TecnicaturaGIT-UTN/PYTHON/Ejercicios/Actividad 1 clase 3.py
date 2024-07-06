# Ejercicio 1: Califica tu día

# Se define una función para calificar el día
def calificar_dia():
  # Se solicita al usuario que califique su día del 1 al 10
  print("¿Cómo estuvo tu día (1 al 10)?")
  calificacion_dia = int(input("Escribe un número: "))

  # Se valida que la calificación ingresada sea un número entre 1 y 10
  while calificacion_dia < 1 or calificacion_dia > 10:
    print("La calificación debe ser un número entre 1 y 10.")
    calificacion_dia = int(input("Escribe un número: "))

  # Se muestra un mensaje personalizado en base a la calificación ingresada
  if calificacion_dia >= 8:
    print("¡Me alegra saber que tuviste un día excelente!")
  elif calificacion_dia >= 5:
    print("¡Parece que tuviste un buen día!")
  else:
    print("Espero que mañana sea un mejor día.")

  print(f"Tu calificación fue: {calificacion_dia}")

# Se llama a la función para calificar el día
calificar_dia()