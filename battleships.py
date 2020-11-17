### see the readme.md file for description and data 
import copy
import random

def is_sunk(ship):
    if ship[3] == len(ship[4]):
        return True
    else:
        return False

def ship_type(ship):
    if ship[3] == 4:
        return 'battleship'
    elif ship[3] == 3:
        return 'cruiser'
    elif ship[3] == 2:
        return 'destroyer'
    else:
        return 'submarine'

def used_squares(ship): #function find and store as set of tuples all the squares of the given ship and its adjacent squares
    set_of_squares = set()
    if ship[2] == True:
        for i in range(ship[0] - 1, ship[0] + 2):
            for j in range(ship[1] - 1, ship[1] + ship[3] + 1):
                set_of_squares.add((i, j))
    else:
        for i in range(ship[0] - 1, ship[0] + ship[3] + 1):
            for j in range(ship[1] - 1, ship[1] + 2):
                set_of_squares.add((i, j))
    return set_of_squares

def is_open_sea(row, column, fleet):
    square = (row, column)
    all_used_squares = set()
    for ship in fleet:
        used_ship_squares = used_squares(ship)
        all_used_squares.update(used_ship_squares)
    if square in all_used_squares:
        return False
    else:
        return True

def ship_squares(ship): #function stores only ship squares as a set of tuples
    ship_sq = set()
    if ship[2] == True:
        for i in range(ship[1], ship[1] + ship[3]):
            ship_sq.add((ship[0], i))
    else:
        for i in range(ship[0], ship[0] + ship[3]):
            ship_sq.add((i, ship[1]))
    return ship_sq

def fleet_squares(fleet): #function stores fleet as a set of tuples
    fleet_sq = set()
    for ship in fleet:
        fleet_sq.update(ship_squares(ship))
    return fleet_sq
    
def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    ship = (row, column, horizontal, length, set())
    if used_squares(ship).intersection(fleet_squares(fleet)) == set():
        return True
    else:
        return False

def place_ship_at(row, column, horizontal, length, fleet):
    new_fleet = copy.deepcopy(fleet)
    new_fleet.append((row, column, horizontal, length, set()))
    return new_fleet

def randomly_place_all_ships():
    fleet = []
    for i in range(4, 0, -1):
        for j in range(1, 6 - i):
            placed = False
            while not placed:
                horizontal = bool(random.getrandbits(1))
                if horizontal == True:
                    row = random.randint(0, 9)
                    column = random.randint(0, 10 - i)
                else:
                    row = random.randint(0, 10 - i)
                    column = random.randint(0, 9)
                length = i
                hits = set()
                if ok_to_place_ship_at(row, column, horizontal, length, fleet):
                    fleet = place_ship_at(row, column, horizontal, length, fleet)
                    placed = True
    return fleet

def check_if_hits(row, column, fleet):
    hit_square = (row, column)
    hit = 0
    for ship in fleet:
        if hit_square in ship_squares(ship) and hit_square not in ship[4]:
            hit = 1
    if hit == 1:
        return True
    else:
        return False
def hit(row, column, fleet):
    for ship in fleet:
        if (row, column) in ship_squares(ship): #and (row, column) not in ship[4]:
            ship_hit = ship
    ship_hit[4].add((row, column))
    return (fleet, ship_hit)
        
def are_unsunk_ships_left(fleet):
    counter = 0
    for ship in fleet:
        if is_sunk(ship):
            counter+=1
    if counter == 10:
        return False
    else:
        return True

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0
    print("You can end game at any time, by entering END")
    while not game_over:
        input_str = input("Enter row and colum to shoot (separted by space): ")
        if input_str == 'END':
            game_over = True
            print("Game over")
        else:
            try:
                loc_str = input_str.split()
                current_row = int(loc_str[0])
                current_column = int(loc_str[1])
                if (-1 < current_row < 10 and -1 < current_column < 10):
                    shots += 1
                    if check_if_hits(current_row, current_column, current_fleet):
                        print("You have a hit!")
                        (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                        if is_sunk(ship_hit):
                            print("You sank a " + ship_type(ship_hit) + "!")
                    else:
                        print("You missed!")
                else:
                    print("This square does not exist")
            except:
                print("Please, use correct input")
                
        if not are_unsunk_ships_left(current_fleet):
                game_over = True
                print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
