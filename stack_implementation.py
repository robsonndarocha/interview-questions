import random

class Stack:
  def __init__(self, stack):
    """
    Parameters
    ----------
    stack : list
      The stack to be implemented
    """
    self.stack = stack

  def is_empty(self):
    """Checks if the stack is empty

    Returns
    ------
    True
      If the stack is empty
    False
      If the stack is not empty
    """
    if not self.stack:
      return True
    else:
      return False

  def max(self):
    """Gets the greater value in the stack

    Raises
    ------
    Exception
      If the input stack is empty

    Returns
    ------
    The greater value in the stack
    """
    if self.stack:
      max = 0
      for element in self.stack:
        if element > max:
          max = element
      return max
    else:
      raise Exception('Empty stack!')

  def peek(self):
    """Gets the first element of the stack

    Raises
    ------
    Exception
      If the input stack is empty

    Returns
    ------
    The first element of the stack
    """
    if self.stack:
      return self.stack[len(self.stack) - 1]
    else:
      raise Exception('Empty stack!')

  def pop(self):
    """Removes the last element of the stack

    Raises
    ------
    Exception
      If the input stack is empty

    Returns
    ------
    The element removed from the stack
    """
    if self.stack:
      # Removes the last element of the stack and then returns it
      last_element = self.stack[-1]
      del self.stack[-1]
      return last_element
    else:
      raise Exception('Empty stack!')

  def push(self, element):
    """Inserts an element at the end of the stack

    Raises
    ------
    Exception
      If the input stack is empty

    Returns
    ------
    The updated stack
    """
    if self.stack:
      # Adds an element to the end of the stack
      self.stack[len(self.stack):] = [element]
      return self.stack
    else:
      raise Exception('Empty stack!')

  def size(self):
    """Gets the size of the stack

    Returns
    ------
    The size of the stack
    """
    if self.stack:
      return len(self.stack)
    else:
      return 0
