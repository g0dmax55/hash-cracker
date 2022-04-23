#!/usr/bin/env python3

import hashlib

#coded by g0dmax55 

count = 0

hashed = ("bed4efa1d4fdbd954bd3705d6a2a78270ec9a52ecfbfb010c61862af5c76af1761ffeb1aef6aca1bf5d02b3781aa854fabd2b69c790de74e17ecfec3cb6ac4bf")
wordlist = ("darkc0de.txt")

try:
	pass_file = open (wordlist, "r")
except:
	quit()

for word in pass_file:
	enc_wrd = word.encode("utf-8")
	digest = hashlib.sha512(enc_wrd.strip()).hexdigest()

	print(digest)
	print(hashed)

	if digest == hashed:
		print()
		print("PASSWORD FOUND !")
		print("PASSWORD IS " + word)
		count = 1
		break

if count == 0:
	print()
	print("PASSWORD IS NOT IN THE LIST !")
