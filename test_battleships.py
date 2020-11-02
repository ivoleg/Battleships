import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    #add at least four more tests for is_sunk by the project submission deadline

def test_ship_type1():
    s = (1, 1, True, 1, {})
    assert ship_type(s) == 'submarine'
    #provide at least five tests in total for ship_type by the project submission deadline

def test_is_open_sea1():
    row = 3
    column = 2
    fleet = [(1, 1, True, 1, {}), (2, 8, True, 1, {}), (9, 0, True, 1, {}), (8, 9, True, 1, {}), (1, 4, False, 2, {}), 
             (0, 7, True, 2, {}), (5, 0, False, 2, {}), (4, 6, True, 3, {}), (7, 6, False, 3, {}), (5, 2, False, 4, {})]
    assert is_open_sea(row, column, fleet) == True
    #provide at least five tests in total for open_sea by the project submission deadline

def test_ok_to_place_ship_at1():
    row = 5
    column = 2
    horizontal = False
    length = 4
    fleet = [(1, 1, True, 1, {}), (2, 8, True, 1, {}), (9, 0, True, 1, {}), (8, 9, True, 1, {}), (1, 4, False, 2, {}), 
             (0, 7, True, 2, {}), (5, 0, False, 2, {}), (4, 6, True, 3, {}), (7, 6, False, 3, {})]
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

def test_place_ship_at1():
    row = 5
    column = 2
    horizontal = False
    length = 4
    fleet = [(1, 1, True, 1, {}), (2, 8, True, 1, {}), (9, 0, True, 1, {}), (8, 9, True, 1, {}), (1, 4, False, 2, {}), 
             (0, 7, True, 2, {}), (5, 0, False, 2, {}), (4, 6, True, 3, {}), (7, 6, False, 3, {})]
    assert place_ship_at(row, column, horizontal, length, fleet) == [(1, 1, True, 1, {}), (2, 8, True, 1, {}), (9, 0, True, 1, {}), (8, 9, True, 1, {}), (1, 4, False, 2, {}), (0, 7, True, 2, {}), (5, 0, False, 2, {}), (4, 6, True, 3, {}), (7, 6, False, 3, {}), (5, 2, False, 4, {})]
    #provide at least five tests in total for place_ship_at by the project submission deadline

def test_check_if_hits1():
    row = 4
    column = 7
    fleet = [(1, 1, True, 1, {}), (2, 8, True, 1, {}), (9, 0, True, 1, {}), (8, 9, True, 1, {}), (1, 4, False, 2, {}), 
             (0, 7, True, 2, {}), (5, 0, False, 2, {}), (4, 6, True, 3, {}), (7, 6, False, 3, {}), (5, 2, False, 4, {})]
    assert check_if_hits(row, column, fleet) == True
    #provide at least five tests in total for check_if_hits by the project submission deadline

def test_hit1():
    row = 4
    column = 7
    fleet = [(1, 1, True, 1, {}), (2, 8, True, 1, {}), (9, 0, True, 1, {}), (8, 9, True, 1, {}), (1, 4, False, 2, {}), 
             (0, 7, True, 2, {}), (5, 0, False, 2, {}), (4, 6, True, 3, {}), (7, 6, False, 3, {}), (5, 2, False, 4, {})]
    assert hit(row, column, fleet) == ([(1, 1, True, 1, {}), (2, 8, True, 1, {}), (9, 0, True, 1, {}), (8, 9, True, 1, {}), (1, 4, False, 2, {}), (0, 7, True, 2, {}), (5, 0, False, 2, {}), (4, 6, True, 3, {(4,7)}), (7, 6, False, 3, {}), (5, 2, False, 4, {})], (4, 6, True, 3, {}))
    #provide at least five tests in total for hit by the project submission deadline

def test_are_unsunk_ships_left1():
    fleet = [(1, 1, True, 1, {}), (2, 8, True, 1, {}), (9, 0, True, 1, {}), (8, 9, True, 1, {}), (1, 4, False, 2, {}), 
             (0, 7, True, 2, {}), (5, 0, False, 2, {}), (4, 6, True, 3, {}), (7, 6, False, 3, {}), (5, 2, False, 4, {})]
    assert are_unsunk_ships_left(fleet) == True
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    
def test_filled_squares(): #test for filled_squares
    ship = (1, 1, True, 1, {})
    assert filled_squares(ship) == set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])