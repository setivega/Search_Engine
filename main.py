from random import *

f = open("input.txt", "r")

words = {}

prevWord = "."
for line in f:
  for word in line.split():
    if word.endswith("."):
      word = word[:-1]
      if word in words:
        words[prevWord].append(word)
        prevWord = "."
      else:
        words[prevWord] = [word]
        prevWord = word
    elif prevWord in words:
      words[prevWord].append(word)
      prevWord = word
    else:
      words[prevWord] = [word]
      prevWord = word
    print(word)

print(words)


text = [line.split() for line in open("input.txt")]
wordsArray = text[0]

wordBefore = wordsArray[randint(0,len(wordsArray)-1)]

sentence = wordBefore

# print("First Word:", wordBefore)
print("\n")

for key in words:
  if len(sentence) < 140:
    if wordBefore in words:
      values = words[wordBefore]
      nextWord = values[randint(0,len(values)-1)]
      sentence += " " + nextWord
      wordBefore = nextWord
    else:
      wordBefore = "."

print("Sentence:",sentence)
print(len(sentence))
