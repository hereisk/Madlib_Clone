from gtts import gTTS
import subprocess

"""This is a Madlib clone. You are welcome to choose from three texts to play the game. Fill out the missing words and
enjoy the result. The final text will be printed and read out to you!
This program is created for educational purposes only. The texts used in the programme are not original and 
are taken from https://www.woojr.com/horror-mad-libs-for-kids/"""

GHOST = "This might sound ONE, but my TWO friend is a ghost.\nWe met in THREE grade at school while they were FOUR" \
        "the FIVE.\nTheir name is SIX and they were SEVEN years old when they died.\nNo one can EIGHT my friend but " \
        "TEN ELEVEN,and their clothes are TWELVE.\nHaving an invisible friend is THIRTEEN, but they always win at " \
        "FourTEEN and seek."

GHOST_USER_INPUT = [
    ["1. Adjective: ", "ONE"],
    ["2. Adjective: ", "TWO"],
    ["3. Noun; number: ", "THREE"],
    ["4. Verb -ing: ", "FOUR"],
    ["5. Noun; room at school: ", "FIVE"],
    ["6. Proper noun; first name: ", "SIX"],
    ["7. Noun; number: ", "SEVEN"],
    ["8. Verb: ", "EIGHT"],
    ["9. Adjective; colour: ", "NINE"],
    ["10. Adverb: ", "TEN"],
    ["11. Adjective: ", "ELEVEN"],
    ["12. Adjective: ", "TWELVE"],
    ["13. Adjective: ", "THIRTEEN"],
    ["14. Verb: ", "FourTEEN"]
]

MONSTER = "Every night before ONE to sleep, I swear I can TWO noises in my closet.\nIt sounds like a THREE FOUR is " \
          "FIVE in there and it’s so SIX!\nWhen I call my mom and SEVEN, they never EIGHT anything.\nSo I NINE off " \
          "the light and try to TEN.\nThat’s when the ELEVEN start under my TWELVE.\nIs it a monster, or something " \
          "else, like a THIRTEEN or maybe even a FourTEEN? "

MONSTER_USER_INPUT = [
    ["1. Verb: ", "ONE"],
    ["2. Verb: ", "TWO"],
    ["3. Adjective: ", "THREE"],
    ["4. Noun: ", "FOUR"],
    ["5. Verb -ing: ", "FIVE"],
    ["6. Adjective: ", "SIX"],
    ["7. Noun; relative: ", "SEVEN"],
    ["8. Verb: ", "EIGHT"],
    ["9. Verb: ", "NINE"],
    ["10. Verb: ", "TEN"],
    ["11. Plural noun: ", "ELEVEN"],
    ["12. Noun; furniture: ", "TWELVE"],
    ["13. Noun; type of monster: ", "THIRTEEN"],
    ["14. Noun; type of monster: ", "FourTEEN"]
]

ZOMBIE_PICNIC = "If zombies ONE a picnic, what would they TWO to eat?\n" \
                "Everybody knows zombies love to THREE FOUR, but did you know they also enjoy FIVE " \
                "and even SIX?\nThe best SEVEN for a zombie picnic is when the moon is EIGHT.\n" \
                "At least one zombie will bring NINE to drink, and it’s not a picnic without TEN with extra" \
                " ELEVEN on top.\nAfter eating, zombies will TWELVE THIRTEEN games like kick" \
                " FourTEEN and FIFTEEN toss."

TEST_INPUT = [['1. Verb -ed: ', 'ONE'], ['2. Verb: ', 'TWO'], ['3. Verb: ', 'THREE']]

TEST_TEXT = """If zombies ONE a picnic, what would they TWO to eat?\nEverybody knows zombies love to THREE"""

ZOMBIE_PICNIC_USER_INPUT = [
    ['1. Verb -ed: ', 'ONE'],
    ['2. Verb: ', 'TWO'],
    ['3. Verb: ', 'THREE'],
    ['4. Noun; body part: ', 'FOUR'],
    ['5. Noun; body part: ', 'FIVE'],
    ['6. Noun; body part: ', 'SIX'],
    ['7. Noun: ', 'SEVEN'],
    ['8. Adjective: ', 'EIGHT'],
    ['9. Noun; beverage: ', 'NINE'],
    ['10. Noun; body part: ', 'TEN'],
    ['11. Noun; something gross: ', 'ELEVEN'],
    ['12. Verb: ', 'TWELVE'],
    ['13. Adjective: ', 'THIRTEEN'],
    ['14. Noun; body part: ', 'FourTEEN'],
    ['15. Noun; body part: ', 'FIFTEEN']
]



def choose_text(): #this function allows to the user to choose from three given texts
  while(True):
    try: #if the selection is valid the relevant text is selected and the code exits the loop
      print("Which story would you like to choose?\n1. Zombie Picnic.\n2. Is There a Monster in My Room?\n3. My Best"
            "Friend Is a Ghost!")
      selection = int(input("Please choose the number of the story: "))
      if selection == 1:
          text = ZOMBIE_PICNIC
          user_input = ZOMBIE_PICNIC_USER_INPUT
          break
      elif selection == 2:
          text = MONSTER
          user_input = MONSTER_USER_INPUT
          break
      elif selection == 3:
          text = GHOST
          user_input = GHOST_USER_INPUT
          break
      elif selection == 0: #if the user chooses to close the program they need to select 0
          print("Thanks for playing!")
          _exit(0)
    except: #this is to deal with invalid selection
          print("\nPlease choose a valid selection or enter 0 to exit\n")
  return text, user_input


def say_it(text): #the function is to create an audio file using gTTS module. The file is saved and played locally
    tts = gTTS(text=text, lang='en')
    tts.save('tts.wav')
    subprocess.call(["afplay", "tts.wav"])


def main(): #the main function to operate the program
    while True:
        selected_game = choose_text()
        text, user_input = selected_game
        for question, placeholder in user_input:
            user_answer = input(question)
            text = text.replace(placeholder, user_answer)
        print(" ")
        print(text)
        print(" ")
        say_it(text)


if __name__ == '__main__':
    main()
