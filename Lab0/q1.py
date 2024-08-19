
with open('example.txt' , 'r') as file:
    text = file.read()
text = text.replace(".", "")
text = text.replace(",", "")
words = text.split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
sorted_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
total_words = sum(word_freq.values())
print(f"Total number of words: {total_words}")
print("\nWords in reverse order of their frequency:")
for word, count in sorted_words:
    print(f"{word}: {count}")



