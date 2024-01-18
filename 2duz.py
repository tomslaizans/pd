import csv

def otrie(csv_file):
    with open(csv_file, 'r') as fails:
        reader = csv.reader(fails)
        for row in reader:
            if len(row) >= 2:
                print(row[1])

if __name__ == "__main__":
    nosaukums=input("ievadi nosaukumu: ")
try:
    otrie(nosaukums)

except FileNotFoundError:
    print("nauuhh")
