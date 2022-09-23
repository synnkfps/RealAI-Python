import random
from . import WordData as wd
from . import Data
WordData = wd.WordData()

last_response = ''
Initiation = False
NewInput = False
UserInput = False
Advanced = False
TopicBased = True
ConditionBased = True
ProceduralBased = True
Speech = False

last_responsive_thinking = ''

topics = [] # strings
topics_thinking = [] # strings

def prepInput(input):
    # todo
    pass

def prepInput_CreateWordArray(str_put):
    wordArray = ''
    reserved = ["|", "\\", "*", "<", "\"", ":", ">", "#"]
    result = str_put

    doc_chars = []
    for c in result:
        doc_chars.append(c)

    result = ''

    for i in doc_chars:
        okay = True
        for s in reserved:
            if i == s:
                okay = False
                doc_chars.remove(i)
                i -= 1
                break
        if okay:
            # todo
            pass
    for i in doc_chars:
        result += i

    result = result.strip()
    if not result == '':
        wordArray = result.split(' ')
        for i in wordArray:
            # wordArray[i] = Util.PunctuationFix_ForInput(wordArray[i]);
            pass
        return wordArray
    #return null;

def prepInput_UpdateExistingFrequencies(wordArray):
    data = Data.getWords()
    for a in data:
        for word in wordArray:
            if WordData.getWord(a) == word:
                WordData.setFrequency(WordData.getFrequency(a) + 1)
    Data.saveWords(data)

def prepInput_AddNewWords(wordArray):
    if len(wordArray) > 0:
        data = Data.getWords()
        for word in wordArray:
            if len(data) > 0:
                found = False 
                for i in data:
                    if i == word and not word == '':
                        found = True 
                        break
                
                if not found:
                    new_wordset = WordData 
                    new_wordset.setWord(word)
                    new_wordset .setFrequency(1)
                    data.append(new_wordset) 
                else: 
                    new_wordset = WordData
                    new_wordset.setWord(word)
                    new_wordset.setFrequency(1)
                    data.append(new_wordset)
            Data.saveWords(data)
