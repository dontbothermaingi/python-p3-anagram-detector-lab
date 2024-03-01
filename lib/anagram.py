# your code goes here!

class Anagram:
    def __init__(self,word):
        self.word = word

    
    def match(self,word_list):
        anagrams = []
        for w in word_list:
            if self.is_anagram(w):
                anagrams.append(w)
        return anagrams
    

    def is_anagram(self,word):
        if len(word) != len(self.word):
            return False 
        return sorted(word.lower()) == sorted(self.word.lower())