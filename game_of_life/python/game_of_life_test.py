import unittest
from ddt import ddt, data, unpack
from game_of_life import *

@ddt
class TestGameOfLife(unittest.TestCase):

  @data(
    (['ooo', 'oxo', 'ooo'], 1, 1, 0), 
    (['ooo', 'oxo', 'ooo'], 0, 0, 1),
    (['ooo', 'oxx', 'xxx'], 2, 2, 3)
  )
  @unpack
  def test_count_live_neighbors_works(self, board, x, y, expected_neighbors):
    self.assertEqual(count_live_neighbors(board, x, y), expected_neighbors)

  @data(
    (ALIVE, True),
    (DEAD, False)
  )
  @unpack
  def test_is_cell_alive_works(self, cell, expected_result):
    self.assertEqual(is_cell_alive(cell), expected_result)
    
  @data(
    (ALIVE, False),
    (DEAD, True)
  )
  @unpack
  def test_is_cell_dead_works(self, cell, expected_result):
    self.assertEqual(is_cell_dead(cell), expected_result)

  @data(
    (ALIVE, 0, DEAD),
    (ALIVE, 1, DEAD),
    (ALIVE, 2, ALIVE),
    (ALIVE, 3, ALIVE),
    (ALIVE, 4, DEAD),
    (ALIVE, 5, DEAD),
    (ALIVE, 6, DEAD),
    (ALIVE, 7, DEAD),
    (ALIVE, 8, DEAD),
    (DEAD, 0, DEAD),
    (DEAD, 1, DEAD),
    (DEAD, 2, DEAD),
    (DEAD, 3, ALIVE),
    (DEAD, 4, DEAD),
    (DEAD, 5, DEAD),
    (DEAD, 6, DEAD),
    (DEAD, 7, DEAD),
    (DEAD, 8, DEAD)
  )
  @unpack
  def test_new_status_works(self, cell, number_of_neighbors, expected_new_status):
    self.assertEqual(new_status(cell, number_of_neighbors), expected_new_status)
 
if __name__ == '__main__':
    unittest.main()
