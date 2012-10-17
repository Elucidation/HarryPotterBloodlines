from random import choice, random

softPhonemes = ["a","e","i","o","u","oo","oi","ou","aw","ar","er"]
hardPhonemes = ["b","c","d", "f","g","h","j","k","l","m","n","p","qu","r","s","t","v","x","w","y","z","sh","wh","ch","th","ng","s",]

consonents = "bcdfghjklmnpqrstvwxyz" # includes y
vowels = "aeiou" # not including y

def randShortName():
    " Returns 3 letter word w/ consonent+vowel+consonent format"
    return (choice(consonents)+ choice(vowels) + choice(consonents)).capitalize()


def randName():
	""" Returns word using phonemes """
	name = choice(hardPhonemes).capitalize() + choice(softPhonemes) if random() > 0.5 else choice(softPhonemes).capitalize() + choice(hardPhonemes)
	for x in xrange(1+int(random()*1)):
		name += choice(hardPhonemes) + choice(softPhonemes) if random() > 0.5 else choice(softPhonemes) + choice(hardPhonemes)
	return name