Stundenlohn = input("Bitte gebe deinen Stundenlohn ein: ")
ArbeitsTage = input("Bitte gebe deine Arbeitstage ein: ")
tag = 8 * int(Stundenlohn)
Monat = tag * int(ArbeitsTage)
Jahr = Monat * 12
ZehnJahre = Jahr * 120
print("Dein Stundenlohn beträgt " + str(Stundenlohn) + "€")
print("Du verdienst " + str(tag) + " € pro Tag")
print("Du verdienst " + str(Monat) + "€ im Monat ")
print("Du verdienst " + str(Jahr) + "€ im Jahr")
print("Du würdest in 10 Jahren " + str(ZehnJahre) + "€ verdienen")
input("Drücke eine belibige Taste um das Programm zu schließen")
