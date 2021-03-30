# Author - Prikota Alexandr
# finding the given sequence of the random numbers
# The average number of the guess attempt per a number is 5
import numpy as np

# finding the number via dichotomy
def my_number_guess(number):
    count = 1
    predict = np.random.randint(1,101)  # initial guess
    err = predict - number
    while err != 0:
        count += 1
        if err > 0:
            predict -= int(err/2) + 1
        else:
            predict += int(-err/2) + 1
        err = predict - number
    return(count) # return the number of the used attempts

def my_score_game(game_core):
    Nruns = 1000
    count_ls = []
    np.random.seed(2)  # choose the particular seed to get the same random sequence or for various runs of the program
    random_array = np.random.randint(1,101, size=Nruns)  # get the sequence of the random numbers
    for number in random_array:
        count_ls.append(my_number_guess(number))
    score = int(np.mean(count_ls))
    print("Ваш алгоритм угадывает число в среднем за", score, "попыток")
    return(score)

my_score_game(my_number_guess)