while True:
    try:
        dni = int(input("DNI: ")).strip()
        parts = dni.split(".")
        if 1 <= int(parts[0]) <= 9 :
            print("Tenes entre 75 a 99 años") #(You have 75 years old or more)
            break
        elif 10 <= int(parts[0]) <= 19 :
            print("Tenes entre 55 a 75 años")#(You are between 55 and 75 years old)
            break
        elif 20 <= int(parts[0]) <= 34 :
            print("Tenes entre 35 a 55 años")#(You are between 35 and 55 years old)
            break
        elif 35 <= int(parts[0]) <= 44 :
            print("Tenes entre 20 a 35 años")#(You are between 20 and 35 years old)
            break
        elif 45 <= int(parts[0]) <= 54 :
            print("Tenes entre 10 a 20 años")#(You are between 10 and 20 years old)
            break
        elif int(parts[0]) <= 55 :
            print ("Tenes menos de 10 años")#(You are 10 years old or less)
            break
        elif int (parts[1]) <= 999999:
            print("No creo que existas, pero estas entre 100 a 120 años")#(You have 75 years old or more)
            break
    except ValueError:
            print("Coloca un DNI valido porfavor") #(Put a valid DNI plaease)
            continue

        