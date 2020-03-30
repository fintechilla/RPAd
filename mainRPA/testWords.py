import Wordy as Word

line = "FIA; Fiber Connect Plus; Voice"
print(line)
separator = ";"
word = Word()
words = word.splitAndRemoveLeadBlanks(line, separator)
# temp = word.splitAndRemoveLeadBlanks()
# print(temp)
print("hello")
print(words)
