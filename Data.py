from . import WordData as wd
import datetime 

WordData = wd.WordData()

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
        
        file.close()
    except:
        print('Error at getting words')

def savePreWords(word):
    try:
        file = open(f'Pre-{word}.txt', 'w')
        WordsLine = ''
        WordSet = len(getWordDataSet())

        i = 0 
        while i < len(getWordDataSet):
            # WordsLine = getWordDataSet().get(i).getWord() + "~" + getWordDataSet().get(i).getFrequency().toString();
            WordsLine = getWordDataSet()[i]+ '~' + WordData.getFrequency(getWordDataSet()[i])
            WordSet[i] = WordsLine
            file.write(WordsLine + '\n')
            
            i += 1 # i++
        
        file.close()
    except:
        print('Error at saving pre words')
    

def getProWords(word):
    getWordDataSet().clear()
    Words.clear()
    Frequecies.clear()
    WordSet = []
    file = open(f'Pro-{word}.txt')

    try:
        line = ''
        if not not file.readlines():
            for line in file.readlines():
                if '~' in line:
                    WordSet = line.split('~')
                    Words.append(WordSet[0])
                    Frequecies.append(WordSet[1])
            
        for i in Words:
            newset = WordData
            newset.setWord(Words[i])
            newset.setFrequency(Frequecies[i]) 
            getWordDataSet().append(newset)
        
        file.close()
    except:
        print('Error on getting pro words')

def saveInputList():
    try:
        file = open('InputList.txt', 'w')

        for i in InputList:
            file.write(InputList[i] + '\n')

        file.close()
    except:
        print('Error on saving input list')

def getInputList():
    InputList.clear()
    try:
        file = open('InputList.txt','w')
        if not not file.readlines():
            for line in file.readlines():
                if not line == '':
                    InputList.append(line)

        file.close()
    except:
        print('Error on getting input list')


def saveOutput(input):
    try:
        file = open(f'{input}.txt')
        if not not file.readlines():
            for i in OutputList:
                file.write(OutputList[i]+'\n')
        
        file.close()
    except:
        print('Error on saving output')

def getOutputList(input):
    OutputList.clear()
    file = open(f'{input}.txt')

    try:
        if not not file.readlines():
            for line in file.readlines():
                if not line == '':
                    OutputList.append(line)
            file.close()
    except:
        print('Error on getting output list')
    
def saveHistory():
    f = datetime.datetime().now()
    currentDate = str(f) 

    try:
        file = open(f'{currentDate}.txt')
        for i in HistoryList:
            file.write(HistoryList[i] + '\n')
        
        file.close()
    except:
        print('Error on saving history')

def getHistory():
    HistoryList.clear()
    f = datetime.datetime().now()
    currentDate = str(f)
    file = open(f'{currentDate}.txt')
    try:
        saveHistory()
    except:
        print('Error saving history')
    
    try:
        for line in file.readlines():
            if not line == '':
                HistoryList.append(line)
        file.close() 
    except:
        print('Error appending history')

def saveThoughts():
    f = datetime.datetime().now()
    currentDate = str(f)
    try:
        file = open(currentDate + '.txt')

        for i in ThoughtList:
            file.write(ThoughtList[i] + '\n')
        file.close()
    except:
        print('Error on saving thoughts')

def getThoughts():
    ThoughtList.clear()

    f = datetime.datetime().now()
    currentDate = str(f)
    file = open(currentDate + '.txt')

    try:
        if not not file.readlines():
            for line in file.readlines():
                if not line == '':
                    ThoughtList.append(line)
            file.close()
    except:
        print('Error on getting thoughts')        

def pullInfo(topic):
    getInputList()
    InformationBank.clear()

    if len(InputList) > 0:
        for i in InputList:
            if topic in i:
                getOutputList(i)
                if len(OutputList) > 0:
                    for b in OutputList:
                        InformationBank.append(b)
