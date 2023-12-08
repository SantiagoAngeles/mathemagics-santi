import random           # Mecánica principal
from gtts import gTTS   # Conversión de audio
import os               # Reproducción de audio
import tempfile         # Eliminar archivos de audio

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
            audcorrect = gTTS(text=str(line), lang='es')     # Adding audio to the question
            audcorrect = audcorrect.save("temp_audio.mp3")

    except Exception as e:
        print("Error:", e)

    os.system("afplay temp_audio.mp3")  # Play audio on system

# Leaving part
    answer = input("Insert your answer here (type 'stop' to end the game): ")

    if answer.lower() == "stop":
        confirm_stop = input("Are you sure you want to stop the game? (yes/no): ").lower()
        if confirm_stop == "yes":
            print("Thanks for playing! You played", count, "times.")
            return  # Termina la función sin continuar
        elif confirm_stop == "no":
            Product(count)
        else:
            Product(count)  # Si el jugador no confirma detener el juego, continua

# Answering part
    elif answer != "stop":
        try:
            answer = int(answer)
            if correct == answer:
                print("Correct! Well done.")
                
            else:
                print("Incorrect, the correct answer was: ", correct)
# Contador part          
            count += 1
            Product(count)
            
        except ValueError:
            print("Invalid input! Please enter a number or 'stop'.")
            Product(count)


if __name__ == '__main__':
    Product()