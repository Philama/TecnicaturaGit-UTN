miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
print(id(x))
y = 2
z = x + y
# Las literales se escriben x528, la variable y = x272, la variable z = x592
print(id(y))
print(id(z))

#Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x="Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))
#Manejo de cadenas (String)
miGrupoFavorito = "The Letter Black:"
caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)
numerol = "7"
numero2 = "8"
print(int(numerol) + int(numero2))


# Tipos Boleanos (bool)
miBooleano = 3 > 2
print(miBooleano)


if miBooleano:
  print("El resultado es verdadero")
else:
  print("El resultado es falso")

#Procesar la entrada del usuario
#función input
#resultado input("Digite un numero: ") regresa un dato tipo string
#print(resultado)

#Conversión de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es:", resultado)
  