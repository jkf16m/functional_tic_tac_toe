import lib.utils.functools as ft



def default_game_state():
    """
    Returns the default game state
    It's a dictionary representing the whole game state
    """
    return {
        'grid':[
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ],
        'players':['X', 'O'],
        'current_player':0,
        'winner':None
    }


def set_error(state, error):
    """
    Sets a property "error" inside the dictionary state
    """
    return {
        **state,
        'error':error
    }


def clean_error(state):
    """
    Cleans the error property from the state dictionary
    """
    return {
        **state,
        'error':None
    }























def try_mark_cell(state, x, y):
    """
    Tries to mark a cell in the grid
    If the cell is already marked, it returns the state with an error
    """
    new_state = {**state}
    current_player = new_state['current_player']
    if(new_state['grid'][x][y] is None):
        new_state['grid'][x][y] = new_state['players'][current_player]
    else:
        return set_error(state, 'Cell already marked')
    return new_state

def switch_player(state):
    """
    Switches the current player, possible values are 0 and 1 (indexes of the players list)
    """
    return {
        **state,
        'current_player': 0 if state['current_player'] == 1 else 1
    }


# WINNING CHECK FUNCTIONS
def check_line(line):
    """Checks if a line is full of the same value"""
    if line[0] is None:
        return False
    return all([cell == line[0] for cell in line])

def check_lines(grid):
    """Checks if any line is full of the same value"""
    return any([check_line(line) for line in grid])

def check_columns(grid):
    """Checks if any column is full of the same value"""
    return check_lines([list(column) for column in zip(*grid)])

def check_diagonals(grid):
    """Checks if any diagonal is full of the same value"""
    return check_lines([
        [grid[0][0], grid[1][1], grid[2][2]],
        [grid[0][2], grid[1][1], grid[2][0]]
    ])


# HERE WINNING CHECK FUNCTIONS ARE USED
def check_winner(state):
    """Checks if there is a winner using the functions above"""
    return {
        **state,
        'winner': ft.any_predicate(state['grid'],[
            check_lines,
            check_columns,
            check_diagonals
        ])
    }




def game_step(state, x,y):
    """
    Performs a game step
    It tries to mark the cell, then it checks if there is a winner

    If there is an error, it returns the state with the error
    """
    return ft.pipe_error_checked(state,[
        lambda s: try_mark_cell(s, x, y),
        switch_player,
        check_winner
    ], lambda s: set_error(s, 'Invalid move'))


def get_grid_as_string(state):
    return '\n'.join([' '.join([str(cell) for cell in line]) for line in state['grid']])