#Variables
gravedad_neptuno = 1.136
gravedad_marte = 0.378

#calcular nuestro peso en marte y neptuno
peso_Nosotros = float(input("Bienvenido, porfavor ingrese su peso: "))

resultado_marte = (peso_Nosotros * gravedad_marte)
resultado_neptuno = (peso_Nosotros * gravedad_neptuno) 

print("Tu peso actualmente en marte equivaldria unos", resultado_marte)
print("Tu peso actualmente en neptuno equivaldria unos", resultado_neptuno)

numero = 5

if(numero > 5):
    print("el numero es mayor a 3")
elif(numero == 5):
    print("el numero es igual a 5")
else:
    print("el numero es menor que 5")

