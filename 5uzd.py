def ierakstit_faila(vards, nosaukums):
    try:
        with open(nosaukums, 'w', encoding='utf-8') as fails:
            fails.write(vards)
            print(f"Vārds '{vards}' tika ierakstīts failā '{nosaukums}'.")
    except Exception as e:
        print(f"Notika kļūda: {e}")

if __name__ == "__main__":
    vards = input("Ievadiet savu vārdu: ")
    faila_nosaukums = input("Ievadiet faila nosaukumu: ")
    ierakstit_faila(vards, faila_nosaukums)
