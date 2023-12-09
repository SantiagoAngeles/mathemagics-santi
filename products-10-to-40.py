import random
from gtts import gTTS
import os
import tempfile

def Product(count=0):
    # Variables part
    first = random.randint(10, 30)
    second = random.randint(10, 30)

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

    # Leaving part
    answer = input("Insert your answer here (type 'stop' to end the game): ")

    if answer.lower() == "stop":
        confirm_stop = input("Are you sure you want to stop the game? (yes/no): ").lower()
        if confirm_stop == "yes":
            print(f"Thanks for playing! You played {count} times.")
            return  # Terminates the function without continuing
        elif confirm_stop == "no":
            Product(count)
        else:
            Product(count)  # If the player doesn't confirm stopping the game, continue

    # Answering part
    elif answer != "stop":
        try:
            answer = int(answer)
            if answer == correct:
                corectmess = "Correcto, !Bien hecho!"
                try:
                    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_audio2:
                        corectmess_audio = gTTS(text=corectmess, lang='es')
                        corectmess_audio.save(temp_audio2.name)
                        os.system(f"afplay {temp_audio2.name}")

                except Exception as e:
                    print("Error:", e)

                print(corectmess)
                
            else:
                print("Incorrect, the correct answer was: ", correct)
            # Counter part
            count += 1
            Product(count)
            
        except ValueError:
            print("Invalid input! Please enter a number or 'stop'.")
            Product(count)

if __name__ == '__main__':
    Product()