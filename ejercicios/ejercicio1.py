def calculadora(a,b):
    while True:
        try:
            opcion = input("Ingresa lo que queres hacer (suma/resta/mult/div): ")
            if opcion != "suma" and opcion != "resta" and opcion != "mult" and opcion != "div":
                raise ValueError("Temes que ingresar una opcion valida") 
            if opcion == "suma":
                resultado = a + b
                return resultado
            elif opcion == "resta":
                resultado = a - b
                return resultado
            
            elif opcion == "mult":
                resultado = a * b
                return resultado
            elif opcion == "div":
                if b == 0:
                    raise ZeroDivisionError ("No se puede dividir por cero")
                else: 
                    a / b
        except ValueError as error:
            print(error)
        except ZeroDivisionError as error:
            print(error)
            

res = calculadora(10, 0)

print(res)
