import GameGrid as gg
import BacktrackingSolver as bs
import pyautogui
import timeit

def run():
    t_0 = timeit.default_timer()
    grid = gg.init_grid()
    #print(f'Initial Grid:\n{grid}\n')
    t_1 = timeit.default_timer()

    ss_t = t_1-t_0

    t_0 = timeit.default_timer()
    bs.solve_sudoku(grid)
    #print(f'Solved Grid:\n{grid}\n')
    t_1 = timeit.default_timer()

    slv_t = t_1-t_0

    t_0 = timeit.default_timer()
    auto_enter_vals(grid)
    t_1 = timeit.default_timer()

    ent_t = t_1-t_0

    return (ss_t, slv_t, ent_t)


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

t_i = timeit.default_timer()
run_times = run()
t_f = timeit.default_timer()

tot_t = t_f-t_i
ss_t = run_times[0]
slv_t = run_times[1]
ent_t = run_times[2]

(f'Total execution time: {tot_t:.5f} seconds')

print(f'Time to take screen shots and init values: {ss_t:.5f} seconds | {(ss_t/tot_t)*100:.5f}%')
print(f'Time to solve using backtracking: {slv_t:.5f} seconds | {(slv_t/tot_t)*100:.5f}%')
print(f'Time to enter values: {ent_t:.5f} seconds | {(ent_t/tot_t)*100:.5f}%\n')
