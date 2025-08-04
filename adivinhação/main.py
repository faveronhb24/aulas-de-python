import random
def main():
    numAleatorio = random.randint(1, 485)

    numero = 0
    i = 0
    while numero != numAleatorio:
        numero = int ( input("Digite um número"))

        if numero > numAleatorio:
            print("o seu número é maior")
        elif numero < numAleatorio:
            print("o seu numero é menor")
        i += 1

        print("\n")

    print("você acertou, com ", i, " tentativas")
    return 0
main()