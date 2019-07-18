"""Given a square matrix, calculate the absolute difference between the sums of its diagonals"""

class Matrix:
  def __init__(self, matrix):
    """
    Parameters
    ----------
    matrix : list
      The matrix to be explored
    """
    self.matrix = matrix

  def get_diagonal_difference(self):
    """Calculates the absolute difference between the sums of its diagonals

    Raises
    ------
    Exception
      If the input matrix is empty

    Returns
    -------
    The absolute difference between the sums of its diagonals
    """
    if self.matrix:
      total = 0
      # Traverses the matrix
      for i in range(len(self.matrix)):
        for j in range(len(self.matrix)):
          # Checks if the element belongs to the left-to-right diagonal
          if i == j:
            # Sum the value of the elements
            total = total + self.matrix[i][j]
      # Subtract the sum of the right-to-left diagonal elements from the sum of the left-to-right diagonal ones
      total = total - sum(self.matrix[i][len(self.matrix) - i - 1] for i in range(len(self.matrix)))
      # Returns the absolute value
      return abs(total)
    else:
      raise Exception('Empty matrix!')
