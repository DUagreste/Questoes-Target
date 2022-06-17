n1 = 0
n2 = 1
n3 = 0

n = int(input("Digite o número que deseja verificar: "))

while(n > n3):
    n3 = n1 + n2
    n1 = n2
    n2 = n3

if (n == 0):
    print("O número 0 está na sequência de Fibonacci.")
elif (n == n3):
    print(f" O número {n} está na sequência de Fibonacci.")
else:
    print(f"O número {n} não está na sequência de Fibonacci.")
