import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = functools.reduce(accum, numbers)

print('Result1: ',result)

result2 = functools.reduce(lambda counter,item: counter + item, numbers)

print('Result2: ',result2)