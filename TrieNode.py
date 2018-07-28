class TrieNode(object):
    #A=0, B=1, .... Z = 25.
    def __init__(self, letter, parent=None, caseSensitive = False):
        self.letter = letter
        self.arr = {}
        self.caseSensitive = caseSensitive
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
        if not self.caseSensitive:
            word = word.upper()


        #Traverse through the word until all letters are nodes
        for letter in word:
            #If node is in, traverse.  Else, add the node.
            if node.arr.get(letter):
                node = node.arr[letter]
            else:
                newNode = TrieNode(letter, node)
                node.arr[letter] = newNode
                newNode.parent = node
                node = newNode

        #Mark the end of this word and append the payload.
        node.payload = payload
        node.isEnd = True

    #Remove this node from the Trie, don't remove *
    def removeNode(self):
        if self.parent:
            self.parent.arr.pop(self.letter)
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
        if not self.caseSensitive:
            word = word.upper()
        i = 0

        #Traverse down to the last letter, then walk back up to the parent.
        while node and i < len(word):
            node = node.arr.get(letter)
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
        if not self.caseSensitive:
            key = key.upper()
        for letter in key:
            keyVal = letter
            if node.arr.get(keyVal):
                node = node.arr[keyVal]
            else:
                return None
        if node.isEnd:
            return node.payload
        return None

    #Given a node, return its word.
    def buildWord(self, partial=""):
        if self.parent:
            partial = self.letter + partial
            return self.parent.buildWord(partial)
        else:
            return partial

    #return the trie structure from this point as a python dictionary.
    #TODO: O(N^2) ish.  Can be improved to O(N)
    def trieToDict(self, newDict={}):
        node = self
        #For all keys at this level
        for child in node.arr.keys():
            cur = node.arr[child]
            #If there's a word ending here, build a dictionary value.
            if cur.isEnd:
                if type(cur.payload) is TrieNode:
                    payloadDict = cur.payload.trieToDict()
                    newDict[cur.buildWord()] = payloadDict
                else:
                    newDict[cur.buildWord()] = cur.payload

            cur.trieToDict(newDict)
        return newDict

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

    #print(tempNode.buildWord())

    trieDict = node.findPayload("ard")
    #print(trieDict.trieToDict())
    print(node.trieToDict())

    print(node.arr['A'].arr)
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
