class TrieNode(object):
    #A=0, B=1, .... Z = 25.
    def __init__(self, letter, parent=None):
        self.letter = letter
        self.arr = {}
        self.payload = None
        self.isEnd = False
        self.parent = parent

    #This takes in a dictionary and appends its KVP to this Trie.
    def addDict(self, d):
        #dictTrie = TrieNode("*")
        #In this context, key is key, d[key] is payload.
        #For every key in this dictionary, I add its key to the trie node, and the value as the end payload
        for key in d.keys():
            if type(d[key]) is dict:
                subTrie = TrieNode("*", self)
                subTrie.addDict(d[key])
                #self.addDict(d[key])
                self.addWord(key, subTrie)
            #No handling for dictionaries in arrays, currently.
            else:
                self.addWord(key, d[key])

    #Word will be sent in via Text.  Letter on the node should be it's whole letter self.
    def addWord(self, word, payload=None):
        node = self
        word = word.upper()
        #Traverse through the word until all letters are nodes.
        for letter in word:
            letterVal = ord(letter) - 65

            if node.arr.get(letterVal, None):
                node = node.arr[letterVal]
            #Otherwise, we have to make a new node.
            else:
                newNode = TrieNode(letter, node)
                node.arr[letterVal] = newNode
                node = newNode
        #Mark the end of this word and append the payload.
        node.payload = payload
        node.isEnd = True

    #removeNode
    def removeNode(self):
        if self.parent:
            val = ord(self.letter) - 65
            self.parent.arr.pop(val)
        self.cleanNode()
        self.arr = {}
        self.isEnd = False

    def cleanNode(self):
        self.isEnd = False
        self.payload = None

    #want to check from the last letter up whether or not we should remove this letter
    #if any letter down the chain isn't removed, we don't want to remove the preceding one.
    def removeWord(self, word):
        node = self
        word = word.upper()

        i = 0

        #Traverse down to the last letter, then walk back up to the parent.
        while node and i < len(word):
            node = node.arr.get(ord(word[i]) - 65)
            i += 1

        if node:
            #There must be a more pythonic way to do this
            if len(node.arr.keys()) > 0:
                node.cleanNode()
            else:
                while len(node.arr.keys()) == 0:
                    node.removeNode()
                    node = node.parent
                    removed = True
            return True
        return False

    def findPayload(self, key):
        node = self
        key = key.upper()
        for letter in key:
            keyVal = ord(letter) - 65
            if node.arr.get(keyVal, None):
                node = node.arr[keyVal]
            else:
                return None
        if node.isEnd:
            return node.payload
        return None

    #A work in progress.  Print the keys in this trie, top down.
    def printWordsInTrie(self):
        for indexNode in self.arr.keys():
            child = self.arr[indexNode]
            if child:
                if not child.isEnd:
                    print(child.letter, end="")
                    child.printWordsInTrie()
                else:
                    print(self.arr[indexNode].letter)
                    if type(child.payload) is TrieNode:
                        child.printWordsInTrie()
                    else:
                        print(child.payload)
            else:
                print("We shouldn't get here.  indexNode: ", indexNode)

#Need some init function, why not main?
if __name__ == "__main__":
    node = TrieNode("*")
    node.addWord("albatross", "birdy")
    node.addWord("Alberta", "province")
    node.addWord("alpaca", "llama")
    node.addWord("antigua", "barbuda")
    node.addWord("alibaba")
    #printWordsInTrie(node)
    #print(node.findPayload("antigua"))

    #print(findPayload(node, "albatross"))


    someDict = {"abc":{"abe":"123"}, "abe":"456"}
    node.addDict(someDict)
    #printWordsInTrie(dictTrie)
    innerTrie = node.findPayload("abc")
    node.removeWord("alpaca")

    node.printWordsInTrie()
    #print(node.findPayload("antigua"))
    #print(node.findPayload("abe"))

    #if dictTrie is TrieNode:
        #print("E")
    #findPayload(dictTrie, "abc")
    #Functionality Checklist:
    #1. Must be able to write a key value pair to a trie
    #2. Must be able to retrieve the key value pair of that Trie
    #3. Must be able to write nested dictionaries into that trie, and retrieve their values
    #4. Must be able to write lists, retrieve lists.  These can be done as the payload
