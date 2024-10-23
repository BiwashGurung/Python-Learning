import random
rand = random.randrange(1,100)
attempt = 0
guess = int(input("Enter any number you like:"))
while rand!= guess:
    if guess < rand:
        attempt +=1
        print("Too Low")
        guess = int(input("Enter any Number:"))
    elif guess > rand:
        attempt +=1
        print("Too high")
        guess = int(input("Enter any Number:"))   
    else:
        break
attempt +1   

print(f"Your Guess The correct Number in {attempt}  attemps!!!")     

