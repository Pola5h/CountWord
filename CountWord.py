file = open("/home/polash/test.txt", "r")
number_of_words = 0
for word in file:
  print("Text in the file:",word)
  word = word.strip("\n")
  words = len(word.split())
  number_of_words += words
file.close()
print("Total words in the file: ", number_of_words)
