openers_and_closers = {
  '(': ')'
}

hola = [[1,2],[1,4]]

print(len(hola))
if hola:
  print('1111')

hola.append('1')
hola.append('2')
hola.append('3')
hola.pop()
print(hola[-1])
print('{' in openers_and_closers.keys())