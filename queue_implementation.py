import math
import random

class Queue:
  def __init__(self, stack):
    """
    Parameters
    ----------
    stack : list
      The stack to be transformed into a queue
    """
    self.stack = stack
    # Reverses the stack using a bultin function
    self.queue = self.reverse(self.stack)

  def dequeue(self):
    """Removes the first element of the queue

    Raises
    ------
    Exception
      If the input stack or queue are empty

    Returns
    -------
    The updated queue
    """
    if self.stack and self.queue:
      # Removes the last (first) element of the queue
      del self.queue[-1]
      # Makes it reflect into the stack
      self.stack = self.reverse(self.queue)
      return self.queue
    else:
      raise Exception('Empty queue!')

  def enqueue(self, element):
    """Adds an element to the queue

    Raises
    ------
    Exception
      If the input queue is empty

    Returns
    -------
    The updated queue
    """
    if self.stack and self.queue:
      # Adds an element to the end of the stack
      self.stack[len(self.stack):] = [element]
      # Makes it reflect into the queue
      self.queue = self.reverse(self.stack)
      return self.queue
    else:
      raise Exception('Empty queue!')

  def front(self):
    """Gets the first element of the queue

    Raises
    ------
    Exception
      If the input queue is empty

    Returns
    -------
    The first element of the queue
    """
    if self.queue:
      return self.queue[0]
    else:
      raise Exception('Empty queue!')

  def is_empty(self):
    """Checks if the queue is empty

    Returns
    ------
    True
      If the queue is empty
    False
      If the queue is not empty
    """
    if not self.queue:
      return True
    else:
      return False

  def reverse(self, array):
    """Rearranges an array backwards

    Raises
    ------
    Exception
      If the input array is empty

    Returns
    -------
    The reversed array
    """
    if array:
      # Traverses half of the array
      for i in range(math.floor(len(array) / 2)):
        # Moves the last element to the first place and the first element to the last place
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]
      return array
    else:
      raise Exception('Empty array!')

  def size(self):
    """Returns the the size of the queue

    Returns
    -------
    The size of the queue
    """
    if self.queue:
      return len(self.queue)
    else:
      return 0
