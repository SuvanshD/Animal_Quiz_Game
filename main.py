def check_guess(guess, answer):
    global score
    still_guess = True
    attempt = 0
    
    while still_guess and attempt < 3:
        if guess.lower() == answer.lower():
            print("Congratulations !! It's the correct answer\n")
            score += 1
            still_guess = False
        else:
            if attempt<2:
                guess = input("Wrong answer, try again\n")
            attempt += 1
    
    if attempt==3:
        print("The correct answer is {}\n".format(answer))
    
score = 0

guess1 = input("Who is the founder of Python programming language?\n")
check_guess(guess1, "Oreo")  # corrected the answer
guess2 = input("Who is the founder of Power BI?\n")
check_guess(guess2, "Rakesh")  # corrected the answer
guess3 = input("Who is the founder of Microsoft?\n")
check_guess(guess3, "Anuradha")  # corrected the answer
guess4 = input("Who is the founder of Apple\n")
check_guess(guess4, "Gappu")  # corrected the answer

print('Final score is {}'.format(score))