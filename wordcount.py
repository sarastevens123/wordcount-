"""Count words in file."""


# put your code here.
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
print(tokenize('test.txt'))





def count_words(words):
  """ Takes in a lists of words and returns a dictionary of each string and number of occurrence"""
  word_count = {}
  for word in words:
      if word not in word_count:
          word_count[word] = 1
      else:
          word_count[word] += 1
  return word_count



print(count_words(tokenize('test.txt')))

#     word_count = {}

#         for word in words:
          
#             print(word)
#             if not word:
#               continue

#             if word[-1] in ',.?!)*':
#                 word = word[:-1]
#             elif word[0] in ',.?!)*':
#                 word = word[1:]
            
#             word = word.upper()
            
#             if word not in word_count:
#                 word_count[word]= 1
#             elif word in word_count:
#                 word_count[word] += 1
    
#     for key, value in word_count.items():
#       print(f"{key} {value}")
#     open_file.close()

# print(count_words('twain.txt'))