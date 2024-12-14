najbolji_djak = 1.0
najgori_djak = 5.0
broj_djaka = int(input("Koliko imate djaka"))
for i in range (broj_djaka) :
    zbir_ocena = 0
    ocene_po_djaku = int(input("Koliko ocena po ovom djaku?"))
    for i in range (ocene_po_djaku):
        ocena = int(input("Koja su ocene ovom djaku?"))
        zbir_ocena = zbir_ocena + ocena
    prosek_ocena = zbir_ocena / broj_djaka 
    zaokruzen_prosek = round ( prosek_ocena , 1 )
    if zaokruzen_prosek > najbolji_djak :
        najbolji_djak = zaokruzen_prosek
    elif zaokruzen_prosek < najgori_djak :
        najgori_djak = zaokruzen_prosek
print("ocena najboljeg djaka je " , najbolji_djak )
print("ocena najgoreg djaka je" , najgori_djak )