
nome = input ("Digite seu nome: ")
print (f"Olá, {nome}!")

idade = int(input("Digite sua idade: "))
print (f"Você tem {idade} anos.")

altura = float(input ("Digite sua altura(metros): "))
print (f"Sua altura é {altura} m.")

peso = float(input ("Digite seu peso(kg): "))
print (f"Seu peso é {peso} kg.")

esporte = bool(input("Você prática esportes? (Digite True ou False) "))
print (f"Afirmar que você prática esportes é {esporte}.")

imc = peso/(altura**2)

print (f"Seu Imc é {imc:.2f}.")

if (imc<25):
    print (f"Seu IMC está bom. Continue assim!")
else:
    print (f"Seu IMC não está bom. Sugiro se cuidar mais.")
