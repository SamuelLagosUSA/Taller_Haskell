edad = int(input("ingrese su edad: "))
ingr = float(input("ingrese sus ingresos actuales: "))

if edad >= 18 and ingr > 1000:
    print("tiene que pagar impuestos")
else:
    print("NO tiene que pagar impuestos")