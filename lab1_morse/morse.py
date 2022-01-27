import argparse
import sys
import os

morse_dict ={
            "a": ".- ",
            "b": "-... ",
            "c": "-.-. ",
            "d": "-.. ",
            "e": ". ",
            "f": "..-. ",
            "g": "--. ",
            "h": ".... ",
            "i": ".. ",
            "j": ".--- ",
            "k": "-.- ",
            "l": ".-.. ",
            "m": "-- ",
            "n": "-. ",
            "o": "--- ",
            "p": ".--. ",
            "q": "--.- ",
            "r": ".-. ",
            "s": "... ",
            "t": "- ",
            "u": "..- ",
            "v": "...- ",
            "w": ".-- ",
            "x": "-..- ",
            "y": "-.-- ",
            "z": "--.. ",
            " ": "/ "
        }


def morse(file_handle):
    message_in_morse = ''
    for line in file_handle:
        line = line.strip().lower()
        for letter in line:
            if letter in morse_dict.keys():
                if len(message_in_morse) != 0 and message_in_morse[-2] == "/" and morse_dict[letter] == "/ ":
                    continue
                else:
                    message_in_morse += morse_dict[letter]
        message_in_morse += '\n'
    return message_in_morse.strip()


def translate(path):
    try:
        with open(path, mode="r", encoding="utf-8") as file_handle:
            result = morse(file_handle)
            return result
    except FileNotFoundError as err:
        return "[-] File not found!"


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args(arguments[1:])

    if args.file is not None:
        print(translate(args.file), end="")
        return

if __name__=='__main__':
    main(sys.argv)
