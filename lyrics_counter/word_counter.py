from wk6_t2_lyrics import lyrics

lyrics = lyrics.lower()
lyrics = lyrics.replace("(", "")
lyrics = lyrics.replace(")", "")
lyrics = lyrics.replace(",", "")
lyrics = lyrics.replace("\n", " ")

words = lyrics.split(" ")

word_count = {}

for word in words:
    if(word != ""):
        if(word in word_count):
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

most_common = {"count": 0}

for key in word_count:
    if(word_count[key] > most_common["count"]):
        most_common = {"word": key, "count": word_count[key]}

print(f'Most common word: "{most_common["word"]}". Uses: {most_common["count"]}')
