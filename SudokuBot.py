import GameGrid as gg
import BacktrackingSolver as bs
import pyautogui

def run():
    grid = gg.init_grid()
    bs.solve_sudoku(grid)
    auto_enter_vals(grid)

def auto_enter_vals(solved_grid):
    for r in range(9):
        for c in range(9):
            if r%2 == 0:
                pyautogui.write(str(solved_grid[r,c]))
                pyautogui.press('right')
            else:
                pyautogui.write(str(solved_grid[r,8-c]))
                pyautogui.press('left')
        pyautogui.press('down')
