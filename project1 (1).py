'''
Project 1 - Game Score Evaluator - Fall 2023
Author: Gavin Richeal (gavinr@vt.edu)

This program recieves a numeric game score and repeatedly returns four
different statements: Beginner, Advanced, Expert, and Intermediate based on
whatever score the user inputs.

I have neither given nor received unauthorized assistance on
this assignment
Signed: Gavin Richeal
'''


def evaluate_score(score):
    if score < 0:
        print('Error: Invalid input. Score cannot be negative.')
    else:
        perf_lvl = determine_level(score)
        print('That performance level is ' + perf_lvl)
        
    '''evaluate_score defines the integer argument as score and checks
with an if statement if it less than 0. If it is, it produces a Invalid Input
otherwise it continues to the code as is''' 

def determine_level(score):
    if score <= 100:
        return 'Beginner'
    if score <= 500:
        return 'Intermediate'
    if score <= 1000:
        return 'Advanced'
    else:
        return 'Expert'
    
    '''determine_level sets up the parameters of the function and then
returns the desired output being Beginner, Intermediate, Advanced,
Expert.'''

def main():
    print('Welcome to the game score evaluator!')

    while True:
        game_input = input("Enter a game score (or 'q' to quit): ")

        if game_input == 'q':
            break
        
        if game_input.isdigit():
                score = int(game_input)
                evaluate_score(score)
        else:
            print('Error: Invalid input. Please enter a valid integer score.')
            
    print('Thanks for using the game score evaluator!')
    

if __name__ == '__main__':
    main()    

'''main houses the while loop used to produce the code it uses an
input operator to prompt the string the enter the game score and as
long as the input does not equal 'q' and is an integer it gives the
desired output'''