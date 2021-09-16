secondes = int(input("choisir nombre de secondes:"))
heure = secondes//3600
minute = (secondes%3600)//60
seconde = (secondes%3600)%60
print(heure, minute, seconde) 