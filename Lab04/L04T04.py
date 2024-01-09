while True:
    try:
        luku = int(input("Anna luku (1-10): "))
        if luku > 0 and luku <= 10:
            break
        else:
            print("Anna numero 1-10 väliltä.")
    except ValueError:
        print("Anna numero 1-10 väliltä.")

for i in range(luku):   
    print(f"Luvun {i+1} neliö on {(i+1)**2}")