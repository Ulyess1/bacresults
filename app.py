print("Select your Choice")
print("1-Bac Science Pc")
print("2-Bac Science Svt")
print("3-Bac Science Math (A)")
print("4-Bac Science Math (B)")
print("5-Bac Lettres et Sciences Humaines")
print("6-Bac Sciences Économiques et Gestion")
choice = input("Type The number of your Bac : ")

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
  print("Passed",round(lanotetotale ,2))
 elif lanotetotale < 10 and lanotetotale > 7 :
  print("Retake",round(lanotetotale ,2))
 else:
  print("Failed",round(lanotetotale ,2))

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
        print("Passed", round(lanotetotale, 2))
    elif lanotetotale < 10 and lanotetotale > 7:
        print("Retake", round(lanotetotale, 2))
    else:
        print("Failed", round(lanotetotale, 2))
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
        print("Passed", round(lanotetotale, 2))
    elif lanotetotale < 10 and lanotetotale > 7:
        print("Retake", round(lanotetotale, 2))
    else:
        print("Failed", round(lanotetotale, 2))

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
        print("Passed", round(lanotetotale, 2))
    elif lanotetotale < 10 and lanotetotale > 7:
        print("Retake", round(lanotetotale, 2))
    else:
        print("Failed", round(lanotetotale, 2))
## Bac Lettres et Sciences Humaines
elif choice == "5":
    print("Now Add your notes")
    arabe = float(input("Langue Arabe :").replace(",", "."))
    philo = float(input("Philosophie :").replace(",", "."))
    hist_geo = float(input("Histoire-Géographie :").replace(",", "."))
    anglais = float(input("Deuxieme langue :").replace(",", "."))
    regional = float(input("entrez votre note du regional :").replace(",", "."))
    controle1 = float(input("entrez votre note du controle 1er semestre :").replace(",", "."))
    controle2 = float(input("entrez votre note du controle 2eme semestre :").replace(",", "."))
    
    arabe_w = arabe * 4
    philo_w = philo * 4
    hist_geo_w = hist_geo * 3
    anglais_w = anglais * 3

    total_national = arabe_w + philo_w + hist_geo_w + anglais_w
    national_avg = total_national / 14

    cont_avg = (controle1 + controle2) / 2
    reg_cont_avg = (regional + cont_avg) / 2
    
    final_grade = (national_avg + reg_cont_avg) / 2

    if final_grade >= 10:
        print("Passed", round(final_grade, 2))
    elif final_grade < 10 and final_grade > 7:
        print("Retake", round(final_grade, 2))
    else:
        print("Failed", round(final_grade, 2))

## Bac Sciences Économiques et Gestion
elif choice == "6":
    print("Now Add your notes")
    eco = float(input("Économie Générale & Statistiques :").replace(",", "."))
    compta = float(input("Comptabilité & Mathématiques Financières :").replace(",", "."))
    gestion = float(input("Organisation des Entreprises :").replace(",", "."))
    philo = float(input("Philosophie :").replace(",", "."))
    anglais = float(input("Anglais :").replace(",", "."))
    regional = float(input("entrez votre note du regional :").replace(",", "."))
    controle1 = float(input("entrez votre note du controle 1er semestre :").replace(",", "."))
    controle2 = float(input("entrez votre note du controle 2eme semestre :").replace(",", "."))
    eco_w = eco * 6
    compta_w = compta * 4
    gestion_w = gestion * 3
    philo_w = philo * 3
    anglais_w = anglais * 3
    total_national = eco_w + compta_w + gestion_w + philo_w + anglais_w
    national_avg = total_national / 19 
    cont_avg = (controle1 + controle2) / 2
    reg_cont_avg = (regional + cont_avg) / 2
    final_grade = (national_avg + reg_cont_avg) / 2
    if final_grade >= 10:
        print("Passed", round(final_grade, 2))
    elif final_grade < 10 and final_grade > 7:
        print("Retake", round(final_grade, 2))
    else:
        print("Failed", round(final_grade, 2))

else:
    print("invalid choice")