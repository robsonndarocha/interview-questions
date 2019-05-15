"""You have a list of words and a pattern, and you want to know which words in the list matches the pattern

Source
------
https://leetcode.com/problems/find-and-replace-pattern/
"""

import re

class List:
  def find_and_replace_pattern(self, words, pattern):
    """Finds the words in a list that match the pattern
    Raises
    ------
    Exception
      If the input wordlist and pattern are empty
    Returns
    -------
    The matching words
    """
    matching_words = []
    if words and pattern:
      for word in words:
        if self.match(word, pattern):
          matching_words.append(word)
      return matching_words
    else:
      raise Exception('There\'s one or more empty inputs. Please, consider supplying both a wordlist and a pattern.')

  def match(self, word, pattern):
    """Matches a word against a pattern
    Returns
    -------
    True
      If the word matches the pattern
    False
      If the word doesn't match the pattern
    """
    char_backreference = {}
    regular_expression = ''
    for char in pattern:
      # Checks if the character is already 'backreferenced'
      if char not in char_backreference:
        # Creates a capture group '(.+)' that matches one or more occurrences
        regular_expression += '(.+)'
        # Associates the capture group to a backreference '\n' of a character
        char_backreference[char] = len(char_backreference) + 1
      else:
        # Mentions the corresponding backreference of a character if it appears
        regular_expression += '\\' + str(char_backreference[char])
    # Matches the Regular Expression against the input word, returning True or False
    return re.match(regular_expression + '$', word)
