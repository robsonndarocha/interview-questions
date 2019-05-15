class NumberArray:
  def __init__(self, array):
    """
    Parameters
    ----------
    array : list
      The array to be verified
    """
    self.array = array

  # def get_twice_repeating_numbers(self):
  #   for i in range(len(self.array)):
  #     for j in range(i + 1, len(self.array)):
  #       if self.array[i] == self.array[j]:
  #         print(self.array[i])

  def get_twice_repeating_numbers(self):
    """Checks for twice repeating numbers

    Raises
    ------
    Exception
      If the input array is empty

    Returns
    ------
    The twice repeating numbers
    """
    if self.array:
      # Creates an array filled with 0's of the same size of the input one
      count = [0] * len(self.array)
      for i in range(len(self.array)):
        # Checks if there's an occurrence
        if count[self.array[i]] == 1:
          return self.array[i]
        else:
          # Adds an occurrence
          count[self.array[i]] = count[self.array[i]] + 1
    else:
      raise Exception('Empty array!')
