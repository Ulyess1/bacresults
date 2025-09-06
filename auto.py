Math = float(input("Math :").replace(",","-"))
philo = float(input("Philosophie :").replace(",","-"))
pc = float(input("Physique :").replace(",","-"))
svt = float(input("science de la vie et de la terre :").replace(",","-"))
anglais = float(input("Anglais").replace(",","-"))
regional = float(input("entrez vote note du regional :").replace(",","-"))
controle = float(input("entrez vote note du controle continue :").replace(",","-"))
m = Math * 7
pc = pc * 7
s = svt * 5
a = anglais * 2
ph = philo * 2
total = m + pc + s + a + ph
national = total / 23 
regcont = regional + controle 
divregcont = regcont / 2
moyennegeneral = national + divregcont
lanotetotale = moyennegeneral / 2
if lanotetotale >= 10:
 print("nje7ti",lanotetotale)
elif lanotetotale < 10 and lanotetotale > 7 :
 print("rattrapage",lanotetotale)
else:
 print("manje7tich",lanotetotale)