import array
a = array.array('i', [1, 2, 3, 4, 5, 6])
print(a)
words = ['apple', 'orange', 'mango', 'banana', 'apple']

word_count ={}

for word in words:
    
    word_count[word] = word_count.get(word, 0) + 1
    
print(word_count)