import random
import math



token_array = ['a','b','c','d','c','c','c','a','b','b','d','a','d','a','a'] 
m = len(token_array)
sum = 0
repeats = 10
for i in range(repeats):
    minimum = 100
    min_token = ''
    min_count = 0
    for j in range(len(token_array)):
        new_random = random.random()
        if new_random < minimum:
            minimum = new_random
            min_token = token_array[j]
            min_count = 1
        elif token_array[j] == min_token:
            min_count += 1
    def f(x):
        if(x == 0):
            return 0
        return - x*math.log(x/m)

    estimate = f(min_count) - f(min_count-1)
    sum += estimate
print(sum/repeats)
