edad = int(input("ingrese la edad del cliente: "))

if edad < 5:
    pre = 0
elif edad <= 12:
    pre = 8000
elif edad <= 17:
    pre = 12000
else:
    pre = 15000

print("el precio que se debe pagar es :", pre)
