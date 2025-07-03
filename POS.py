import os  # Import die os module om skerm skoonmaak te kan doen

items = []  # Lys om alle items (produknaam en prys) te stoor

# Funksie om 'n item by die lys te voeg
def voeg_item_by():
    # Vra die gebruiker om die produknaam in te tik
    naam = input("Tik die produknaam in: ")
    try:
        # Vra die gebruiker om die prys in te tik en verander dit na 'n float toe
        prys = float(input("Tik die prys van die produk in: R"))
        # Voeg 'n tuple met die produknaam en prys by die items lys
        items.append((naam, prys))  
        # Bevestig vir die gebruiker dat die produk bygevoeg is
        print(f"{naam} is bygevoeg teen R{prys:.2f}")
    except ValueError:
        # Error boodskap as die prys nie 'n geldige nommer is nie
        print("Fout: Ongeldige prys.")

# Funksie om al die items met pryse en die totaal uit te druk
def wys_items():
    totaal = 0  # Begin totaal by nul
    print("\n--- Lys van items ---")
    # Gaan deur elke item in die lys en druk die naam en prys uit
    for item in items:
        naam, prys = item
        print(f"{naam:<10} R{prys:.2f}")  # Format die prys met 2 desimale plekke
        totaal += prys  # Voeg die prys by die totaal
    print("----------------------")
    # Print die totaal van al die items
    print(f"Totaal     R{totaal:.2f}")

# Funksie om die skerm skoon te maak
def maak_skoon():
    os.system("cls" if os.name == "nt" else "clear")

aan_die_gang = True  # Sentinel variable om die hooflus te beheer

# Hoofprogram 'loop' wat sal aanhou totdat aan_die_gang 'False' word
while aan_die_gang:
    # Vertoon die menu vir die gebruiker
    print("\n=== POS Stelsel ===")
    print("1. Voeg item by")
    print("2. Wys items en totaal")
    print("3. Maak skerm skoon")
    print("4. Verlaat")

    # Vra die gebruiker om 'n keuse te maak
    keuse = input("Kies 'n opsie (1-4): ")

    # Besluit wat gebeur op grond van die gebruiker se 'input'
    if keuse == "1":
        voeg_item_by()  # Funksie om item by te voeg
    elif keuse == "2":
        wys_items()     # Funksie om items en totaal te wys
    elif keuse == "3":
        maak_skoon()    # Funksie om die skerm skoon te maak
    elif keuse == "4":
        aan_die_gang = False  # Verander sentinel variable om die 'loop' te stop
        print("Totsiens!")    # Groet die gebruiker
    else:
        # As die invoer ongeldig is, vra die gebruiker om weer te probeer
        print("Ongeldige keuse. Probeer asseblief weer.")
