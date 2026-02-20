is_valid = False

while True:
    user_pass = input("What's your password? ").lower().strip()
    numbers_found = 0
    
    for character in user_pass:
        if character.isdigit():
            numbers_found += 1 

    if len(user_pass) >= 9 and numbers_found >= 4 :
        print("Password is Secure")
        break
    
    elif len(user_pass) >= 6 and numbers_found >= 3 :
        print("Password is Mid-Level")
        break
    
    elif len(user_pass) >= 4 :
        print("Terrible Password")
        break
    else:
        print("Write a password please")  
        continue









#print bad, normal, good, secured