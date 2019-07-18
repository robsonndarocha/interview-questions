import random

class Array:
  def __init__(self, array):
    """
    Parameters
    ----------
    array : list
      The array to be shuffled
    """
    self.array = array

  def shuffle(self):
    """Rearranges an array randomly

    Raises
    ------
    Exception
      If the input array is empty

    Returns
    -------
    The shuffled array
    """
    if self.array:
      # Traverses the array backwards
      for i in range(len(self.array) - 1, 0, -1):
        # Creates a random index
        j = random.randint(0, i + 1)
        # Moves the element under the random index to the ith element and the ith element to the randomic position
        self.array[i], self.array[j] = self.array[j], self.array[i]
      return self.array
    else:
      raise Exception('Empty array!')
