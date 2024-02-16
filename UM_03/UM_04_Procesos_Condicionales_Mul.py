punt_obt=int(input("Ingrese el  Puntaje Obtenido:"))
if punt_obt>150:
    print("Eres un Master en Python")
elif 100 < punt_obt <=150:
    print("Tienes un Nivel Señior")    
elif 70 <  punt_obt <=100:
    print("Tienes un Nivel Intermedio")    
else:
    print("Tienes un Nivel Basico")    