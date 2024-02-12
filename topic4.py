import random
from gtts import gTTS
import os
import tempfile

menu = '''
1 - Multiply by 11
2 - Square numbers ending with 5
3 - Multiply same-first-digit-and-last-add-up-10 numbers 
4 - Multiply numbers between 10 and 20

'''

'''
response = int(input(""))

if response == 4:
    Product()
'''


def Product(count=0):
    # Variables part
    first = random.randint(11, 30)
    second = random.randint(11, 30)

    print("---> ", first, "*", second)

    correct = first * second

    # Audio part
    line = f"{first} por {second}"

    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_audio:
            audcorrect = gTTS(text=str(line), lang='es')
            audcorrect.save(temp_audio.name)

            os.system(f"afplay {temp_audio.name}")  # Play audio on system

    except Exception as e:
        print("Error:", e)
    
    answer = input("Insert your answer here ('s' to end the game, 'r' to repeat): ")

# Leaving part
    if answer.lower() == "s":
        confirm_stop = input("Are you sure you want to stop the game? (y/n): ").lower()
        if confirm_stop == "y":
            print(f"Thanks for playing! You played {count} times.")
            return  # Terminates the function without continuing
        elif confirm_stop == "n":
            Product(count)
        else:
            Product(count)  # If the player doesn't confirm stopping the game, continue

    elif answer.lower() == "r":
        try:
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_audio:
                audcorrect = gTTS(text=str(line), lang='es')
                audcorrect.save(temp_audio.name)

                os.system(f"afplay {temp_audio.name}")  # Play audio on system

        except Exception as e:
            print("Error:", e)
        
        answer = input("Insert your answer here ('s' to end the game, 'r' to repeat): ")


# Answering part
    elif answer != "stop":
        try:
            answer = int(answer)
            if answer == correct:
                corectmessage = "¡Correcto!"

                try:
                    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_audio2:
                        corectmess_audio = gTTS(text=corectmessage, lang='es')
                        corectmess_audio.save(temp_audio2.name)
                        os.system(f"afplay {temp_audio2.name}")
                except Exception as e:
                    print("Error:", e)

                print(corectmessage)

            elif answer != correct:
                incorectmessage = "Incorrecto, era " + str(correct)
                
                try:
                    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_audio3:
                        incorrect_audio = gTTS(text=incorectmessage, lang='es')
                        incorrect_audio.save(temp_audio3.name)
                        os.system(f"afplay {temp_audio3.name}")
                except Exception as e:
                    print("Error:", e)
                
                print(incorectmessage)

            else:
                pass

            # Counter part
            count += 1
            Product(count)
            
        except ValueError:
            print("Invalid input! Please enter a number or 's'.")
            Product(count)

if __name__ == '__main__':
    Product()