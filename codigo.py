def suma(numeros):
    return sum(numeros)

def resta(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def multiplicar(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def dividir(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        if num == 0:
            return "Error: División por cero"
        resultado /= num
    return resultado

def potenciar(numeros):
    base = numeros[0]
    exponente = numeros[1] if len(numeros) > 1 else 2
    return base ** exponente

def porcentaje(numeros):
    if len(numeros) < 2:
        return "Error: Se necesitan dos números para calcular porcentaje"
    total = numeros[0]
    porcentaje = numeros[1]
    return (total * porcentaje) / 100

def calculadora():
    print("Bienvenido a la calculadora")
    operacion = input("Escoje una operación (suma, resta, multiplicar, dividir, potenciar, porcentaje): ").strip().lower()
    num_numeros = int(input("Cuántos números quieres ingresar? "))
    
    numeros = []
    for i in range(num_numeros):
        numero = float(input(f"Ingresa el número {i + 1}: "))
        numeros.append(numero)
    
    if operacion == "suma":
        print("Resultado de la suma:", suma(numeros))
    elif operacion == "resta":
        print("Resultado de la resta:", resta(numeros))
    elif operacion == "multiplicar":
        print("Resultado de la multiplicación:", multiplicar(numeros))
    elif operacion == "dividir":
        print("Resultado de la división:", dividir(numeros))
    elif operacion == "potenciar":
        print("Resultado de la potenciación:", potenciar(numeros))
    elif operacion == "porcentaje":
        print("Resultado del porcentaje:", porcentaje(numeros))
    else:
        print("Operación no válida")

if __name__ == "__main__":
    calculadora()
