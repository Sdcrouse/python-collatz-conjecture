def collatz_conjecture():
    introduction()
    main_loop()
    good_bye()

def introduction():
    print('The Collatz Conjecture is a famous unsolved problem in mathematics.')
    print('It states the following:')
    print('\n1. Start with a positive integer (i.e. a number greater than 0)')
    print('2. If the number is even, divide it by 2')
    print('3. If the number is odd, multiply it by 3 and add 1')
    print('4. Repeat Steps 2 and 3')
    print('\nThe Collatz Conjecture states that for any positive integer, the above process will eventually end at the number 1.')
    print('Can you disprove it? Think of a positive number and try it out!')

def main_loop():
    while True:
        try:
            number = int(input('\nEnter a number: '))
            if number <= 0:
                print('The number must be greater than 0. Please try again.')
            else:
                print('Here is the Collatz sequence:')
                print(collatz(number))

                quit = input('\nWould you like to try another number? (Y/n) ').lower()
                if quit == 'n' or quit == 'no':
                    break
                elif quit != 'y' and quit != 'yes':
                    print('Invalid choice.')
        except ValueError:
            print('Invalid input. Please try again.')

def collatz(number):
    collatz_numbers = [str(number)]

    while True:
        # Put this if/else logic into a separate method and test it. Then, delete this comment.
        # I may want to do something similar with the main_loop() method and test with valid/invalid inputs.
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        
        collatz_numbers.append(str(number))

        if number == 1:
            break

    collatz_sequence = ' -> '.join(collatz_numbers)

    return collatz_sequence

def good_bye():
    print('\nThanks for trying out the Collatz Conjecture! Goodbye.')

if __name__ == '__main__':
    collatz_conjecture()