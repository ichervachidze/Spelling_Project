'''
Iryna Chervachidze
MET CS 521
Term Project "Spelling Program" ver.2
October 19, 2019
Word class module
'''
import os.path
from playsound import playsound


class Word:
    '''
    Class Word defines objects for spelling words.
    Provides methods:
    1.For checking the correct spelling
    3.Getting .mp3 file of the word (already downloaded)
    2.Getting url of the .mp3 recording of the word 
    (useful for future features)

    Attributes:
    word (str): the word for which an object is created
    isProper (bool): whether the word is a person's name and 
    should be capitalized, e.g. Keith; False by default
    '''

    def __init__(self, word, is_proper=False):
        self.__word = word  # correct spelling of the word
        self.url = ("https://ssl.gstatic.com/dictionary/static/"
                    "sounds/oxford/" + self.__word + "--_us_1.mp3")
        self.sound_file = os.path.join('Audio', self.__word + '.mp3')
        self.__is_proper = is_proper

    def get_word(self):
        """ Returns correct spelling of the word"""
        return self.__word

    def is_identical_to(self, other):
        '''
        Compares a given word (other) to the correct spelling (self.__word)
        Proper names need to be capitalized for correct spelling.
        Other words can be compared in lower case.

        Args:
        other (str): a word that needs spelling check
        '''
        if self.__is_proper == True:
            return True if other == self.__word else False
        else:
            return True if other.lower() == self.__word else False

    def playback_word(self):
        """ PLays .mp3 recording of the word"""
        playsound(self.sound_file)

    def get_url(self):
        """ Returns url of the .mp3 file for the given word"""
        return self.url

    def get_sound_file(self):
        """ Returns file path of the .mp3 file for the given word"""
        return self.sound_file

    def __repr__(self):
        """ Returns string representation of the object"""
        return self.__word


if __name__ == "__main__":
    ########################
    # Class Method Tests
    ########################
    chronic = Word("chronic")
    jonathan = Word("Jonathan", is_proper=True)  # proper name

    assert chronic.is_identical_to("chronic") == True, (
        f"Error: chronic is spelled correctly: "
        f"'{chronic.is_identical_to('chronic')}' but it must be True")

    assert chronic.is_identical_to("cronic") == False, (
        f"Error: cronic is spelled correctly:"
        f"'{chronic.is_identical_to('cronic')}' but it must be False")

    assert jonathan.is_identical_to("Jonathan") == True, (
        f"Error: Jonathan is spelled correctly: "
        f"'{chronic.is_identical_to('Jonathan')}' but it must be True")

    assert jonathan.is_identical_to("jonathan") == False, (
        f"Error: jonathan is spelled correctly: "
        f"'{chronic.is_identical_to('jonathan')}' but it must be False")

    print("is_identical_to() test: Success!")
