print("Select your Choice")
print("1-Bac Science Pc")
print("2-Bac Science Svt")
print("3-Bac Science Math (A)")
print("4-Bac Science Math (B)")
choice = input("Select Type of your Bac :")

if choice == "1" :
 print ("Now Add your notes")
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
    print("Now Add your notes")
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
##Bac Science Math (A)
elif choice == "3":
    print("Now Add your notes")
    Math = float(input("Math :").replace(",", "."))
    philo = float(input("Philosophie :").replace(",", "."))
    pc = float(input("Physique :").replace(",", "."))
    si = float(input("Sciences de l'Ingénieur :").replace(",", "."))
    anglais = float(input("Anglais :").replace(",", "."))
    regional = float(input("entrez votre note du regional :").replace(",", "."))
    controle1 = float(input("entrez votre note du controle 1er semestre :").replace(",", "."))
    controle2 = float(input("entrez votre note du controle 2eme semestre :").replace(",", "."))

    m = Math * 9
    pc_weighted = pc * 7
    si_weighted = si * 3
    a = anglais * 3
    ph = philo * 3
    
    total = m + pc_weighted + si_weighted + a + ph
    national = total / 25
    
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

elif choice == "4":
    print("Now Add your notes")
    Math = float(input("Math :").replace(",", "."))
    philo = float(input("Philosophie :").replace(",", "."))
    pc = float(input("Physique :").replace(",", "."))
    svt = float(input("science de la vie et de la terre :").replace(",", "."))
    anglais = float(input("Anglais :").replace(",", "."))
    regional = float(input("entrez votre note du regional :").replace(",", "."))
    controle1 = float(input("entrez votre note du controle 1er semestre :").replace(",", "."))
    controle2 = float(input("entrez votre note du controle 2eme semestre :").replace(",", "."))

    m = Math * 9
    pc_weighted = pc * 7
    s = svt * 3
    a = anglais * 3
    ph = philo * 3
    
    total = m + pc_weighted + s + a + ph
    national = total / 25
    
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