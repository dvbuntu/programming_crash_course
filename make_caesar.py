import string

plain = 'Welcome to the UA Integration Workshop!  One definition of a function f continuous at a is:  For every epsilon greater than zero, there exists a delta greater than zero such that if the absolute value of x minus a is less than delta, then the absolute value of f at x minus f at a is less than epsilon.'

shift = 42

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

