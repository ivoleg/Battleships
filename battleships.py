#see the readme.md file for description and data 


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

def filled_squares(ship): #function find and store as set of tuples all the squares of the given ship and its adjacent squares
    set_of_squares = set()
    if ship[2] == True:
        for i in range(ship[0] - 1, ship[0] + 2):
            for j in range(ship[1] - 1, ship[1] + ship[3] + 1):
                square = (i,j)
                set_of_squares.add(square)
    elif ship[2] == False:
        for i in range(ship[0] - 1, ship[0] + ship[3] + 1):
            for j in range(ship[1] - 1, ship[1] + 2):
                square = (i,j)
                set_of_squares.add(square)
    return set_of_squares

def is_open_sea(row, column, fleet):
    square = (row, column)
    all_filled_squares = set()
    for ship in fleet:
        ship_squares = filled_squares(ship)
        all_filled_squares.update(ship_squares)
    if square in all_filled_squares:
        return False
    else:
        return True


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    #remove pass and add your implementation
    pass

def place_ship_at(row, column, horizontal, length, fleet):
    #remove pass and add your implementation
    pass

def randomly_place_all_ships():
    #remove pass and add your implementation
    pass

def check_if_hits(row, column, fleet):
    #remove pass and add your implementation
    pass

def hit(row, column, fleet):
    #remove pass and add your implementation
    pass

def are_unsunk_ships_left(fleet):
    #remove pass and add your implementation
    pass

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()    
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_shis_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
