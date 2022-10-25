#Inicio del huevo
print("Hola, el dia de hoy haremos un huevo frito, ¿tienes los ingredientes?")
print("Porfavor responde si o no en las preguntas que se te den :)")


#Ingredientes
ingredientes = input("Tienes los ingredientes: ")

if(ingredientes == "si"):
    print("Es momento de prender la estufa")
elif(ingredientes == "no"):
    print("Sal a la tienda y consiguelos, nosotros te esperamos ;)")
    exit()
else:
    print("responde solamente si o no, reinicia y vuelvelo a intentar")
    exit()

#Calentando sarten

print("Una vez con todos los ingredientes procedemos a prender la estufa, aplicar aceite o mantequilla a nuestro sarten y calentarlo")

sarten = input("¿crees que ya esta caliente?: ")

if(sarten == "si"):
    print("Ya es hora de agregar nuestro huevo ;)")
elif(sarten == "no"):
    print("En cuanto este Agregas tu huevo ;)")
    exit()
else:
    print("responde solamente si o no, reinicia y vuelvelo a intentar")
    exit()
    
#Huevo frito 

print("Una vez que agregamos nuestro huevo y ponemos la tapa del sarten es solo esperar a que este frito")

frito = input("¿ya frito?: ")

if(frito == "si"):
    print("Apaga el fogon y sirvete tu huevo, recuerda que puedes hecharle especias ;)")
elif(frito == "no"):
    print("En cuanto este apagas el sarten, cuidado con quemarlo")
    exit()
else:
    print("responde solamente si o no, reinicia y vuelvelo a intentar")
    exit()