#search engine
# you are given few sentences as a list user input dega.You have to pull out the sentences matching the query by the user
#in decreasing order of relevance
#most relevant sentence is the one with the maximum number of matching words

def match(sentence1,sentence2):
    l_q=sentence1.split()
    l_s=sentence2.split()
    sc=0

    for word1 in l_q:
        for word2 in l_s:
            if word1.lower()==word2.lower():
                sc+=1
    return sc




if __name__ == '__main__':
    print("Welcome to my serach engine")
    sentences=["Is python OK for beginners Python can be considered beginner-friendly, as it is a programming language that prioritizes readability. ","Python is not an exception - its most popular / 'traditional' implementation is called CPython and is written in C","Python so popular is that it is an easy-to-learn programming language"]
    q=input('Please enter your query')

    scores=[match(q,sentence) for sentence in sentences]
    #print(list_mw)
    sortedscentscore=[sortscent for sortscent in sorted(zip(scores,sentences),reverse=True)]
    #print(sortedscentscore)
    leng=0
    for i,v in sortedscentscore:
        if i!=0:
            leng+=1

    print(f"{leng} results")
    for score,item in sortedscentscore:
        if score!=0:
            print(item)
