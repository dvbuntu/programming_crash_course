import string

plain = 'Not going to be that easy :)'

shift = 0

def caesar(plain, shift=1):
    key = {l:string.ascii_lowercase[(i+shift) % 26] for i,l in enumerate(string.ascii_lowercase)}
    output = ''
    for l in plain:
        if l in key:
            output += key[l]
        else:
            output += l
    return output

result = caesar(plain.lower(), shift)

with open('caesar.txt', 'w') as f:
    f.write(result)

