import lib.utils.functools as ft


def default_game_state():
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
    return {
        **state,
        'error':error
    }


def clean_error(state):
    return {
        **state,
        'error':None
    }

def game_step(state, x,y):
        
    def try_mark_cell(state, x, y):
        new_state = {**state}
        current_player = new_state['current_player']
        if(new_state['grid'][x][y] is None):
            new_state['grid'][x][y] = new_state['players'][current_player]
        else:
            return set_error(state, 'Cell already marked')
        return new_state

    def switch_player(state):
        return {
            **state,
            'current_player': 0 if state['current_player'] == 1 else 1
        }

    def check_line(line):
        if line[0] is None:
            return False
        return all([cell == line[0] for cell in line])

    def check_lines(grid):
        return any([check_line(line) for line in grid])

    def check_columns(grid):
        return check_lines([list(column) for column in zip(*grid)])

    def check_diagonals(grid):
        return check_lines([
            [grid[0][0], grid[1][1], grid[2][2]],
            [grid[0][2], grid[1][1], grid[2][0]]
        ])

    def check_winner(state):
        return {
            **state,
            'winner': ft.any_predicate(state['grid'],[
                check_lines,
                check_columns,
                check_diagonals
            ])
        }


    return ft.pipe_error_checked(state,[
        lambda s: try_mark_cell(s, x, y),
        switch_player,
        check_winner
    ])


def get_grid_as_string(state):
    return '\n'.join([' '.join([str(cell) for cell in line]) for line in state['grid']])