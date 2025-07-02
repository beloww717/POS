import os

items = []

def voeg_item_by():
    naam = input("Tik die produknaam in: ")
    try:
        prys = float(input("Tik die prys van die produk in: R"))
        items.append((naam, prys))  
        print(f"{naam} is bygevoeg teen R{prys:.2f}")
    except ValueError:
        print("Fout: Ongeldige prys.")

def wys_items():
    totaal = 0
    print("\n--- Lys van items ---")
    for item in items:
        naam, prys = item
        print(f"{naam:<10} R{prys:.2f}")
        totaal += prys
    print("----------------------")
    print(f"Totaal     R{totaal:.2f}")

def maak_skoon():
    os.system("cls" if os.name == "nt" else "clear")

aan_die_gang = True

while aan_die_gang:
    print("\n=== POS Stelsel ===")
    print("1. Voeg item by")
    print("2. Wys items en totaal")
    print("3. Maak skerm skoon")
    print("4. Verlaat")

    keuse = input("Kies 'n opsie (1-4): ")

    if keuse == "1":
        voeg_item_by()
    elif keuse == "2":
        wys_items()
    elif keuse == "3":
        maak_skoon()
    elif keuse == "4":
        aan_die_gang = False  
        print("Totsiens!")
    else:
        print("Ongeldige keuse. Probeer asseblief weer.")