def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
   return a * b

def dividir(a,b):
    return a/b

def exponencial(a,b):
    return a**b

def menu():
    opc = { "1)": "Sumar", "2)": "Restar", "3)": "Multiplicar", "4)": "Dividir", "5)": "Exponencial" }
    for k, v in opc.items():
        print(k, v)

print("----Menu----")
menu()
print("------------")
op = int(input("Elija una opción (1-5)\n"))
a = int(input("Introduce el primer número\n"))
b = int(input("Introduce el segundo número\n"))

if op == 1:
    print ("La suma de "+  str(a) + "+" + str(b) +" es = " + str(suma(a,b)))
elif op == 2:
    print ("La resta de "+  str(a) + "-" + str(b) +" es = " + str(resta(a,b)))
elif op == 3:
    print ("La multiplicacion "+  str(a) + "*" + str(b) +" es = " + str(multiplicacion(a,b)))
elif op == 4:
    try:
        print("La multiplicacion " + str(a) + "/" + str(b) + " es = " + str(dividir(a, b)))
    except ZeroDivisionError:
        print("No se puede divir entre 0")
elif op == 5:
    print (str(a) + " ^ " + str(b) +" es = " + str(exponencial(a,b)))












