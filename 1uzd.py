nosaukums=input("ievadi dokumenta nosaukumu: ")
try:
    with open(nosaukums,"r") as teksts:
            saturs=teksts.read()
            print(saturs)
except FileNotFoundError:
    print("nepastav!")