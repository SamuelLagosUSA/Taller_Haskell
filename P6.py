nombre = input("ingrese su nombre ")
genero = input("ingrese su genero (m/f): ")

if genero.upper() == "m":
    print(nombre, "pertenece al grupo 1")
elif genero.upper() == "f":
    print(nombre, "pertenece al grupo 2")