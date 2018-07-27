#This Python implementation of a Trie is made to store items at the end of each Trie branch.
#Primary usage is to convert dictionary key value pairs into a Trie structure.
#Cannot currently handle multiple equal keys.  New key will overwrite the old, as is.
#Current implementation of the descendant "trie" nodes creates a dictionary to be filled with single-letter
#KVP's, rather than allocate 26 arrays filled with None.  Will implement alternative for arrays rather than dictsself.
