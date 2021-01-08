# Spelling Practice Project (in Python 3)

**Note: This program uses .mp3 recordings of words. The user needs speakers/headphones to be able to hear the recordings. Please make sure that the speaker sound level is acceptable before running the program!
Note2: Module spelling_main_program runs the program.**

## Brief Description
This program helps practice spelling words. The user can choose from the main menu options or press “E”/“e” to exit the program. Main menu has following options:
1.	Practice 10 Random Words
2.	Words Ending in -TURE
3.	Words Ending in -US
4.	Words with -GU-
5.	Words with -CH- 

This main menu is stored in a list in a .dat file. As the user starts the program, it unpickles the .dat file and uploads the above menu. I chose to do it this way rather than hard-code it because in the future when I add more features to the program, such add/delete a lesson, it will be easy to update this menu. The program will then read the updated menu and no further changes to the program will be required.
The user can choose any lesson from the menu. Words for each lesson are stored in separate .txt files. When the user chooses a lesson, the program creates an instance of the Lesson class. That lesson object uploads the words necessary for the lesson.
If the user chooses lesson 1, Practice 10 Random Words, the program creates an instance of a separate class ShuffledLesson. ShuffledLesson object then uploads all the available words from their files, shuffles them, and picks the first 10 words for the user to practice.
<br>
<br>
Once the user chooses one of the menu options, he hears a spelling word played back to him. He is then prompted to type this word and immediately gets a feedback whether the spelled word is correctly spelled or not. At the end of the lesson, the user can see the statistics for the lesson: the number of correctly spelled words and incorrectly spelled words. The user has a choice to continue practicing the same lesson or return to the main menu.
<br>
<br>
There are several validation points in the program. The program validates user’s input and prompts the user to re-enter the choice if the input fails the checks. The program also checks if the .txt files containing words as well as .mp3 files containing word recordings exist. If .txt file does not exist, then the lesson cannot load, but the program does not crash. It informs the user that the lesson file was not found and prompts him to enter again from the menu. If an .mp3 file of the recorded word fails to load, the program skips that word without informing the user. The total count of words as displayed at the end of the spelling practice is adjusted for words whose recordings failed to load.

## How to Run
The program contains five .py modules: spelling_main_program,  spelling_functions, Word, Lesson, and ShuffledLesson modules. Module spelling_main_program runs the program.


## Third Party Module Playsound
To playback the words, I use a module called “playsound.” Documentation for playsound and instructions how to download can be found here:<br>
[````https://pypi.org/project/playsound/````](https://pypi.org/project/playsound/)<br>
I only need this module to play .mp3 files of the words which I need for the lessons.
According to the author of this module, playsound is supposed to work with all platforms.

