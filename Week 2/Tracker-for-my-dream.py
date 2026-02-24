def main():
    
    age = int(input("What is your age? "))
    savings = float(input("How much did you save (USD) ? ").strip().replace("$", ""))

    calculate_status (age, savings)


def calculate_status(age, savings):
    if age <= 15 and savings >= 10000:
        print("I don't belive you, but if you got that money at your age, you are on the right path")
    elif age <= 18 and savings >= 50000:
        print("U just got out from high school and making that much money?, you got to be einsten haha, but anyways, keep coding, you are really close :)")
    elif age <= 20 and savings >= 200000:
        print("U can buy an Aston Martin now :), i wish i was you") 
    elif age <= 20 and savings >= 160000:
        print("You are really close, keep coding")
    elif savings >= 400000:
        print("Wow")     
    elif savings <= 20:
        print("Umm, keep coding i guess...")   
    elif age >= 30 and age <= 69:
        print("Its no expiration date for dreams, keep it up!")
    elif age >= 70 and age <= 99:
        print("You are a legend, keep coding and inspirating others :) ")
    elif age >= 100 and age <= 149:
        print("Wow, over a hundred years old and still coding, you are a legend, keep coding and inspirating others :) ")
    elif age > 150:
        print("Do you even even exist? haha, but if you do, you are a legend, keep coding and inspirating others :) ")
    else:
        print("I belive in you, you are on the right path budy :) ")   

if __name__ == "__main__":
    main()

