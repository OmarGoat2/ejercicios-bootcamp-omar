num_1=input('Ingrese un primer número: ')
signo=input('Ingrese un signo: ')
num_2=input('Ingrese un segundo número: ')
def calculadora(num_1, signo, num_2):
    if signo == '+':
        return num_1 + num_2
    elif signo == '-':
        return num_1 - num_2
    elif signo == '*':
        return num_1 * num_2
    elif signo == '/':
        return num_1 / num_2
    elif signo == '**':
        return num_1 ** num_2
    elif signo == '//':
        return num_1 // num_2

resultado = calculadora(num_1, signo, num_2)
print('El resultado es', resultado)

