#1.1

print('\n#1.1\n')

# Code here
def check_unique_characters(word):
  characters = []
  for character in word:
    if character in characters:
      return False
    characters.append(character)
  return True

# Execute
test = ['asdbasdqw', 'aaaa', 'abcdefg', '']

for entry in test:
  print(check_unique_characters(entry))
  
#1.2

print('\n#1.2\n')

# Code here
def check_is_permutation(word1, word2):
  if len(word1) != len(word2):
    return False
  return ''.join(sorted(word1)) == ''.join(sorted(word2))

# Execute

test = [('ABC', 'CAB'), ('AEF', 'DEF'), ('ASS','ASSS')]

for entry in test:
  print(check_is_permutation(*entry))