def main():
    numero = int (input ("Digite um número: "))


    i = 2

    while numero != i and numero != 1:
        if numero % i == 0:
            break
        i += 1
    
    if numero == i:
        print("O número", numero, "é primo")
    elif numero== 1:
         print("o número 1 não é primo")
    else:
        print("o número", numero, "não primo porque é divisivel por", i)


    return 0 
main()