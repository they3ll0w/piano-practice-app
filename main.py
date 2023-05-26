from tkinter import *
import random

# Constant lists

MAJOR_SHARP = ["C", "G", "D", "A", "E", "B", "F sharp", "C sharp"]
MAJOR_FLAT = ["F", "B flat", "E flat", "A flat", "D flat", "G flat", "C flat"]
MAJORS = [MAJOR_FLAT, MAJOR_SHARP]

MINOR_SHARP = ["A", "E", "B", "F sharp", "C sharp", "G sharp", "B sharp"]
MINOR_FLAT = ["B", "G", "C", "F", "B flat", "D flat", "A flat"]
MINORS = [MINOR_FLAT, MINOR_SHARP]

MAJOR_SCALES = ["major", "separated by a third", "separated by a sixth", "separated by a tenth",
                    "contrary motion", "chromatic scale", "octaves"]
MAJOR_OCTAVES = ["four keys", "dominant seven chords", "dominant seven seperated"]
MAJOR_ARPEGGIO = ["four key form " + str(random.randint(0, 2))
    , "dominant seven" + str(random.randint(0, 3))]
MAJOR_TESTS = [MAJOR_ARPEGGIO, MAJOR_OCTAVES, MAJOR_SCALES]

MINOR_SCALES = ["harmonic", "melodic", "contrary motion"]
MINOR_OCTAVES = ["four keys", "diminished seven chords", "diminished seven separated"]
MINOR_ARPEGGIO = ["four key form inversion " + str(random.randint(0, 2))
    , "diminished seven inversion " + str(random.randint(0, 3))]
MINOR_TESTS = [MINOR_ARPEGGIO, MINOR_SCALES, MINOR_OCTAVES]

MAJOR_MINOR = ["major", "minor"]

# Functions

# choose_majororminor() returns randomly one of "major" or "minor"
def choose_majororminor():
    choice = random.choice(MAJOR_MINOR)
    return choice


def choose_key(major_or_minor):
    if major_or_minor == "major":
        f_or_s = random.choice(MAJORS)
        key = random.choice(f_or_s)
        return (key)
    else:
        f_or_s = random.choice(MINORS)
        key = random.choice(f_or_s)
        return (key)


def choose_tests(major_or_minor):
    test_list = MINOR_TESTS
    if major_or_minor == "major":
        test_list = MAJOR_TESTS
    whichtest = random.choice(test_list)
    the_test = random.choice(whichtest)
    return (the_test)

def click():
    major_minor = choose_majororminor()
    key = choose_key(major_minor)
    test = choose_tests(major_minor)
    to_print = to_print = "Perform " + str(key) + " " + str(major_minor) + "," + " in " + str(test)
    label.config(text=to_print)


window = Tk()
window.title("Application")
window.geometry("420x210")
major_minor = choose_majororminor()
key = choose_key(choose_majororminor())
test = choose_tests(choose_majororminor())
to_print = to_print = "Perform " + str(key) + " " + str(major_minor) + "," + " in " + str(test)

# Button
button = Button(window, text="Reset the skill", command=click)
button.pack()

#label
label= Label(window)
label.config(text=to_print, font = ("Times New Roman",12))
label.pack()


window.mainloop()