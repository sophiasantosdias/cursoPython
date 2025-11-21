# Maior e menor valor em Tupla
from random import randint
nums = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: {nums[0]}, {nums[1]}, {nums[2]}, {nums[3]}, {nums[4]}')
print(f'O Maior número sorteado foi: {sorted(nums)[-1]}')
print(f'O Menor número sorteado foi: {sorted(nums)[0]}')
