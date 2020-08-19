# number of rows and columns to make the board
rows_and_columns = 8

#print game in terminal


def print_game(players_place, walls):
    #print 100 enter to clear screen
    print('\n'*100)
    #line iterator
    for i in range(2*rows_and_columns-1):
        #chracter iterator
        for j in range(2*rows_and_columns-1):
            #check if line includes game board space
            if i % 2 == 0:
                #check if current character
                if j % 2 == 0:
                    #check if current space is occupide
                    if [j//2, i//2] in players_place:
                        #print the player
                        print(players_place.index([j//2, i//2])+1, end="")
                    #if it isn't prints E
                    else:
                        print("E", end="")
                #if charcter is wall place
                else:
                    #check if there is a wall
                    if ('V', j//2, i//2, i//2+1) in walls or ('V', j//2, i//2-1, i//2)in walls:
                        print("|", end="")
                    #if not print .
                    else:
                        print(".", end="")
            #if line is all wall places
            else:
                #if it's a horizontal wall place
                if j % 2 == 0:
                    #if there is a wall
                    if ('H', i//2, j//2, j//2+1) in walls or ('H', i//2, j//2-1, j//2)in walls:
                        print("-", end="")
                    #if there isn't
                    else:
                        print(".", end="")
                #if it's a vertical wall place
                else:
                    #if there's wall
                    if ('V', j//2, i//2, i//2+1) in walls or ('V', j//2, i//2-1, i//2)in walls:
                        print("|", end="")
                    #if there isn't
                    else:
                        print(" ", end="")
        #go to next line
        print()

#check if you can place a wall


def wall_is_valid(wall, walls):
    #check if wall places is already occupide
    if wall in walls or (wall[0], wall[1], wall[2]-1, wall[2])in walls or (wall[0], wall[1], wall[3], wall[3]+1)in walls:
        return False
    #check if it has collision with other wall
    if wall[0] == 'V':
        return ('H', wall[2], wall[1], wall[1]+1) not in walls
    elif wall[0] == 'H':
        return ('V', wall[2], wall[1], wall[1]+1) not in walls

#check if player can move in move_d direction


def move_is_valid(pose, walls, move_d, other_players):
    #check if direction is upward
    if move_d == 'W':
        #check if player is in the first row
        if pose[1] == 0:
            return False
        #check if there is a player in upper space
        if [pose[0], pose[1]-1] in other_players:
            #returns if can jump over other player
            return move_is_valid([pose[0], pose[1]-1], walls, 'W', other_players) or move_is_valid([pose[0], pose[1]-1], walls, 'A', other_players) or move_is_valid([pose[0], pose[1]-1], walls, 'D', other_players)
        #check if a wall is blocking its way
        return ('H', pose[1]-1, pose[0], pose[0]+1) not in walls and ('H', pose[1]-1, pose[0]-1, pose[0])not in walls
    #check if direction is down ward
    elif move_d == 'S':
        #check if player is in last row
        if pose[1] == 7:
            return False
        #check if there is a player in bottom space
        if [pose[0], pose[1]+1] in other_players:
            #returns if can jump over other player
            return move_is_valid([pose[0], pose[1]+1], walls, 'S', other_players) or move_is_valid([pose[0], pose[1]+1], walls, 'A', other_players) or move_is_valid([pose[0], pose[1]+1], walls, 'D', other_players)
        #check if a wall is blocking its way
        return ('H', pose[1]+1, pose[0], pose[0]+1)not in walls and ('H', pose[1]+1, pose[0]-1, pose[0])not in walls
    #check if direction is to the right
    elif move_d == 'A':
        #check if player is in the first column
        if pose[0] == 0:
            return False
        #check if there is a player in right side space
        if [pose[0]-1, pose[1]] in other_players:
            #returns if can jump over other player
            return move_is_valid([pose[0]-1, pose[1]], walls, 'W', other_players) or move_is_valid([pose[0]-1, pose[1]], walls, 'S', other_players) or move_is_valid([pose[0]-1, pose[1]], walls, 'A', other_players)
        #check if a wall is blocking its way
        return ('V', pose[0]-1, pose[1], pose[1]+1)not in walls and ('V', pose[0]-1, pose[1]-1, pose[1])not in walls
    #check if direction is to the left
    elif move_d == 'D':
        #check if player is in the first column
        if pose[0] == 7:
            return False
        #check if there is a player in left side space
        if [pose[0]+1, pose[1]] in other_players:
            #returns if can jump over other player
            return move_is_valid([pose[0]+1, pose[1]], walls, 'W', other_players) or move_is_valid([pose[0]+1, pose[1]], walls, 'S', other_players) or move_is_valid([pose[0]+1, pose[1]], walls, 'D', other_players)
        #check if a wall is blocking its way
        return ('V', pose[0], pose[1], pose[1]+1)not in walls and ('V', pose[0], pose[1]-1, pose[1])not in walls

#function to apply movement


def move_player(pose, move_d, walls, other_players):
    #check if direction is upward
    if move_d == 'W':
        #check if there is a player in upper space
        if [pose[0], pose[1]-1] in other_players:
            #check if can jump over other player to upside
            if move_is_valid([pose[0], pose[1]-1], walls, 'W', other_players):
                pose[1] -= 1
                #do the jump
                move_player(pose, move_d, walls, other_players)
            else:
                print("you can jump ", end="")
                #check if can jump to the right and left of opponet
                if move_is_valid([pose[0], pose[1]-1], walls, 'A', other_players) and move_is_valid([pose[0], pose[1]-1], walls, 'D', other_players):
                    print("right and left of your opponet")
                    m = None
                    #let player choose which side to jump
                    while m not in ['D', 'A']:
                        m = input("select with 'A' and 'D'")
                    move_player([pose[0], pose[1]-1], m, walls, other_players)
                #if only one side jump is valid jump that way
                elif move_is_valid([pose[0], pose[1]-1], walls, 'D', other_players):
                    move_player([pose[0], pose[1]-1],
                                'D', walls, other_players)
                elif move_is_valid([pose[0], pose[1]-1], walls, 'A', other_players):
                    move_player([pose[0], pose[1]-1],
                                'A', walls, other_players)
        #move if there is no player
        else:
            pose[1] -= 1
    #check if direction is upward
    elif move_d == 'S':
        #check if there is a player in bottom space
        if [pose[0], pose[1]+1] in other_players:
            #check if can jump over other player to downside
            if move_is_valid([pose[0], pose[1]+1], walls, 'S', other_players):
                #do the jump
                pose[1] += 1
                move_player(pose, move_d, walls, other_players)
            else:
                print("you can jump ", end="")
                #check if can jump to the right and left of opponet
                if move_is_valid([pose[0], pose[1]+1], walls, 'A', other_players) and move_is_valid([pose[0], pose[1]+1], walls, 'D', other_players):
                    print("right and left of your opponet")
                    m = None
                    #let player choose which side to jump
                    while m not in ['D', 'A']:
                        m = input("select with 'A' and 'D'")
                    move_player([pose[0], pose[1]+1], m, walls, other_players)
                #if only one side jump is valid jump that way
                elif move_is_valid([pose[0], pose[1]+1], walls, 'D', other_players):
                    move_player([pose[0], pose[1]+1],
                                'D', walls, other_players)
                elif move_is_valid([pose[0], pose[1]+1], walls, 'A', other_players):
                    move_player([pose[0], pose[1]+1],
                                'A', walls, other_players)
        #move if there is no player
        else:
            pose[1] += 1
    #check if direction is to rightside
    elif move_d == 'A':
        #check if there is a player in rightside space
        if [pose[0]-1, pose[1]] in other_players:
            #check if can jump over other player to rightside
            if move_is_valid([pose[0]-1, pose[1]], walls, 'A', other_players):
                #do the jump
                pose[0] -= 1
                move_player(pose, move_d, walls, other_players)
            else:
                print("you can jump ", end="")
                #check if can jump to the up and down of opponet
                if move_is_valid([pose[0]-1, pose[1]], walls, 'S', other_players) and move_is_valid([pose[0]-1, pose[1]], walls, 'W', other_players):
                    print("right and left of your opponet")
                    m = None
                    #let player choose which side to jump
                    while m not in ['S', 'W']:
                        m = input("select with 'S' and 'W'")
                    move_player([pose[0]-1, pose[1]], m, walls, other_players)
                #if only one side jump is valid jump that way
                elif move_is_valid([pose[0]-1, pose[1]], walls, 'S', other_players):
                    move_player([pose[0]-1, pose[1]+1],
                                'S', walls, other_players)
                elif move_is_valid([pose[0]-1, pose[1]], walls, 'W', other_players):
                    move_player([pose[0]-1, pose[1]],
                                'W', walls, other_players)
        #move if there is no player
        else:
            pose[0] -= 1
    #check if direction is to rightside
    elif move_d == 'D':
        if [pose[0]+1, pose[1]] in other_players:
            #check if there is a player in leftside space
            if move_is_valid([pose[0]-1, pose[1]], walls, 'D', other_players):
                #do the jump
                pose[0] += 1
                move_player(pose, move_d, walls, other_players)
            else:
                print("you can jump ", end="")
                #check if can jump to the up and down of opponet
                if move_is_valid([pose[0]+1, pose[1]], walls, 'S', other_players) and move_is_valid([pose[0]+1, pose[1]], walls, 'W', other_players):
                    print("right and left of your opponet")
                    m = None
                    #let player choose which side to jump
                    while m not in ['S', 'W']:
                        m = input("select with 'S' and 'W'")
                    move_player([pose[0]+1, pose[1]], m, walls, other_players)
                #if only one side jump is valid jump that way
                elif move_is_valid([pose[0]+1, pose[1]], walls, 'S', other_players):
                    move_player([pose[0]+1, pose[1]+1],
                                'S', walls, other_players)
                elif move_is_valid([pose[0]+1, pose[1]], walls, 'W', other_players):
                    move_player([pose[0]+1, pose[1]],
                                'W', walls, other_players)
        #move if there is no player
        else:
            pose[0] += 1

#check recursively if ther is still a way to goal and path is not blocked using dfs


def has_way_to_goal(pose, goal, walls, visited):
    #remember the place to not visit it again
    visited.append(pose)
    #check available moves and if they reach the goal
    if move_is_valid(pose, walls, 'W', []):
        if [pose[0], pose[1]-1] in goal:
            return True
        elif [pose[0], pose[1]-1] not in visited:
            if has_way_to_goal([pose[0], pose[1]-1], goal, walls, visited):
                return True

    if move_is_valid(pose, walls, 'S', []):
        if [pose[0], pose[1]+1] in goal:
            return True
        elif [pose[0], pose[1]+1] not in visited:
            if has_way_to_goal([pose[0], pose[1]+1], goal, walls, visited):
                return True
    if move_is_valid(pose, walls, 'A', []):
        if [pose[0]-1, pose[1]] in goal:
            return True
        elif [pose[0]-1, pose[1]] not in visited:
            if has_way_to_goal([pose[0]-1, pose[1]], goal, walls, visited):
                return True
    if move_is_valid(pose, walls, 'D', []):
        if [pose[0]+1, pose[1]] in goal:
            return True
        elif [pose[0]+1, pose[1]] not in visited:
            if has_way_to_goal([pose[0]+1, pose[1]], goal, walls, visited):
                return True
    return False

#to run a persons turn


def player_turn(player, walls, player_walls, other_players, n):
    #declare whose turn it is
    print(n, " player's turn")
    #check if player has walls left
    if player_walls != 0:
        #a loop to run until a valid move is made
        while True:
            #let player decide to put a wall or make a move
            print("input 'W' to place 'W'all and 'M' to 'M'OVE player")
            descission = input()
            #a loop to run until a valid wall data is given
            while descission == 'W':
                #let player decide if want to cancel putting a wall or decide type of wall
                print(
                    "input 'H' for 'H'orizontal and 'V' for 'V'ertical walls or input 'A' to 'A'bort and go back")
                wall_type = input()
                #if player want to put a horizontal wall
                if wall_type == 'H':
                    #get wall data
                    print("input row of the wall (0-6)")
                    row = int(input())
                    print(
                        "input two covering columns of the wall seperated by blank(0-7)")
                    l = list(map(int, input().split()))
                    l.sort()
                    c1, c2 = l
                    #check wall is valid
                    if c1-c2 != -1:
                        print("invalid wall input")
                    elif wall_is_valid(('H', row, c1, c2), walls):
                        #put wall if valid
                        walls.append(('H', row, c1, c2))
                        return player_walls-1
                    else:
                        print("can't place wall there")
                #if player want to put a vertical wall
                elif wall_type == 'V':
                    #get wall data
                    print("input column of the wall (0-6)")
                    column = int(input())
                    print(
                        "input two covering rows of the wall seperated by blank(0-7)")
                    l = list(map(int, input().split()))
                    l.sort()
                    r1, r2 = l
                    #check wall is valid
                    if r1-r2 != -1:
                        print("invalid wall input")
                    elif wall_is_valid(('V', column, r1, r2), walls):
                        #put wall if valid
                        walls.append(('V', column, r1, r2))
                        return player_walls-1
                    else:
                        print("can't place wall there")
                #cancel putting a wall
                elif wall_type == 'A':
                    break
            #if player wants to make a move
            else:
                while descission == 'M':
                    #let player decide if want to go back or choose a direction
                    print(
                        "input direction with WASD!(or 'B' to go 'B'ACK)")
                    move_d = input()
                    #go back
                    if move_d == 'B':
                        break
                    #check if input is valid
                    elif move_d not in ['W', 'A', 'S', 'D']:
                        print("invalid input")
                    #check if move is valid
                    elif move_is_valid(player, walls, move_d, other_players):
                        #make the move
                        move_player(player, move_d, walls, other_players)
                        return player_walls
                    else:
                        print("can't move that way")
    #if player has no walls left
    else:
        while True:
            #let player decide the direction
            print("input direction with WASD!(You don't have walls anymore!)")
            move_d = input()
            #check if input is valid
            if move_d not in ['W', 'A', 'S', 'D']:
                print("invalid input")
            #check if move is valid
            elif move_is_valid(player, walls, move_d, other_players):
                #make move
                move_player(player, move_d, walls, other_players)
                return player_walls
            else:
                print("can't move that way")


#function to play game as two player
def two_player_game():
    #declaring players starting places and walls
    player_1_place = [3, 0]
    player_2_place = [4, 7]
    player_1_walls = 5
    player_2_walls = 5
    #declaring game variables
    game_is_over = False
    wall_places = []
    turn = 1
    #main game loop
    while not game_is_over:
        print_game([player_1_place, player_2_place], wall_places)
        #if it's 1st player turn
        if turn == 1:
            player_1_walls = player_turn(
                player_1_place, wall_places, player_1_walls, [player_2_place], turn)
            #pass the turn
            turn = 2
        #if it's 2nd player turn
        elif turn == 2:
            player_2_walls = player_turn(
                player_2_place, wall_places, player_2_walls, [player_1_place], turn)
            #pass the turn
            turn = 1
        #if walls are place legally
        if not has_way_to_goal(player_1_place, [[i, 7] for i in range(8)], wall_places, []) or not has_way_to_goal(player_2_place, [[i, 0] for i in range(8)], wall_places, []):
            print("walls are placed in a way which is illegal")
            game_is_over = True
        #if 1st won
        if player_1_place in [[i, 7] for i in range(8)]:
            print("player 1 won")
            game_is_over = True
        #if 2nd won
        if player_2_place in [[i, 0] for i in range(8)]:
            print("player 2 won")
            game_is_over = True


def four_player_game():
    #declaring players starting places and walls
    player_1_place = [3, 0]
    player_2_place = [4, 7]
    player_3_place = [0, 3]
    player_4_place = [7, 4]
    player_1_walls = 5
    player_2_walls = 5
    player_3_walls = 5
    player_4_walls = 5
    #declaring game variables
    game_is_over = False
    wall_places = []
    turn = 1
    #set the middle goal
    goal = [[[i, 7] for i in range(8)], [[i, 0] for i in range(8)], [
        [7, i] for i in range(8)], [[0, i] for i in range(8)]]
    #main game loop
    while not game_is_over:
        print_game([player_1_place, player_2_place,
                    player_3_place, player_4_place], wall_places)
        #if it's 1st player turn
        if turn == 1:
            player_1_walls = player_turn(player_1_place, wall_places, player_1_walls, [
                                         player_2_place, player_3_place, player_4_place], turn)
            #pass the turn
            turn = 2
        #if it's 2nd player turn
        elif turn == 2:
            player_2_walls = player_turn(player_2_place, wall_places, player_2_walls, [
                                         player_1_place, player_3_place, player_4_place], turn)
            #pass the turn
            turn = 3
        #if it's 3rd player turn
        elif turn == 3:
            player_3_walls = player_turn(player_3_place, wall_places, player_3_walls, [
                                         player_1_place, player_2_place, player_4_place], turn)
            #pass the turn
            turn = 4
        #if it's 4th player turn
        elif turn == 4:
            player_4_walls = player_turn(player_4_place, wall_places, player_4_walls, [
                                         player_1_place, player_2_place, player_3_place], turn)
            #pass the turn
            turn = 1
        #if walls are place legally
        if not has_way_to_goal(player_1_place, goal[0], wall_places, []) or not has_way_to_goal(player_2_place, goal[1], wall_places, [])or not has_way_to_goal(player_3_place, goal[2], wall_places, [])or not has_way_to_goal(player_4_place, goal[3], wall_places, []):
            print("walls are placed in a way which is illegal")
            game_is_over = True
        #if it's 1st player won
        if player_1_place in goal[0]:
            print("player 1 won")
            game_is_over = True
        #if it's 2nd player won
        if player_2_place in goal[1]:
            print("player 2 won")
            game_is_over = True
        #if it's 3rd player won
        if player_3_place in goal[2]:
            print("player 3 won")
            game_is_over = True
        #if it's 4th player
        if player_4_place in goal[3]:
            print("player 4 won")
            game_is_over = True


#let client decide game mode
game_mode = input("enter 4 for four players and 2 for two players")
if game_mode == '4':
    four_player_game()
elif game_mode == '2':
    two_player_game()

print("GOODBYE")
