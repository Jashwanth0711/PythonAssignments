#Define a function word_count(sentence) that returns the top N frequent words (case-insensitive, ignore punctuation)
def word_count(sentence,N):
    sentence=sentence.lower()
    punctuations=".,!?;:'\"()[]{}"
    for punc in punctuations:
        sentence=sentence.replace(punc,"")
    words=sentence.split()
    freq_count={}
    for word in words:
        freq_count[word]=freq_count.get(word,0)+1
    result=[]
    for word,count in freq_count.items():
        if count==N:
            result.append((word,count))
    return result

sentence="Hello hello! How are you? You look great, hello!"
print(word_count(sentence,2))