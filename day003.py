number = [0,1,2,3]
for i in  range(len(number)-1, -1, -1):
   print(number[i], end='')

print()


guess_me = 7
number = 1
while True:
   if number < guess_me:
      print('too low')
   elif number > guess_me:
      print('opps')
   elif number == guess_me:
      print('found it!')
      break
   number += 1


print()


guess_me = 5
for number in range(10):
      if number < guess_me:
         print('too low')
      elif number == guess_me:
         print('found it')
      elif number > guess_me:
         print('opps')
         break
