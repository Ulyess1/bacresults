print("Created By Mr-Ulyess ::")
print()
print("Select your Choice :")
print()
print("1-Bac Science Pc.")
print("2-Bac Science Svt.")
print("3-Bac Science Math (A).")
print("4-Bac Science Math (B).")
print("5-Bac Lettres.")
print("6-Bac Sciences Économiques et Gestion.")
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

    m = Math * 9
    ph = philo * 3
    phy = pc * 7
    scii = si * 3
    ang = anglais * 3
    avgtota = m + ph + scii + ang 
    notesavg = avgtota / 25
    regcont = regional + controle1
    regcontdiv = regcont / 2
    notesbac = notesavg + regcontdiv 
    notesbacdiv = notesbac / 2
    

    if notesbacdiv >= 10:
        print("Passed", round(notesbacdiv, 2))
    elif notesbacdiv < 10 and notesbacdiv > 7:
        print("Retake", round(notesbacdiv, 2))
    else:
        print("Failed", round(notesbacdiv, 2))
##Bac science(B)
elif choice == "4":
    print("Now Add your notes")
    Math = float(input("Math :").replace(",", "."))
    philo = float(input("Philosophie :").replace(",", "."))
    physique = float(input("Physique :").replace(",", "."))
    svt = float(input("science de la vie et de la terre :").replace(",", "."))
    anglais = float(input("Anglais :").replace(",", "."))
    regional = float(input("entrez votre note du regional :").replace(",", "."))
    controle1 = float(input("entrez votre note du controle 1er semestre :").replace(",", "."))

    m = Math * 9
    pc = physique * 7
    s = svt * 3
    a = anglais * 3
    ph = philo * 3
    
    totalnotes = m + pc + s + a + ph
    totalnotesdiv = totalnotes / 25
    regcont = regional + controle1
    regcontdiv = regcont / 2
    moyennegeneral = totalnotesdiv + regcontdiv
    lanotetotale = moyennegeneral / 2
    
    if lanotetotale >= 10:
        print("Passed", round(lanotetotale, 2))
    elif lanotetotale < 10 and lanotetotale > 7:
        print("Retake", round(lanotetotale, 2))
    else:
        print("Failed", round(lanotetotale, 2))

## Bac Lettres 
elif choice == "5":
    print("Now Add your notes")
    arabe = float(input("Langue Arabe :").replace(",", "."))
    philo = float(input("Philosophie :").replace(",", "."))
    hist_geo = float(input("Histoire-Géographie :").replace(",", "."))
    deuxi = float(input("Deuxieme langue :").replace(",", "."))
    regio = float(input("Regional :").replace(",","-"))
    controle = float(input("Controle :").replace(",","-"))
    a = arabe * 4
    ph = philo * 3
    hist = hist_geo * 3
    deux = deuxi * 4 
    totalcoef = a + ph + hist + deux 
    totaldiv = totalcoef / 14
    regcont = regio + controle
    regcontdiv = regcont / 2
    avgnot = totaldiv + regcontdiv
    avgnotes = avgnot / 2
    if avgnotes >= 10:
        print("Passed", round(avgnotes, 2))
    elif avgnotes < 10 and avgnotes > 7:
        print("Retake", round(avgnotes, 2))
    else:
        print("Failed", round(avgnotes, 2))
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

    ec = eco *7
    comp = compta * 7 
    gest = gestion * 6
    ph = philo * 2 
    an = anglais * 3
    avgnatio = ec + comp + gest + ph + an 
    avgnatiodiv = avgnatio / 25
    regcont = regional + controle1
    regcontdiv = regcont / 2
    notesbac = avgnatiodiv + regcontdiv 
    notesbac1 = notesbac / 2


    if notesbac1 >= 10:
        print("Passed", round(notesbac1, 2))
    elif notesbac1 < 10 and notesbac1 > 7:
        print("Retake", round(notesbac1, 2))
    else:
        print("Failed", round(notesbac1, 2))

else:
    print("invalid choice")