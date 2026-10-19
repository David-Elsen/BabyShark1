"""----------------------------------------------------------------
Name:       your name
Assignment: Lab - Baby Shark
Course:     CS 1430, Section X, Fall 2026
Purpose:    This program is designed to be practice for Python
            functions

Input: None

Output: The sound Baby Shark, with three verses:
        Baby Shark,
        doo-doo-doo-do-do-do-do *3
        Baby Shark!
        Mommy Shark,
        doo-doo-doo-do-do-do-do *3
        Mommy Shark!
        Daddy Shark,
        doo-doo-doo-do-do-do-do *3
        Daddy Shark!
----------------------------------------------------------------"""

##############
# CONSTANTS
##############
DOO = "doo-doo-doo-do-do-do-do"
REPEAT = 3


def verse(who):
    for _ in range(REPEAT):
        print(f"{who} Shark,")
        print(DOO)
    print(f"{who} Shark!")


def main():
    verse("Baby")
    verse("Mommy")
    verse("Daddy")


if __name__ == "__main__":
    main()
