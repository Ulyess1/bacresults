print("Select your Choice")
print("1-Bac Science Pc")
print("2-Bac Science Svt")
choice = input("Enter 1 Or 2 :")

if choice == "1" :
 Math = float(input("Math :").replace(",","-"))
 philo = float(input("Philosophie :").replace(",","-"))
 pc = float(input("Physique :").replace(",","-"))
 svt = float(input("science de la vie et de la terre :").replace(",","-"))
 anglais = float(input("Anglais :").replace(",","-"))
 regional = float(input("entrez vote note du regional :").replace(",","-"))
 controle1 = float(input("entrez votre note du controle 1er semestre :").replace(",","-"))
 controle2 = float(input("entrez votre note du controle 2eme semestre :").replace(",","-"))
 m = Math * 7
 pc = pc * 7
 s = svt * 5
 a = anglais * 2
 ph = philo * 2
 total = m + pc + s + a + ph
 national = total / 23 
 cont = controle1 + controle2
 contcontinue = cont / 2
 regcont = regional + contcontinue 
 divregcont = regcont / 2
 moyennegeneral = national + divregcont
 lanotetotale = moyennegeneral / 2
 if lanotetotale >= 10:
  print("nje7ti",round(lanotetotale ,2))
 elif lanotetotale < 10 and lanotetotale > 7 :
  print("rattrapage",round(lanotetotale ,2))
 else:
  print("manje7tich",round(lanotetotale ,2))

  ## bac science svt

elif choice == "2":
    Math = float(input("Math :").replace(",", "."))
    philo = float(input("Philosophie :").replace(",", "."))
    pc = float(input("Physique :").replace(",", "."))
    svt = float(input("science de la vie et de la terre :").replace(",", "."))
    anglais = float(input("Anglais :").replace(",", "."))
    regional = float(input("entrez vote note du regional :").replace(",", "."))
    controle1 = float(input("entrez votre note du controle 1er semestre :").replace(",", "."))
    controle2 = float(input("entrez votre note du controle 2eme semestre :").replace(",","-"))
    m = Math * 7
    pc = pc * 5
    s = svt * 7
    a = anglais * 2
    ph = philo * 2
    total = m + pc + s + a + ph
    national = total / 23
    cont = controle1 + controle2
    contcontinue = cont / 2
    regcont = regional + contcontinue
    divregcont = regcont / 2
    moyennegeneral = national + divregcont
    lanotetotale = moyennegeneral / 2
    if lanotetotale >= 10:
        print("nje7ti", round(lanotetotale, 2))
    elif lanotetotale < 10 and lanotetotale > 7:
        print("rattrapage", round(lanotetotale, 2))
    else:
        print("manje7tich", round(lanotetotale, 2))
else:
 print("invalid choice")