import pytest
from battleships import *

def test_is_sunk1():
    s1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s1) == True
    s2 = (4, 3, False, 4, {(4,3)})
    assert is_sunk(s2) == False
    s3 = (0, 5, True, 2, {(0,5), (0,6)})
    assert is_sunk(s3) == True
    s4 = (5, 2, True, 4, {(5,2), (5,3), (5,4), (5,5)})
    assert is_sunk(s4) == True
    s5 = (7, 8, True, 1, set())
    assert is_sunk(s5) == False

def test_ship_type1():
    s1 = (1, 1, True, 1, set())
    assert ship_type(s1) == 'submarine'
    s2 = (0, 8, False, 3, {(1,8)})
    assert ship_type(s2) == 'cruiser'
    s3 = (7, 5, True, 2, {(7,5), (7,6)})
    assert ship_type(s3) == 'destroyer'
    s4 = (3, 4, False, 4, set())
    assert ship_type(s4) == 'battleship'
    s5 = (5, 7, False, 1, set())
    assert ship_type(s5) == 'submarine'

def test_is_open_sea1():
    row1 = 3
    column1 = 2
    fleet1 = [(1, 1, True, 1, {(1,1)}), (2, 8, True, 1, set()), (9, 0, True, 1, set()), (8, 9, True, 1, {(8,9)}),
             (1, 4, False, 2, {(2,4)}), 
             (0, 7, True, 2, set()), (5, 0, False, 2, set()), (4, 6, True, 3, {(4,7), (4,8)}), (7, 6, False, 3, set()), 
             (5, 2, False, 4, {(5,2), (6,2), (7,2), (8,2)})]
    assert is_open_sea(row1, column1, fleet1) == True
    row2 = 4
    column2 = 8
    fleet2 = [(7, 4, True, 4, set()), (2, 4, True, 3, set()), (1, 2, False, 3, set()), (8, 1, True, 2, set()), 
             (4, 4, True, 2, set()), 
             (4, 8, False, 2, set()), (1, 9, False, 1, set()), (9, 8, True, 1, set()), (0, 7, True, 1, set()), 
             (0, 5, False, 1, set())]
    assert is_open_sea(row2, column2, fleet2) == False
    row3 = 3
    column3 = 0
    fleet3 = [(2, 3, False, 4, {(2,4), (2,5)}), (3, 5, True, 3, set()), (2, 0, False, 3, {(3,0), (4,0)}), 
              (8, 4, True, 2, set()), (5, 8, False, 2, set()), 
              (8, 0, False, 2, {(8,0), (9,0)}), (0, 4, False, 1, {(0,4)}), (2, 9, True, 1, set()), (0, 1, False, 1, set()), 
              (0, 8, False, 1, set())]
    assert is_open_sea(row3, column3, fleet3) == False
    row4 = 8
    column4 = 1
    fleet4 = [(5, 0, True, 4, set()), (6, 8, False, 3, set()), (3, 5, False, 3, set()), (4, 8, True, 2, set()), 
              (9, 2, True, 2, {(9,2), (9,3)}), 
              (1, 0, True, 2, set()), (0, 3, False, 1, set()), (7, 2, False, 1, {(7,2)}), (1, 9, True, 1, set()), 
              (8, 0, True, 1, {(8,0)})]
    assert is_open_sea(row4, column4, fleet4) == False
    row5 = 9
    column5 = 9
    fleet5 = [(6, 3, False, 4, set()), (1, 1, False, 3, set()), (3, 6, True, 3, set()), (5, 7, False, 2, set()), 
              (1, 8, True, 2, set()), 
              (9, 0, True, 2, set()), (8, 7, False, 1, set()), (4, 4, True, 1, set()), (6, 5, True, 1, set()), 
              (5, 1, False, 1, set())]
    assert is_open_sea(row5, column5, fleet5) == True

def test_ok_to_place_ship_at1():
    row = 5
    column = 2
    horizontal = False
    length = 4
    fleet = [(1, 1, True, 1, set()), (2, 8, True, 1, set()), (9, 0, True, 1, set()), (8, 9, True, 1, set()),
             (1, 4, False, 2, set()), 
             (0, 7, True, 2, set()), (5, 0, False, 2, set()), (4, 6, True, 3, set()), (7, 6, False, 3, set())]
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

def test_place_ship_at1():
    row = 5
    column = 2
    horizontal = False
    length = 4
    fleet = [(1, 1, True, 1, set()), (2, 8, True, 1, set()), (9, 0, True, 1, set()), (8, 9, True, 1, set()),
             (1, 4, False, 2, set()), 
             (0, 7, True, 2, set()), (5, 0, False, 2, set()), (4, 6, True, 3, set()), (7, 6, False, 3, set())]
    assert place_ship_at(row, column, horizontal, length, fleet) == [(1, 1, True, 1, set()), (2, 8, True, 1, set()), 
             (9, 0, True, 1, set()), (8, 9, True, 1, set()),(1, 4, False, 2, set()), (0, 7, True, 2, set()), 
             (5, 0, False, 2, set()), (4, 6, True, 3, set()), (7, 6, False, 3, set()), (5, 2, False, 4, set())]
    
    #provide at least five tests in total for place_ship_at by the project submission deadline

