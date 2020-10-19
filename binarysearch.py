import random
pick = random.randint(1,1000000)

#mr. bob
def bob(num,pick):
    if num == pick:
        return "e"
    elif num > pick:
        return "g"
    else:
        return "l"

#ms. mary
def mary(val1, val2):
    min_val = val1
    max_val = val2
    #guess = int((min_val + max_val)/2)
    guess = int((min_val + max_val)//2)
    #conversation
    print(f"Mary: hey bob, did I guess the number right? my guess {guess}")
    response = bob(guess,pick)
    if response == "e":
        return f"Bob: yes mary, you guessed it right! I picked {guess}."
    elif response == "g":
        print("Bob: your guess is too high, mary!")
        max_val = guess - 1
        return mary(min_val, max_val)
    elif response == "l":
        print("Bob: your guess is too low, mary!")
        min_val = guess + 1
        return mary(min_val, max_val)
    
#test1
mary(1,1000000)
    
