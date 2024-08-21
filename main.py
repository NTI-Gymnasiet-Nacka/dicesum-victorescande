# Dice sum probability calculator
# Författare:
# Datum:
from collections import Counter

def main():
    user_input = input().split(" ")
    lista=[]
    while True:
        for table in range(1, 5):
            print(f"tabell {table}")
            for y in range(1, 7):
                print(f"{table} + {y} = {str(table+y)}")
                lista.append(str(table+y))
        break
    most_common = Counter(lista).most_common(len(lista))
    print(most_common)
    for i in range(len(most_common)):
        if int(most_common[0][1])== int(most_common[i][1]):
            print(most_common[i][0])



if __name__ == "__main__":
    main()

