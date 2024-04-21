def shortest_word(str):
    words = s.split()
    # s_len = [len(i) for i in words]
    # for i in range(len(s_len)):
    #     if s_len[i] == min(s_len):
    #         min_word = words[i]
    #     if s_len[i] == max(s_len):
    #         max_word = words[i]
    return (min(words, key=len), max(words, key=len))


s = "Un chasseur sachant chasser sait chasser sans son chien"
min_word, max_word = shortest_word(s)

print("Mot le plus petit:   ", min_word)
print("Mot le plus long:    ", max_word)
