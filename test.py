
import sys

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(num1 + num2)
except IndexError:
    print("Error: Se requieren dos números como argumentos.")
