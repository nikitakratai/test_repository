defi

%% LISTS
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')

%% enumerate() function.
for i, v in enumerate(['first', 'second', 'third', 'fourth']):
  print(i, v)

%%
for num in range(2, 10):
  if num % 2 == 0:
  print("Found an even number", num)
  continue
print("Found a number", num)
