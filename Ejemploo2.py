def calcular(a, b, c):
    res = a * b + c
    return res

def principal():
    x = float(input("multiplicando: "))
    y = float(input("multiplicador: "))
    z = float(input("sumando: "))
    resultado = calcular(x, y, z)
    print("El resultado es:", resultado)

principal()
