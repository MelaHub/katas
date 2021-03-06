import unittest
from ddt import ddt, data, unpack
from game_of_life import *

@ddt
class TestGameOfLife(unittest.TestCase):

  @data(
    (['   ', ' x ', '   '], 1, 1, 0), 
    (['   ', ' x ', '   '], 0, 0, 1),
    (['   ', ' xx', 'xxx'], 2, 2, 3),
    (['   ', 'xxx', '   '], 2, 0, 2)
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

  @data(
    ('     xx  xx     ', '     xx  xx     ', 4),
    ('   xxx   ', ' x  x  x ', 3),
  )
  @unpack
  def test_update_board_works(self, input_board, expected_board, board_size):
    board = [list(input_board[i:i+board_size]) for i in range(0, len(input_board), board_size)]
    self.assertEqual(''.join([''.join(row) for row in update_board(board)]), expected_board)
 
if __name__ == '__main__':
    unittest.main()
