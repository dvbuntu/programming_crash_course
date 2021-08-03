# text is stored in a local file
filename = 'caesar.txt'

# read the text into a string and close the file
f = open(filename, 'r')
cipher = f.read()
f.close()

# or copy to a string
# cipher = 'mubsecu je jxu kq ydjuwhqjyed mehaixef!  edu tuvydyjyed ev q vkdsjyed v sedjydkeki qj q yi:  veh uluho ufiybed whuqjuh jxqd puhe, jxuhu unyiji q tubjq whuqjuh jxqd puhe iksx jxqj yv jxu qriebkju lqbku ev n cydki q yi buii jxqd tubjq, jxud jxu qriebkju lqbku ev v qj n cydki v qj q yi buii jxqd ufiybed.'

# check it
print(cipher)

# setup a dictionary to store count of each letter
counts = dict()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    counts[letter] = 0 # initial zero

# make sure letters are all lowercase
cipher_low = cipher.lower()

# iterate through letters to count
for letter in cipher_low:
    # check if it's actually a letter
    if letter in alphabet: 
        counts[letter] += 1

# take a quick look at counts
print(counts)

# Let's make a plot to see if this is clearer
import matplotlib.pyplot as plt
plt.ion()  # make interactive

# assign letters to integers for plotting
positions = list(range(len(alphabet)))

# extract the heights into a list (in alphabetical order)
heights = [counts[letter] for letter in alphabet]

# do the barplot
plt.bar(positions, heights)

# fix the x-axis
plt.xticks(positions, alphabet)

# add more information
plt.ylabel('Letter Count')
plt.title('Count of Cipher Characters')

# 'u' is most common, maybe that maps to 'e'?
# What's the shift between these?
shift = alphabet.index('u') - alphabet.index('e')

# make a function to shift the letters
def unshift(letters, shift=1):
    # make a dictionary mapping from old to new
    key = dict()
    for i in range(len(alphabet)):
        key[alphabet[i]] = alphabet[(i+shift) % 26]
    # initialize string output
    output = ''
    for l in letters:
        # check if current character is actually a letter and apply shift
        if l in key:
            output += key[l]
        else:
            output += l
    return output

# reverse the shift
plain = unshift(cipher, -shift)

# does this look right?  Yes!
print(plain)

