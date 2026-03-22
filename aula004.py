

n= int(input("Informe de qual número você quer a tabuada (1 a 10):\n"))

if(n<1 or n>10):

    print("Que pena! Você informou um valor fora do intervalo de 1 a 10. Tente novamente.")

else:

 for i in range (1,11):
    print (f"{n}x{i}={n*i}")


