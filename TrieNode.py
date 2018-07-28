class TrieNode(object):
    #A=0, B=1, .... Z = 25.
    def __init__(self, letter, parent=None):
        self.letter = letter
        self.arr = {}
        self.payload = None
        self.isEnd = False
        self.parent = parent

    # Add a dictionary to the Trie, recursively.
    def addDict(self, d):
        for key in d.keys():
            if type(d[key]) is dict:
                subTrie = TrieNode("*")
                subTrie.addDict(d[key])
                self.addWord(key, subTrie)
            #No handling for dictionaries in arrays, currently.
            else:
                self.addWord(key, d[key])

    # Add a key value pair or a word to the Trie.
    def addWord(self, word, payload=None):
        node = self
        word = word.upper()

        #Traverse through the word until all letters are nodes
        for letter in word:
            letterVal = ord(letter) - 65

            #If node is in, traverse.  Else, add the node.
            if node.arr.get(letterVal, None):
                node = node.arr[letterVal]
            else:
                newNode = TrieNode(letter, node)
                node.arr[letterVal] = newNode
                newNode.parent = node
                node = newNode

        #Mark the end of this word and append the payload.
        node.payload = payload
        node.isEnd = True

    #Remove this node from the Trie, don't remove *
    def removeNode(self):
        if self.parent:
            val = ord(self.letter) - 65
            self.parent.arr.pop(val)
        self.cleanNode()
        self.arr = {}
        self.isEnd = False

    #Remove the payload of this node from Trie without removing the node itself
    def cleanNode(self):
        self.isEnd = False
        self.payload = None


    #Remove a given word from the Trie
    def removeWord(self, word):
        node = self
        word = word.upper()

        i = 0

        #Traverse down to the last letter, then walk back up to the parent.
        while node and i < len(word):
            node = node.arr.get(ord(word[i]) - 65)
            i += 1

        if node:#If not node, we were given an invalid word to remove
            #There must be a more pythonic way to do this
            if len(node.arr) > 0:
                node.cleanNode()
            else:
                while len(node.arr) == 0:
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

    def buildWordFromEnd(self, partial=""):
        if self.parent:
            partial = self.letter + partial
            return self.parent.buildWordFromEnd(partial)
        else:
            return partial

    #return the trie structure from this point as a python dictionary.
    #TODO: O(2N).  Can be improved.
    def trieToDict(self, newDict={}):
        node = self
        #For all keys at this level
        for child in node.arr.keys():
            cur = node.arr[child]
            #If there's a word ending here, build a dictionary value.
            if cur.isEnd:
                if type(cur.payload) is TrieNode:
                    payloadDict = cur.payload.trieToDict()
                    newDict[cur.buildWordFromEnd()] = payloadDict
                else:
                    newDict[cur.buildWordFromEnd()] = cur.payload

            cur.trieToDict(newDict)
        return newDict
        #Do O(2N) solution first
        #Traverse down to each isEnd, ascend back up


            #For every key on this level, we have some preceding string that is identical to the
                #other keys on this level
            #for every key:
                #If it would end the string
                    #If it has no children, we append the string to our list
                    #If it has children, we append the string to our list and make a copy of it
                    #This copy continues to be built downwards
                #else it would not end the string.
                    #a copy of the string must exist to this point for every child node
                    #make copies if necessary
        #keys.append(key)


'''
    #A work in progress.  Print the keys in this trie, top down.
    #Currently does not print each word, prints all letters in each trie branch.
    def printWordsInTrie(self):
        letters = []
        for indexNode in self.arr.keys():
            child = self.arr[indexNode]
            if child:
                if not child.isEnd:
                    for cl in child.printWordsInTrie():
                        letters.append(child.letter + cl)
                else:
                    letters.append(child.letter)
                    if type(child.payload) is TrieNode:
                        #print(child.payload)
                        #letters.append(child.payload.printWordsInTrie())
                        pass
                    else:
                        letters.append(child.payload)
            else:
                print("We shouldn't get here.  indexNode: ", indexNode)
        return letters
'''
#Need some init function, why not main?
if __name__ == "__main__":
    node = TrieNode("*")
    node.addWord("albatross", "birdy")
    node.addWord("Alberta", "province")
    node.addWord("alpaca", "llama")
    node.addWord("abc", "barbuda")
    node.addWord("alibaba")
    node.addWord("babi", "nani")
    #printWordsInTrie(node)
    #print(node.findPayload("antigua"))

    #print(findPayload(node, "albatross"))


    someDict = {"abc":{"ard":[1,2,3,4], "babby":"boy"}, "ard":"456"}
    node.addDict(someDict)
    #printWordsInTrie(dictTrie)

    #innerTrie = node.findPayload("abc")

    #tempNode = node.arr[0].arr[1].arr[2]

    #print(tempNode.buildWordFromEnd())

    trieDict = node.findPayload("abc")
    print(trieDict.trieToDict())
    print(node.trieToDict())
    #print(trieDict["ABC"]["ARD"])
    #print(node.trieToDict())
    #print(innerTrie.findPayload("ard"))

    #print(node.printWordsInTrie())

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
