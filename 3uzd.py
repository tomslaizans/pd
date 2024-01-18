def lasit_teksta_failu(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r', encoding='utf-8') as fails:
            rindas = fails.readlines()
            if len(rindas) >= 3:
                print("Trešā rinda:", rindas[2])
            else:
                print("Kļūda: Fails pa īsu.")
    except FileNotFoundError:
        print(f"Kļūda: Fails '{faila_nosaukums}' nepastāv.")
    except Exception as e:
        print(f"Notika kļūda: {e}")

if __name__ == "__main__":
    faila_nosaukums = input("Ievadi teksta faila nosaukumu: ")

    lasit_teksta_failu(faila_nosaukums)
