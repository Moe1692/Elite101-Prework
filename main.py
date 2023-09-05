def printList(ops):
  for i in range(len(ops)):
    print(f'{i+1}. {ops[i]}')

print('Welcome to GhatCPT.')
name = input('What\'s you\'re name? ')
age = input('How old are you, ' + name + '? ')
print(f'You\'re name is {name} and you are {age} years old.')
print('How can I help you, ' + name + '?')
options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Exit']


while True:
  printList(options)
  selected = input('Enter an option selection based on number: ')
  if selected == '5':
    print('See you later, ' + name + '!')
    break