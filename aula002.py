

v = float (input("Digite a velocidade do carro (km/h): "))
print (f"Velocidade informada: {v}")


if v>80:
    m = 20 *(v-80)
    print ("Velocidade acima de 80 km/h. Você foi multado.")
    print (f"Multa (R$): {m:.2f}")


    