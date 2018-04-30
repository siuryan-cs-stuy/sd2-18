f = open('book.txt', 'r')

contents = f.read()
words = contents.split()
f.close()

def freq(word):
    return len([ x for x in words if x.lower() == word.lower() ])

def freq_group(list_words):
    return reduce(lambda a, b: a + freq(b) if isinstance(a, int) else freq(a) + freq(b), list_words)

def most_freq():
    return reduce( lambda a, b: a if a > freq(b) else freq(b), words)

print "Frequency of macaroon:", freq("macaroon")
print "Frequency of how:", freq("how")
print "Frequency of a:", freq("a")
print "Frequency of (macaroon, how, a):", freq_group(["macaroon", "how", "a"])

freq_word = most_freq()
print "Most frequent word:", freq_word, "(" + str(freq(freq_word)) + ")"
