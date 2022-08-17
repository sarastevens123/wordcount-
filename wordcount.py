"""Count words in file."""


def tokenize(file):
  """Returns a list of words from the file"""
  open_file = open(file)
  list_of_words = []
  for line in open_file:
    line = line.rstrip()
    words = line.split(' ')

    for word in words:
      if not word:
        continue
      if word[-1] in ',.?!)*':
        word = word[:-1]
      elif word[0] in ',.?!)*':
        word = word[1:]
      
      list_of_words.append(word)

  open_file.close()
  return list_of_words
#print(tokenize('test.txt'))


def count_words(words):
  """ Takes in a lists of words and returns a dictionary of each string and number of occurrence"""
  word_count = {}
  for word in words:
      if word not in word_count:
          word_count[word] = 1
      else:
          word_count[word] += 1
  return word_count



#print(count_words(tokenize('test.txt')))


            

def print_word_count(word_count):
  for key, value in word_count.items():
    print(f"{key} {value}")
#print_word_count(count_words(tokenize('test.txt')))


#I need to fix the code to accept upper and lower case letters as the same in the count

