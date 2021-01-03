'''
Iryna Chervachidze
MET CS 521
Term Project "Spelling Program" ver.2
October 19, 2019
spelling_main_program module: RUN THIS MODULE TO START THE PROGRAM
'''
'''
NOTE: This program uses audio playback. You need to use speakers to be able
to hear words played back to you. Before running this program make sure that
the sound level is acceptable.
'''

import sys
import spelling_functions as sf
from ShuffledLesson import ShuffledLesson
from Lesson import Lesson

######################################
# Main Program
######################################

# Display welcome message
sf.display_welcome()
# Load lesson menu from the file
lesson_menu = sf.read_lesson_menu()
# Display lesson menu and prompt the user to choose lesson
sf.display_main_menu(lesson_menu)

# Start main menu loop:
while True:
    user_input = input()
    # If the user chooses "E" or "e", exit the program
    if user_input.lower() == "e":
        print("Exiting the program...Bye!")
        sys.exit()
    # If the user input is valid, cast lesson number into integer
    if sf.is_valid(user_input, len(lesson_menu)):
        lesson_number = int(user_input)

        # For practicing random words (lesson 1), create an instance
        # of ShuffledLesson:
        if lesson_number == 1:
            current_lesson = ShuffledLesson(lesson_menu)

        # For all other lessons, create and instance of Lesson:
        else:
            current_lesson = Lesson(lesson_menu[lesson_number - 1])

        # If lesson words file is not found
        if not current_lesson.lesson_words:
            print('Sorry! '
                  f'Lesson "{lesson_menu[lesson_number - 1]}" is not found!\n')
            # Go back to the main menu
            sf.display_main_menu(lesson_menu)
            continue

        # If lesson file exists, start lesson practice loop
        while True:
            print(f"\nWelcome to LESSON {lesson_number}!"
                  f" {lesson_menu[lesson_number - 1]}")
            sf.practice_lesson(current_lesson.lesson_words)

            # Continue practicing same lesson or
            # break out of the practice loop to exit to main menu
            print('\nPress "A" to practice again '
                  "or any other key to exit to main menu: ")
            if input().lower() == "a":
                continue
            else:
                # Display lesson menu and prompt to choose lesson number
                sf.display_main_menu(lesson_menu)
                break
