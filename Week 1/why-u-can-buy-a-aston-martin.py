#Ask if the user wants an aston martin

name = input("What is your name? ").strip(" ")

reply = input(f"Do you want an Aston Martin {name}? ").strip().lower()

no = ["no", "nah", "nope"]
yes = ["yes", "yeah", "yep"]

if reply in yes:
    print("Great choice!")
elif reply in no:
    print("U are not on my team.")
else:
    print("Just answer normally bro...")