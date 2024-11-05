# Přivítání uživatele
print("Vítejte v programu pro výpočet elektrického výkonu (P)")

# Cyklus pro opakování
while True:
    # Získání hodnot od uživatele
    napeti = float(input("Zadejte napětí (U) ve voltech: "))
    proud = float(input("Zadejte proud (I) v ampérech: "))

    # Výpočet výkonu
    vykon = napeti * proud
    print("Výsledek: Výkon P =", vykon, "W")

    # Dotaz, zda uživatel chce pokračovat
    opakovani = input("Chcete vypočítat další hodnotu? (ano/ne): ")
    if opakovani.lower() != "ano":
        print("Děkujeme za použití programu.")
        break
