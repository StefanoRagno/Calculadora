ok = 1

while ok == 1:
  try:
    num1 = float(input("Ingrese un numero1: "))
    ok = 0
  except:
    print("Error! no se aceptan letras")

# Ejemplo de refactoring de Ricardo

#no_error = True
#while no_error:
#  try:
#    calculo = eval(input("Operación 'Ej: 2+2*(3-1)':"))
#    print("Resultado", calculo)
#    no_error = False
#  except Exception as e:
#    print("Algo salió mal, procure hacer operaciones como 2+2*(3-1) sin letras", str(e))

ok = 1
print("Ingrese la operación que quiere hacer")
while ok == 1:
  try:
    sig = input("Suma = +, Resta = -, Multiplicación = x, División = /: ")
    sig = sig.lower()
    if sig == "+" or sig == "-" or sig == "x" or sig == "*" or sig == "/":
      ok = 0
    else:
      ok = 1
  except:
    print("Error! entrada equivocada")

ok = 1
while ok == 1:
  try:
    num2 = float(input("Ingrese un numero2: "))
    ok = 0
  except:
    print("Error! no se aceptan letras")

if sig == "+":
  resultado = num1 + num2
elif sig == "-":
  resultado = num1 - num2
elif sig == "x" or sig == "*":
  resultado = num1 * num2
elif sig == "/":
  resultado = num1 / num2

print(f"El resultado es: {resultado}")