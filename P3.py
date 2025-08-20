try:
    a = float(input("ingrese el primer numero"))
    b = float(input("ingrese el segundo numero"))

    res = a / b
    print("resultado:", res)
except ZeroDivisionError:
    print("error")
    