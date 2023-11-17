with open("story.txt","r") as f:
    story = f.read()

words = set()
start_word = -1

target_begin = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == "<":
        start_word = i

    if char == target_end and start_word != -1:
        word = story[start_word: i+1]
        words.add(word)
        start_word = -1

answers = {}
for word in words:
    answer = input("Enter a word" + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
    

print(story)