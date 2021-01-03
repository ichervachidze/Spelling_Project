'''
Iryna Chervachidze
MET CS 521
Term Project "Spelling Program" ver.2
October 19, 2019
ShuffledLesson class module
'''
from Lesson import Lesson
import random


class ShuffledLesson:
    """ Creates a lesson of 10 random words

    Provides methods for:
    1. Loading all available words
    2. Shuffling all words and selecting first 10 words

    Attributes:
    lesson_menu (list of strings): list of all lesson names
    lesson_words (list of strings): list of 10 randomized words
    """

    def __init__(self, lesson_menu):
        self.lesson_menu = lesson_menu
        self.lesson_words = self.__shuffle_words()

    def __shuffle_words(self):
        ''' Shuffles words in a list and returns the first 10 shuffled words.

        Returns:
        all_words (list of strings): a list of 10 words
        '''
        all_words = self.load_all_words()
        random.shuffle(all_words)
        return all_words[:10]

    def load_all_words(self):
        ''' Loads words from all available lessons into a list.

        Returns:
        all_words (list of strings): list of all words
        '''
        all_words = []
        # Load words from all lessons except lesson #0, which is
        # practicing 10 random words
        for lesson in self.lesson_menu[1:]:
            lesson_words = Lesson(lesson).lesson_words
            if not lesson_words:
                continue
            all_words += lesson_words
        return all_words

    def __str__(self):
        """ Return string representation of the ShuffledLesson object"""
        to_string = ''
        for word in self.lesson_words:
            to_string += word + " "
        return to_string

    def __repr__(self):
        """ Returns the shuffled list of 10 words"""
        return self.lesson_words
