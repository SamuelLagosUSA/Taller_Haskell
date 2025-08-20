contrasena = "123456"
entrada = input("ingrese la contraseña: ")

if entrada.lower() == contrasena.lower():
    print("contraseña correcta")
else:
    print("la contraseña no es correcta")