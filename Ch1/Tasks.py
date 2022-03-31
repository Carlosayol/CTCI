#1.1

test = ['asdbasdqw', 'aaaa', 'abcdefg', '']

# Code here
def check_unique_characters(word):
  characters = []
  for character in word:
    if character in characters:
      return False
    else:
      characters.append(character)
  return True

for word in test:
  print(check_unique_characters(word))
  




