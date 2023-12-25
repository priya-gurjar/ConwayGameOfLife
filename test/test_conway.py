import sys
import os

# Add the directory containing GameOfLife.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from GameOfLife import next_generation
import global_vars as g


def test_alive_cell():
    g.rows = 10
    g.cols = 10
    g.current_cells = [[0 for i in range(g.cols)] for j in range(g.rows)]
    g.current_cells[0][0] = 1
    g.current_cells[0][1] = 1
    g.current_cells[1][0] = 1
    
    g.current_cells[1][8] = 1
    g.current_cells[1][7] = 1
    g.current_cells[0][8] = 1
    g.current_cells[2][8] = 1
    
    g.current_cells[9][9] = 1
    g.new_cells = g.current_cells
    next_generation(g.rows, g.cols, g.current_cells, g.new_cells)
    assert g.new_cells[0][0] == 1
    assert g.new_cells[1][8] == 1
    assert g.new_cells[9][9] == 0


def test_dead_cell():
    g.rows = 10
    g.cols = 10
    g.current_cells = [[0 for i in range(g.cols)] for j in range(g.rows)]
    
    g.current_cells[1][8] = 1
    g.current_cells[1][7] = 1
    g.current_cells[0][8] = 1
    
    g.new_cells = g.current_cells
    next_generation(g.rows, g.cols, g.current_cells, g.new_cells)
    
    assert g.new_cells[0][7] == 1


def test_update_cells():
    g.rows = 10
    g.cols = 10
    g.current_cells = [[0 for i in range(g.cols)] for j in range(g.rows)]
    
    g.current_cells[1][8] = 1
    g.current_cells[1][7] = 1
    g.current_cells[0][8] = 1
    
    g.new_cells = g.current_cells
    g.numOfCells = 3
    next_generation(g.rows, g.cols, g.current_cells, g.new_cells)
    
    assert g.numOfCells == 4

