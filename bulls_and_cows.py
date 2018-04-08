from random import *


def initialise():
	dictionary_file = 'dictionary.txt'
	word_length = 4
	words = list(x.strip() for x in open(dictionary_file) if len(x.strip()) == word_length)
	valid_words = []
	for i in range(len(words)):
		if check_char_frequency(words[i]) == 1:
			valid_words.append(words[i])
	return valid_words
	

def choose_target(words):

	return words[randint(0,len(words) - 1)]

def evaluate(guess, target_word):
	bulls_cows = [0,0]
	if guess == target_word:
		return 'correct!'
	for x in range(len(guess)):
		if guess[x] in target_word:
			if guess[x] == target_word[x]:
				bulls_cows[0] += 1
			else:
				bulls_cows[1] += 1
	return bulls_cows

def check_char_frequency(s):
	dict= {}
	for n in s:
		keys = dict.keys()
		if n in keys:
			dict[n] += 1
		else:
			dict[n] = 1
	for n in s:
		if dict[n] > 1:
			return -1
	return 1


def play(valid_words, target_word):
	max_attempts = 10
	for i in range(max_attempts):
		guess = input().upper()
		if(guess in valid_words):
			ans = evaluate(guess, target_word)
			if ans == 'correct!':
				print(ans)
				return 
			else:
				print("Bulls: ", ans[0], "Cows: ", ans[1])
		else:
			print("Invalid word entered!")
	print("Maximum attempts reached!")
	print(target_word)
	return


if __name__ == '__main__':
	valid_words = initialise()
	target_word = choose_target(valid_words)
	#print(target_word)
	play(valid_words, target_word)
	

