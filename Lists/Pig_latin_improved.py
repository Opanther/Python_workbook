

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
punctuation = [',', '.', '?', '!']

line = input('Enter a sample text: ').lower()

punctuation_positions = []

for j in line:
    if j in punctuation:
        punctuation_positions.append(line.index(j))

punc = ''
for loc in punctuation_positions:
    punc += line[loc]

if line[0] in vowels:
    new_text = line + 'way' + punc
else:
    new_text = ''
    i = 0
    cond = False

    while not cond and i < len(line) - 1:
        if line[i] in consonants and line[i + 1] in vowels:
            new_word = line[i + 1:] + line[:i + 1] + 'ay' + punc
            new_text += new_word
            new_text = new_text.capitalize()
            cond = True
        else:
            i += 1

print(new_text)
