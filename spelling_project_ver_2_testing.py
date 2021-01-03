from shuffled_lesson import ShuffledLesson
import pickle
from word_ver_2 import Word


def read_lesson_menu():
    ''' Reads a list containing lesson names from .dat file.

    Returns: 
    lesson_menu (list of strings): a list of all lesson names
    '''
    lesson_menu_infile = open("lesson_menu.dat", "rb")
    lesson_menu = pickle.load(lesson_menu_infile)
    lesson_menu_infile.close()
    return lesson_menu


lesson_menu = read_lesson_menu()
new_lesson = ShuffledLesson(lesson_menu)
print(new_lesson)
print(new_lesson.__repr__())

new_word = Word("echo")
print(new_word)
