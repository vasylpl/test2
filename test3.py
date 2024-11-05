print("Vítejte v programu pro výpočet elektrického výkonu (P), napětí (U) nebo proudu (I)")

while True:  # provádí výpočty opakovaně, dokud se nerozhodne program ukončit.
    
    volba = input("Co chcete vypočítat? Zadejte 'P' pro výkon, 'U' pro napětí, nebo 'I' pro proud: ")
    
    if volba == "P":
        napeti = float(input("Zadejte napětí (U) ve voltech: "))
        while napeti < 0:
            napeti = float(input("Chyba: Napětí nemůže být záporné. Zadejte znovu napětí (U) ve voltech: "))
        
        proud = float(input("Zadejte proud (I) v ampérech: "))
        while proud < 0:
            proud = float(input("Chyba: Proud nemůže být záporný. Zadejte znovu proud (I) v ampérech: "))
        
        vykon = napeti * proud
        print("Výsledek: Výkon P =", vykon, "W")
    
    elif volba == "U":
        vykon = float(input("Zadejte výkon (P) ve wattech: "))
        while vykon < 0:
            vykon = float(input("Chyba: Výkon nemůže být záporný. Zadejte znovu výkon (P) ve wattech: "))
        
        proud = float(input("Zadejte proud (I) v ampérech: "))
        while proud < 0:
            proud = float(input("Chyba: Proud nemůže být záporný. Zadejte znovu proud (I) v ampérech: "))
        
        if proud != 0:
            napeti = vykon / proud
            print("Výsledek: Napětí U =", napeti, "V")
        else:
            print("Chyba: Proud nemůže být 0.")

    elif volba == "I":
        vykon = float(input("Zadejte výkon (P) ve wattech: "))
        while vykon < 0:
            vykon = float(input("Chyba: Výkon nemůže být záporný. Zadejte znovu výkon (P) ve wattech: "))
        
        napeti = float(input("Zadejte napětí (U) ve voltech: "))
        while napeti < 0:
            napeti = float(input("Chyba: Napětí nemůže být záporné. Zadejte znovu napětí (U) ve voltech: "))
        
        if napeti != 0:
            proud = vykon / napeti
            print("Výsledek: Proud I =", proud, "A")
        else:
            print("Chyba: Napětí nemůže být 0.")

    else:
        print("Neplatná volba, zkuste to znovu.")

    opakovani = input("Chcete provést další výpočet? (ano/ne): ")
    if opakovani.lower() != "ano":  # Převedeme vstup na malá písmena pro snadnější porovnání
        print("Děkujeme za použití programu. Nashledanou!")
        break
