def main():
    inicio = int (input ("digite o inicio do intervalo: "))
    fim = int (input ("digite o fim do intervalo: "))


    i = 1 

    if inicio < fim:
        while inicio <= fim:
            print("tabuada do ", inicio)
            i = 1
            while i <= 10:
                print( inicio, " x ", i, " = ", inicio * i)
                i+=1
            print("\n")
            inicio += 1
    elif inicio > fim:
        while inicio >= fim:
            print("tabuada do ", inicio)
            i = 1
            while i <= 10:
                print( inicio, " X ", i, " = ", inicio * i)
                i+= 1
            inicio -=1
    return 0
main()
