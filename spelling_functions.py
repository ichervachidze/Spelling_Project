'''
Iryna Chervachidze
MET CS 521
Term Project "Spelling Program" ver.2
October 19, 2019
spelling_functions module
'''
import pickle
from Word import Word
import os.path


def read_lesson_menu():
    ''' Reads a list containing lesson names from .dat file.

    Returns: 
    lesson_menu (list of strings): a list of all lesson names
    '''
    lesson_menu_infile = open("lesson_menu.dat", "rb")
    lesson_menu = pickle.load(lesson_menu_infile)
    lesson_menu_infile.close()
    return lesson_menu


def display_main_menu(lesson_menu):
    ''' Displays lesson menu and prompts the user to select a lesson

    Args: 
    lesson_menu (list of strings): list of all lessons
    '''
    print("Choose a lesson number to practice\n"
          'or press "E" to exit the program: ')
    display_lesson_menu(lesson_menu)


def display_lesson_menu(lesson_menu):
    ''' Displays formatted menu of lessons

    Args:
    lesson_menu (list of strings): list of all lessons
    '''
    print("\n{:^25}".format("LESSON MENU:"))
    print("=" * 25)
    for i, lesson in enumerate(lesson_menu, 1):
        print(f"{i}. {lesson}")


def is_valid(user_input, number_of_lessons):
    ''' Checks if the user input is valid.
    Conditions:
    1. input must be integer only
    2. range of input must be between 1 and the last available lesson

    Args:
    user_input (str): input string by the user
    number_of_lessons (int): number of available lessons

    Returns:
    True if all check are passed successfully
    False otherwise
    '''

    # Try to convert input into integer:
    try:
        number = int(user_input)
    except ValueError:
        print(f'{user_input} is not an integer. Please enter lesson number '
              'or "E" to exit: ')
        return False

    # Check if the input number within range of lessons:
    if number < 1 or number > number_of_lessons:
        print(f"Lesson {number} does not exist. Enter lesson number between 1 "
              f'and {number_of_lessons} or "E" to exit')
        return False
    return True


def practice_lesson(lesson):
    ''' Executes the lesson, i.e. playback of words and spelling check

    Args:
    lesson (list of strings): lesson words to practice
    '''
    correct_count = 0  # initiate variable for counting correct answers
    file_not_found_count = 0  # Initiate counter of corrupt .mp3 files
    for entry in lesson:
        print("\nPlease spell the word you hear or "
              "press ENTER to hear the word again: ")

        # Create a Word class object for each of the word in the list
        # word starts with a capital letter (proper noun)
        if "A" <= entry[0] <= "Z":
            word = Word(entry, is_proper=True)
        else:
            word = Word(entry)

        # Check if the .mp3 file for this word exists
        if not os.path.isfile(word.sound_file):
            file_not_found_count += 1
            continue

        # PLay the recorded word and prompt the user to spell
        word.playback_word()
        user_word = input()

        # If the user presses "Enter", play the word again
        while user_word == '':
            word.playback_word()
            user_word = input()

        # Use .is_identical_to() method to compare spelling
        if word.is_identical_to(user_word):
            correct_count += 1
            print("Correct")
        else:
            print(f'Incorrect. Correct word is "{word}"')

    # Display the results of practice, i.e. number of
    # correctly and incorrectly spelled words
    display_results(correct_count, (len(lesson) - file_not_found_count))


def display_results(correct_count, total_count):
    """ Displays formatted results of spelling practice
    Shows the number of correctly and incorrectly spelled words

    Args:
    correct_count (int): number of correctly spelled words
    total_count (int): total number of words to practice in this lesson
    """
    print("=" * 50)  # frame for the results display
    if correct_count == total_count:
        print(" Congratulation! You spelled all words correctly!")
    else:
        print(" You spelled {} {} correctly and {} incorrectly".format(
            correct_count, 'word' if correct_count == 1 else 'words',
            total_count - correct_count))
    print("=" * 50)  # frame for the results display


def display_welcome():
    '''Displays formatted welcome message at the start of program.'''
    print("{}".format("*" * 33))
    print("{}".format("* Welcome to Spelling Practice! *"))
    print("{}".format("*" * 33))
    print()
