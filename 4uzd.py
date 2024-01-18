def lasit_un_drukats(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{faila_nosaukums}' nav.")
    except Exception as e:
        print(f"Notika kļūda: {e}")

if __name__ == "__main__":
    faila_nosaukums = input("Ievadiet faila nosaukumu: ")
    faila_formats = input("Ievadi faila formaty: ")
    pilns_faila_nosaukums = f"{faila_nosaukums}.{faila_formats}"
    lasit_un_drukats(pilns_faila_nosaukums)
