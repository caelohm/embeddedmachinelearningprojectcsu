from os import walk
import re

f = []

'''
for (dirpath, dirnames, filenames) in walk('C:\\Users\\Cael\\Documents\\College\\RYM Project\\Finished\\Electronic'):
    f += filenames
'''

file = open('releases_per_genre200up.txt', 'r')
Lines = file.readlines()

for line in Lines:
    f.append(line.replace('\n', ''))

squish = ''
num_alb = []

print(f)

for tem in f:
    num_alb.append(int(re.search('\d+', tem).group(0)))
    squish += tem + '_'

num_alb.sort(reverse=True)

file.close()
file = open('releases_per_genre_sorted.txt', 'w')

for gen in num_alb:
    file.write(re.search(str(gen) + '[\s\D-]+', squish).group(0)[:-1] + '\n')
