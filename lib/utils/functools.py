import random

def map_if(list, predicate, function):
    """Applies a function to each element of a list if the predicate is true.
    """
    return [function(element) for element in list if predicate(element)]

def map_at_least(list, n, random_seed, function):
    """Applies a function to at least n elements of a list.
    """
    if len(list) <= n:
        return map(function, list)
    else:
        random.seed(random_seed)
        return [function(element) for element in random.sample(list, n)]


def pipe(var, functions):
    """Applies a list of functions to a variable.
    """
    for function in functions:
        var = function(var)
    return var

def pipe_error_checked(var, functions, error_function = None):
    """
        Appliest a list of functions to a variable.
        If a function returns a dictionary with an error key, the pipe is stopped and the error_function is called.
    """
    for function in functions:
        var = function(var)
        if 'error' in var and var['error'] is not None:
            return error_function(var) if error_function is not None else var
    return var

def repeat_until(function, predicate):
    """Applies a function until the predicate is true.
    """
    while not predicate(var):
        var = function(var)
    return var


def any_predicate(var, predicates):
    """
        Returns True if any of the predicates is true for the variable
    """
    for predicate in predicates:
        if predicate(var):
            return True
    return False

def tap(var, function):
    """Applies a function to a variable and returns the variable.
    """
    function(var)
    return var