def test_check_if_hits1():
    row = 4
    column = 7
    fleet = [(1, 1, True, 1, set()), (2, 8, True, 1, set()), (9, 0, True, 1, set()), (8, 9, True, 1, set()),
             (1, 4, False, 2, set()), 
             (0, 7, True, 2, set()), (5, 0, False, 2, set()), (4, 6, True, 3, set()), (7, 6, False, 3, set()), 
             (5, 2, False, 4, set())]
    assert check_if_hits(row, column, fleet) == True
    #provide at least five tests in total for check_if_hits by the project submission deadline

def test_hit1():
    row = 4
    column = 7
    fleet = [(1, 1, True, 1, set()), (2, 8, True, 1, set()), (9, 0, True, 1, set()), (8, 9, True, 1, set()),
             (1, 4, False, 2, set()), 
             (0, 7, True, 2, set()), (5, 0, False, 2, set()), (4, 6, True, 3, set()), (7, 6, False, 3, set()), 
             (5, 2, False, 4, set())]
    assert hit(row, column, fleet) == ([(1, 1, True, 1, set()), (2, 8, True, 1, set()), (9, 0, True, 1, set()), 
                                        (8, 9, True, 1, set()), (1, 4, False, 2, set()), (0, 7, True, 2, set()), 
                                        (5, 0, False, 2, set()), (4, 6, True, 3, {(4,7)}), (7, 6, False, 3, set()), 
                                        (5, 2, False, 4, set())], (4, 6, True, 3, {(4,7)}))
    #provide at least five tests in total for hit by the project submission deadline

def test_are_unsunk_ships_left1():
    fleet1 = [(1, 1, True, 1, set()), (2, 8, True, 1, set()), (9, 0, True, 1, set()), (8, 9, True, 1, set()),
             (1, 4, False, 2, set()), 
             (0, 7, True, 2, set()), (5, 0, False, 2, set()), (4, 6, True, 3, set()), (7, 6, False, 3, set()), 
             (5, 2, False, 4, set())]
    assert are_unsunk_ships_left(fleet1) == True
    fleet2 = [(4, 6, False, 4, {(4,6), (5,6), (6,6), (7,6)}), (0, 5, False, 3, {(0,5), (1,5), (2,5)}), 
              (6, 1, True, 3, {(6,1), (6,2), (6,3)}), (1, 3, False, 2, {(1,3), (2,3)}), (0, 8, False, 2, {(0,8), (1,8)}), 
              (9, 0, True, 2, {(9,0), (9,1)}), (3, 9, False, 1, {(3,9)}), (8, 8, False, 1, {(8,8)}), (2, 1, False, 1, {(2,1)}), 
              (5, 8, False, 1, {(5,8)})]
    assert are_unsunk_ships_left(fleet2) == False
    fleet3 = [(9, 3, True, 4, set()), (3, 5, True, 3, set()), (0, 0, True, 3, set()), (6, 9, False, 2, set()), 
              (0, 7, True, 2, set()), 
              (5, 4, True, 2, set()), (7, 7, True, 1, {(7,7)}), (9, 8, True, 1, {(9,8)}), (7, 4, True, 1, {(7,4)}), 
              (2, 1, True, 1, {(2,1)})]
    assert are_unsunk_ships_left(fleet3) == True
    fleet4 = [(2, 8, False, 4, {(2,8), (3,8), (4,8)}), (6, 0, True, 3, {(6,0), (6, 1)}), (5, 4, True, 3, {(5,4), (5, 5)}),
              (7, 5, False, 2, {(7,5)}), (1, 5, False, 2, {(2,5)}), 
              (3, 1, True, 2, {(3,1)}), (8, 8, False, 1, set()), (1, 2, True, 1, {(1,2)}), (0, 8, False, 1, {(0,8)}), 
              (8, 1, False, 1, set())]
    assert are_unsunk_ships_left(fleet4) == True
    fleet5 = [(5, 6, False, 4, {(5,6), (6,6), (8,6), (7,6)}), (0, 0, False, 3, {(0,0), (0, 1), (0,2)}), 
              (4, 8, False, 3, set()), (7, 2, False, 2, {(7,2), (8,2)}),
              (2, 4, False, 2, {(2,4), (3,4)}), (0, 6, False, 2, {(0,6), (1,6)}), 
              (6, 0, False, 1, {(6,0)}), (5, 2, True, 1, {(5,2)}), (3, 6, False, 1, {(3,6)}), 
              (9, 4, True, 1, {(9,4)})]
    assert are_unsunk_ships_left(fleet5) == True
    
def test_used_squares(): #test for used_squares
    ship = (1, 1, True, 1, set())
    assert used_squares(ship) == set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])