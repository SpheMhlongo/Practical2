#!/usr/bin/python3

def rot(string, rotation):
	letters = list(map(ord, list(string.upper())))
	new_string = ""

	while letters:
		ordinal = letters.pop(0)

		if ordinal >= 65 and ordinal <= 90:
			if ordinal >= 65 + rotation:
				ordinal -= rotation
			else:
				ordinal += rotation

		new_string += chr(ordinal)
	return new_string

print(rot("HELLO WORLD", 17))