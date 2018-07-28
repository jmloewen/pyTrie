This is a Python3 implementation of a Trie, using Dictionaries.

End goal is the ability to be compliant with JSON standard.

Features:
  Import Dictionary to TrieNode
  Import Words & Payloads to TrieNode
  Remove Words from TrieNode
  Export TrieNode as Dictionary
  Return Value in Trie given Key

Feature Goals:
-Full test suite
-Print entire Trie given a child node
-Faster export function (current is slow)
-Include ability to parse through dicts nested in arrays, arrays nested in arrays.
-Include Array as alternative to dictionary
-Remove Dict from TrieNode
  -Include ability to export as Array
-Maybe's:
  -Allowance for duplicate values within a single key?
  -Case Sensitivity in letters?  Is this something that should be added?
Goal:
-Compliance with JSON standard - should be able to import JSON dictionary, add values to it, and export as a new JSON dictionary
