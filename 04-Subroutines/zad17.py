from tkinter import E


def letter_counter(letter, str):
    counter=0
    for i in str:
        if i==letter:
            counter+=1
    print(f"Letter {letter} appers in '{str}' {counter} times")

letter_counter("e", "You never get a second chance to make a first impression")