import random

def Product(count=0):

    first = random.randint(10, 30)
    second = random.randint(10, 30)

    print("---> ", first, "*", second)

    correct = first * second

    answer = input("Insert your answer here (type 'stop' to end the game): ")

    if answer.lower() == "stop":
        confirm_stop = input("Are you sure you want to stop the game? (yes/no): ").lower()
        if confirm_stop == "yes":
            print("Thanks for playing! You played", count, "times.")
            return  # Termina la función sin continuar
        elif confirm_stop == "no":
            Product(count)
        else:
            # Si el jugador no confirma detener el juego, continua
            Product(count)

    elif answer != "stop":
        try:
            answer = int(answer)
            if correct == answer:
                print("Correct! Well done.")
                
            else:
                print("Incorrect, the correct answer was: ", correct)
            
            count += 1
            Product(count)
            
        except ValueError:
            print("Invalid input! Please enter a number or 'stop'.")
            Product(count)


if __name__ == '__main__':
    Product()