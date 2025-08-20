op = input("desea su pizza vegetariana? (si/no): ")

if opcion.lower() == "si":
    print("ingredientes: 1) pimientos 2) brocoli")
    ing = input("elija un ingrediente: ")
    if ing == "1":
        ing = "pimientos"
    else:
        ing = "brocoli"
    print("Su pizza ademas del queso mozzarella y el tomate tendra: ", ing)
else:
    print("ingredientes no vegetarianos: 1) peperoni 2) jamon 3) carne")
    ing = input("elija un ingrediente: ")
    if ing == "1"
       ing = "peperoni"
    elif ing == "2":
        ing = "jamon"
    else:
        ing = "carne"
    print("pizza normal con el siguiente ingrediente: ", ing)