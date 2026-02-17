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
    else:
        print("I belive in you, you are on the right path budy :) ")   

if __name__ == "__main__":
    main()