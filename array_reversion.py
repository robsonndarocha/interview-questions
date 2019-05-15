import math

class Array:
  def __init__(self, array):
    """
    Parameters
    ----------
    array : list
      The array to be reversed
    """
    self.array = array

  def reverse(self):
    """Rearranges an array backwards

    Raises
    ------
    Exception
      If the input array is empty

    Returns
    -------
    The reversed array
    """
    if self.array:
      # Traverses half of the array
      for i in range(math.floor(len(self.array) / 2)):
        # Moves the last element to the first place and the first element to the last place
        self.array[i], self.array[len(self.array) - i - 1] = self.array[len(self.array) - i - 1], self.array[i]
      return self.array
    else:
      raise Exception('Empty array!')
