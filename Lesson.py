'''
Iryna Chervachidze
MET CS 521
Term Project "Spelling Program" ver.2
October 19, 2019
Lesson class module
'''
import os.path


class Lesson:
    """ Creates a lesson.
    Provides method for uploading word lists from .txt file.

    Attributes:
    name (str): name of the lesson that corresponds 
        to the name of the .txt file
    lesson_words (list of strings): list of all words in the lesson
    """

    def __init__(self, name):
        self.name = name
        self.lesson_words = self.load_lesson_words()

    def load_lesson_words(self):
        '''Reads and returns a list of words from a .txt file

        Returns:
        lesson_words (list of strings): all words of the given lesson
        or None if the file does not exist
        '''
        filename = (self.name + ".txt")

        # Check if the file exists
        if os.path.isfile(filename):
            # Read the contents into a list
            infile = open(filename, 'r')
            words = infile.readlines()
            infile.close()
            lesson_words = [word.strip() for word in words]
            return lesson_words
        else:
            pass


if __name__ == "__main__":

    ###############################
    # Class Method Tests
    ###############################

    new_lesson = Lesson("test")
    test_words = ['test_line1', 'test_line2', 'test_line3']

    assert new_lesson.load_lesson_words() == test_words, (
        f'Error: {new_lesson.load_lesson_words()} is not equal to '
        "['test_line1', 'test_line2', 'test_line3']")
    print("load_lesson_words() test: Success!")
