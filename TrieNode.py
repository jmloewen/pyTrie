#This Python implementation of a Trie is made to store items at the end of each Trie branch.
#Primary usage is to convert dictionary key value pairs into a Trie structure.
#Cannot currently handle multiple equal keys.  New key will overwrite the old, as is.
#Current implementation of the descendant "trie" nodes creates a dictionary to be filled with single-letter
#KVP's, rather than allocate 26 arrays filled with None.  Will implement alternative for arrays rather than dictsself.

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
    def addWord(self, word, payload):
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

    def removeNode(self):
        #If we're calling this, we want to remove the node.
        if self.parent:
            val = ord(self.letter) - 65
            self.parent.arr[val] = None

        self.arr = {}

        return self.payload
        '''
    #In: A word to remove from this trienode.
    def removeWord(self, word):
        removed = False
        #Dig to the end of the word, remove on our way back up
        if len(word) == 1:
            #if more than 1 child, then don't delete the node.
            if len(self.arr.keys()) > 1:
                self.payload = None
                self.isEnd = False
                return False
            #Remove this node
            else:
                self.removeNode()
                return True
        else:
            removed = self.removeWord(word[1:])
            #If the letter after this was removed, consider removing this node.
            if removed:
                #Stop here if there wouldbe other keys removed.
                if len(self.arr.keys()) > 1:
                    return False
                else:
                    self.removeNode()
                    return True
            #If the next letter wasn't removed, it was part of a different trie.  this shouldn't be removed.
            else:
                return False

        #Continue removal here.


        #Removenode should only remove this node.  Recursion should be handled by the calling function
        #Cases:
        #1. Leaf node
            #Remove data in node, shouldn't need to be more complex than del?
                #What about if there is a nested node beneath this?  Does it get removed by del?
            #Remove node itself, Proceed to parent.
        #2. Branch node above a Leaf
            #Check if it has children other than the one that was just removed
            #if so, do not remove, stop here, return True or Word+payload
            #if not, remove self, proceed to parent.
        #3. Root
            #Check if it has children other than the one that was just removeNod
                #If so, do not remove, return True or Word+payload
                #if not, remove node, return True or Word + Payload.


        #On return to removeWord, gc.collect()

    #Return the payload of the given Trie with the given key, if it exists.
    '''
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
            if not child.isEnd:
                print(child.letter, end="")
                child.printWordsInTrie()
            else:
                print(self.arr[indexNode].letter)
                if type(child.payload) is TrieNode:
                    child.printWordsInTrie()
                else:
                    print(child.payload)

#Need some init function, why not main?
if __name__ == "__main__":
    node = TrieNode("*")
    node.addWord("albatross", "birdy")
    node.addWord("Alberta", "province")
    node.addWord("alpaca", "llama")
    node.addWord("antigua", "barbuda")
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
