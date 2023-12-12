consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

line = input('Enter a sample texts: ')


new = ''
i = 0
cond = False
length = len(line)

if line[0] in vowels:
    new += line + 'way'
else:
    while not cond:
        if line[i] in consonants and line[i+1] in vowels:
            new += line[i+1] + line[:i+1] + 'ay'
            cond = True
        else:
            i += 1

print(new)

