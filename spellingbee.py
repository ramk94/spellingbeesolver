# Ram Bhattarai
# Spelling Bee Solver

# Imports
import re
import pprint
import argparse


class SpellingBeeSolver:

    def __init__(self):
        """
        Load Dictionary text
        Remove words that are less than 4 characters
        Appends the word that is greater than or equal to 4 characters
        """
        self.dictionary_words = []
        with open("words.txt") as words:
            words_in_dictionary = words.readlines()

        for word in words_in_dictionary:
            if len(word) > 4:
                self.dictionary_words.append(word)

    def solve_the_puzzle(self, puzzle_letters, important_letter):
        """
        :param important_letter: The letter that must be present in the word
        :param puzzle_letters: Provide the puzzle string to solve
        :return: the list of words that are the potential answers for spelling bee
        """
        words_with_important_letter = []
        pattern = "^[" + puzzle_letters + "]*$"

        for string in self.dictionary_words:
            string = string.upper()
            if important_letter in string:
                if re.search(pattern, string):
                    words_with_important_letter.append(string.strip("\n"))

        return words_with_important_letter


puzzle = SpellingBeeSolver()

parser = argparse.ArgumentParser()
parser.add_argument("puzzle", help="Puzzle string of the day from spelling bee")
parser.add_argument("special_char", help="The middle character from spelling bee")
args = parser.parse_args()

pprint.pprint(puzzle.solve_the_puzzle(args.puzzle, args.special_char))
