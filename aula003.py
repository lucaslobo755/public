

contador=0

soma=0

while  True:
    numero=int(input ("Informe um valor inteiro: "))
   
    if numero==0: break

    soma+=numero
    contador+=1

print (f"\n PAUSA! Você digitou o 0 (zero).\n Qtd de números digitados antes do 0 (zero): {contador}.\n Soma: {soma}.\n Média: {(soma/contador):.2f}.")


