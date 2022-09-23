WordDataSet = []
Words = [] # string
Frequecies = [] # ints
InputList = [] # string
OutputList = [] # string
HistoryList = [] #string
ThoughtList = [] #string
InformationBank = [] #string

def getWordDataSet(wordDataSet):
    return WordDataSet

def setWordDataSet(wordDataSet):
    WordDataSet = wordDataSet

def saveWords():
    try:
        file = open('Words.txt', 'w')
        WordsLine = ''
        for i in getWordDataSet():
            WordsLine = i + '~' # + getFrequency() + '\n'
            file.write(WordsLine)
        file.close()
    except:
        print('Error at saving words')

def getWords():
    getWordDataSet().clear() 
    Words.clear()
    Frequecies.clear()
    WordSet = ''

    file = open('Words.txt', 'w')
    try: 
        # != null
        if not not file.readlines():
            for line in file.readlines():
                if '~' in line:
                    WordSet = line.split('~')
                    Words.append(WordSet[0])
                    Frequecies.append[WordSet[1]]
        
        for i in Words:
            # WordData newset = new WordData();
    		# newset.setWord(Words.get(i));
    		# newset.setFrequency(Frequencies.get(i));
            # getWordDataSet().add(newset);
            pass 
    except:
        print('Error at getting words')
