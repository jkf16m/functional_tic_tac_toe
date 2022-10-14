import lib.tic_tac_toe as ttt
import lib.utils.functools as ft

def main():
    game_state = ttt.default_game_state()

    ft.pipe_error_checked(game_state, # This is the variable that will be passed to the functions
    
        [ # This is the list of functions, they will be applied in order, the result of the previous function will be passed to the next one
            lambda g: ttt.game_step(g, 0, 0),
            lambda g: ttt.game_step(g, 0, 1),
            lambda g: ttt.game_step(g, 0, 1),
            lambda g: ttt.game_step(g, 1, 1),
            lambda g: ft.tap(g, lambda g: print(g)),
            lambda g: ft.tap(g, lambda g: print(ttt.get_grid_as_string(g)))
        ],
        
        lambda g: ft.tap(g, lambda g: print(g)) # This is the error function, executed if an error occurs in the pipe (no matter where)
    ) # End of pipe_error_checked

if __name__ == '__main__':
    main()