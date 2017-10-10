from curses import wrapper
import time
import sys

ALIVE = 'x'
DEAD = 'o'

BOARD = [
  ['o', 'o', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'o', 'o'],
  ['o', 'x', 'x', 'x', 'o'],
  ['o', 'o', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'o', 'o'],
]


def is_cell_alive(cell):
  return cell == ALIVE

def is_cell_dead(cell):
  return cell == DEAD

def count_live_neighbors(board, x, y):
  check_coordinates = [
    (x1, y1) 
    for x1 in range(x - 1, x + 2) if x1 >= 0 and x1 < len(board[0])
    for y1 in range(y - 1, y + 2) if y1 >= 0 and y1 < len(board) 
    if (x1, y1) != (x, y)
  ]
  neighbors = [board[y1][x1] for (x1, y1) in check_coordinates]
  return sum(is_cell_alive(cell) for cell in neighbors)

def new_status(cell, number_of_neighbors):
  new_status = cell
  if is_cell_alive(cell):
    if number_of_neighbors < 2 or number_of_neighbors > 3:
      new_status = DEAD
  elif is_cell_dead(cell) and number_of_neighbors == 3:
    new_status = ALIVE
  return new_status

def update_board(board):
  new_board = []
  for y in range(0, len(board)):
    new_row = []
    for x in range(0, len(board[y])):
      new_row.append(new_status(board[y][x], count_live_neighbors(board, x, y)))
    new_board.append(new_row)
  return new_board

def print_board(stdscr, board, iteration):
  stdscr.clear()
  stdscr.addstr(0, 0, str(iteration))
  stdscr.addstr(1, 0, '\n'.join([''.join(row) for row in board]))
  stdscr.refresh()

def main(stdscr):
  board = list(list(row) for row in BOARD)
  for i in range(1, 10):
    print_board(stdscr, board, i)
    time.sleep(1)
    board = update_board(board)


if __name__ == '__main__':
  wrapper(main)
