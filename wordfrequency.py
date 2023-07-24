word_freq = {}

filename = 'sometext-1.txt'

with open (filename,'r') as file:
    for line in file:
        
        line_split = line.split()

        for word in line_split:

            word_freq[word] = word_freq.get(word, 0) + 1

for word, freq in word_freq.items():
    print(f'(word): (freq)')
    