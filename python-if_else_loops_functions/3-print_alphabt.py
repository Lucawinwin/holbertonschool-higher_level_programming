#!/usr/bin/python3

for letter in range(97, 123):  # ASCII values for 'a' to 'z'
    if letter != 101 and letter != 113:  # Skip 'e' (ASCII 101) and 'q' (ASCII 113)
        print(chr(letter), end="")

