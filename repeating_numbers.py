class NumberArray:
  def __init__(self, array):
    """
    Parameters
    ----------
    array : list
      The array to be verified
    """
    self.array = array

  def get_repeating_numbers(self):
    """Checks for repeating numbers

    Raises
    ------
    Exception
      If the input array is empty

    Returns
    -------
    The repeating numbers
    """
    if self.array:
      repeating_numbers = []
      for i in range(len(self.array)):
        # Gets the current position
        pos = i + 1
        for j in range(pos, len(self.array)):
          # Checks if the elements match and ...
          if self.array[i] == self.array[j]:
            # ... if they're not in the 'repeating_numbers' list ...
            if self.array[i] not in repeating_numbers:
              # ... flags the element as a repeating one
              repeating_numbers.append(self.array[i])
      return repeating_numbers
    else:
      raise Exception('Empty array!')
