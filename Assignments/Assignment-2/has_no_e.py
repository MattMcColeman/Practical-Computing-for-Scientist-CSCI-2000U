#!/bin/bash
#Matt McColeman 100525235
def has_no_e(line):
	for character in line:
		if (character == "e"):
			return False
	else:
		return True
reader = open('gadsby_stripped.txt', 'r')
for line in reader:
	has_no_e(line)