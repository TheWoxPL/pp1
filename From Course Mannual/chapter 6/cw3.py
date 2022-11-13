def count(word, to_find):
    count = 0
    for letter in word:
        if letter == to_find:
            count = count + 1
    print(count)

count("banan", "a")
