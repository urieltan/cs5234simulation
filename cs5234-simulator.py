import random
import math

random.seed(1)
token_array = ['a','b','c','d','c','c','c','a','b','b','d','a','d','a','a']
sum = 0
repeats = 100000
for i in range(repeats):
    min = 100
    min_token = ''
    for j in range(len(token_array)):
        if random.random() < min:
            min = random.random()
            min_token = token_array[j]
            min_count = 1
        elif token_array[j] == min_token:
            min_count += 1
    def f(x):
        if(x == 0):
            return 0
        return x*math.log(len(token_array)/x)

    estimate = f(min_count) - f(min_count-1)
    sum += estimate
print(sum/repeats)
