#!/bin/bash
#Matt McColeman 100525235
def has_no_e(word):
	if character in string(word) == 'e':
		return False
	else:
		return True
reader = open('gadsby.txt', 'r')
for line in reader:
	has_no_e(line)