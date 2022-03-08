# this is a program to convert the given text into pig-latin

vowels = ['a', 'e', 'i', 'o', 'u']
new_list = []
sentence = input("Enter a string to conver it into pig-latin : ")
sentence = sentence.lower()
sentence = sentence.split()
print(sentence)

for word in sentence:
    if word[0] in vowels:
        new_list.append(word+"hay")
    else:
        new_list.append(word+"ay")

print(new_list)
