def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero"
    else:
        return 0

print(calculadora(10, 5, 1))  
print(calculadora(10, 5, 2))  
print(calculadora(10, 5, 3))  
print(calculadora(10, 5, 4))  
print(calculadora(10, 5, 9))  
