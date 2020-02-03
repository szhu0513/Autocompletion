from urllib.request import urlopen

with open("word_list.csv") as f:
    for l in f:
        index, word, wordtype, frequency, score = l.split("\t")
        #print("http://192.168.1.5:8080/insert?word=" + word)
        urlopen("http://192.168.1.5:8080/insert?word=" + word.strip())
