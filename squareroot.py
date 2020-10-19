# heron of alexandria greek
# find sqaure root of a number
import time
square_root_of = float(input("SQUARE ROOT OF: "))
precision = float(input("PRECISION: "))
if square_root_of < 0:
    print("SQUARE ROOT OF A NUMBER LESS THAN ZERO IS NOT REAL.")
else:
    tic = time.time()
    upper = square_root_of + precision
    lower = square_root_of - precision
    guess = 2

    while True:
        square_of_guess = guess * guess
        if square_of_guess <= upper and square_of_guess >= lower:
            square_root = guess
            break
        else:
            guess = (guess + (square_root_of/guess))/2
    tac = time.time()
    print("{:.3f}".format(square_root))
    print(f"COMPUTATION TIME: {tac-tic} ")

    #testing result
    import math
    tic = time.time()
    check = math.sqrt(square_root_of)
    tac = time.time()
    print("{:.3f}".format(check))
    print(f"COMPUTATION TIME: {tac-tic}")
