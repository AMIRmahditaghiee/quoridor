# number of rows and columns to make the board
rows_and_columns = 8


def print_game(players_place, walls):
    print('\n'*100)
    for i in range(2*rows_and_columns-1):
        for j in range(2*rows_and_columns-1):
            if i % 2 == 0:
                if j % 2 == 0:
                    if [j//2, i//2] in players_place:
                        print(players_place.index([j//2, i//2])+1, end="")
                    else:
                        print("E", end="")
                else:
                    if ('V', j//2, i//2, i//2+1) in walls or ('V', j//2, i//2-1, i//2)in walls:
                        print("|", end="")
                    else:
                        print(".", end="")
            else:
                if j % 2 == 0:
                    if ('H', i//2, j//2, j//2+1) in walls or ('H', i//2, j//2-1, j//2)in walls:
                        print("-", end="")
                    else:
                        print(".", end="")
                else:
                    if ('V', j//2, i//2, i//2+1) in walls or ('V', j//2, i//2-1, i//2)in walls:
                        print("|", end="")
                    else:
                        print(" ", end="")
        print()


def wall_is_valid(wall, walls):
    if wall in walls or (wall[0], wall[1], wall[2]-1, wall[2])in walls or (wall[0], wall[1], wall[3], wall[3]+1)in walls:
        return False
    if wall[0] == 'V':
        return ('H', wall[2], wall[1], wall[1]+1) not in walls
    elif wall[0] == 'H':
        return ('V', wall[2], wall[1], wall[1]+1) not in walls


def move_is_valid(pose, walls, move_d, other_players):
    if move_d == 'W':
        if pose[1] == 0:
            return False
        if [pose[0], pose[1]-1] in other_players:
            return move_is_valid([pose[0], pose[1]-1], walls, 'W', other_players) or move_is_valid([pose[0], pose[1]-1], walls, 'A', other_players) or move_is_valid([pose[0], pose[1]-1], walls, 'D', other_players)
        return ('H', pose[1]-1, pose[0], pose[0]+1) not in walls and ('H', pose[1]-1, pose[0]-1, pose[0])not in walls
    elif move_d == 'S':
        if pose[1] == 7:
            return False
        if [pose[0], pose[1]+1] in other_players:
            return move_is_valid([pose[0], pose[1]+1], walls, 'S', other_players) or move_is_valid([pose[0], pose[1]+1], walls, 'A', other_players) or move_is_valid([pose[0], pose[1]+1], walls, 'D', other_players)
        return ('H', pose[1]+1, pose[0], pose[0]+1)not in walls and ('H', pose[1]+1, pose[0]-1, pose[0])not in walls
    elif move_d == 'A':
        if pose[0] == 0:
            return False
        if [pose[0]-1, pose[1]] in other_players:
            return move_is_valid([pose[0]-1, pose[1]], walls, 'W', other_players) or move_is_valid([pose[0]-1, pose[1]], walls, 'S', other_players) or move_is_valid([pose[0]-1, pose[1]], walls, 'A', other_players)
        return ('V', pose[0]-1, pose[1], pose[1]+1)not in walls and ('V', pose[0]-1, pose[1]-1, pose[1])not in walls
    elif move_d == 'D':
        if pose[0] == 7:
            return False
        if [pose[0]+1, pose[1]] in other_players:
            return move_is_valid([pose[0]+1, pose[1]], walls, 'W', other_players) or move_is_valid([pose[0]+1, pose[1]], walls, 'S', other_players) or move_is_valid([pose[0]+1, pose[1]], walls, 'D', other_players)
        return ('V', pose[0], pose[1], pose[1]+1)not in walls and ('V', pose[0], pose[1]-1, pose[1])not in walls


def move_player(pose, move_d, walls, other_players):
    if move_d == 'W':
        if [pose[0], pose[1]-1] in other_players:
            if move_is_valid([pose[0], pose[1]-1], walls, 'W', other_players):
                pose[1] -= 1
                move_player(pose, move_d, walls, other_players)
            else:
                print("you can jump ", end="")
                if move_is_valid([pose[0], pose[1]-1], walls, 'A', other_players) and move_is_valid([pose[0], pose[1]-1], walls, 'D', other_players):
                    print("right and left of your opponet")
                    m = None
                    while m not in ['D', 'A']:
                        m = input("select with 'A' and 'D'")
                    move_player([pose[0], pose[1]-1], m, walls, other_players)
                elif move_is_valid([pose[0], pose[1]-1], walls, 'D', other_players):
                    move_player([pose[0], pose[1]-1],
                                'D', walls, other_players)
                elif move_is_valid([pose[0], pose[1]-1], walls, 'A', other_players):
                    move_player([pose[0], pose[1]-1],
                                'A', walls, other_players)
        else:
            pose[1] -= 1
    elif move_d == 'S':
        if [pose[0], pose[1]+1] in other_players:
            if move_is_valid([pose[0], pose[1]+1], walls, 'S', other_players):
                pose[1] += 1
                move_player(pose, move_d, walls, other_players)
            else:
                print("you can jump ", end="")
                if move_is_valid([pose[0], pose[1]+1], walls, 'A', other_players) and move_is_valid([pose[0], pose[1]+1], walls, 'D', other_players):
                    print("right and left of your opponet")
                    m = None
                    while m not in ['D', 'A']:
                        m = input("select with 'A' and 'D'")
                    move_player([pose[0], pose[1]+1], m, walls, other_players)
                elif move_is_valid([pose[0], pose[1]+1], walls, 'D', other_players):
                    move_player([pose[0], pose[1]+1],
                                'D', walls, other_players)
                elif move_is_valid([pose[0], pose[1]+1], walls, 'A', other_players):
                    move_player([pose[0], pose[1]+1],
                                'A', walls, other_players)
        else:
            pose[1] += 1
    elif move_d == 'A':
        if [pose[0]-1, pose[1]] in other_players:
            if move_is_valid([pose[0]-1, pose[1]], walls, 'A', other_players):
                pose[0] -= 1
                move_player(pose, move_d, walls, other_players)
            else:
                print("you can jump ", end="")
                if move_is_valid([pose[0]-1, pose[1]], walls, 'S', other_players) and move_is_valid([pose[0]-1, pose[1]], walls, 'W', other_players):
                    print("right and left of your opponet")
                    m = None
                    while m not in ['S', 'W']:
                        m = input("select with 'S' and 'W'")
                    move_player([pose[0]-1, pose[1]], m, walls, other_players)
                elif move_is_valid([pose[0]-1, pose[1]], walls, 'S', other_players):
                    move_player([pose[0]-1, pose[1]+1],
                                'S', walls, other_players)
                elif move_is_valid([pose[0]-1, pose[1]], walls, 'W', other_players):
                    move_player([pose[0]-1, pose[1]],
                                'W', walls, other_players)
        else:
            pose[0] -= 1
    elif move_d == 'D':
        if [pose[0]+1, pose[1]] in other_players:
            if move_is_valid([pose[0]-1, pose[1]], walls, 'D', other_players):
                pose[0] += 1
                move_player(pose, move_d, walls, other_players)
            else:
                print("you can jump ", end="")
                if move_is_valid([pose[0]+1, pose[1]], walls, 'S', other_players) and move_is_valid([pose[0]+1, pose[1]], walls, 'W', other_players):
                    print("right and left of your opponet")
                    m = None
                    while m not in ['S', 'W']:
                        m = input("select with 'S' and 'W'")
                    move_player([pose[0]+1, pose[1]], m, walls, other_players)
                elif move_is_valid([pose[0]+1, pose[1]], walls, 'S', other_players):
                    move_player([pose[0]+1, pose[1]+1],
                                'S', walls, other_players)
                elif move_is_valid([pose[0]+1, pose[1]], walls, 'W', other_players):
                    move_player([pose[0]+1, pose[1]],
                                'W', walls, other_players)
        else:
            pose[0] += 1


def has_way_to_goal(pose, goal, walls, visited):
    result = False
    visited.append(pose)
    if move_is_valid(pose, walls, 'W', []):
        if [pose[0], pose[1]-1] in goal:
            return True
        elif [pose[0], pose[1]-1] not in visited:
            result = result or has_way_to_goal(
                [pose[0], pose[1]-1], goal, walls, visited)
    if move_is_valid(pose, walls, 'S', []):
        if [pose[0], pose[1]+1] in goal:
            return True
        elif [pose[0], pose[1]+1] not in visited:
            result = result or has_way_to_goal(
                [pose[0], pose[1]+1], goal, walls, visited)
    if move_is_valid(pose, walls, 'A', []):
        if [pose[0]-1, pose[1]] in goal:
            return True
        elif [pose[0]-1, pose[1]] not in visited:
            result = result or has_way_to_goal(
                [pose[0]-1, pose[1]], goal, walls, visited)
    if move_is_valid(pose, walls, 'D', []):
        if [pose[0]+1, pose[1]] in goal:
            return True
        elif [pose[0]+1, pose[1]] not in visited:
            result = result or has_way_to_goal(
                [pose[0]+1, pose[1]], goal, walls, visited)
    return result


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
        if turn == 1:
            invalid_input = True
            print("first player's turn")
            if player_1_walls != 0:
                while invalid_input:
                    print("input 'W' to place 'W'all and 'M' to 'M'OVE player")
                    descission = input()
                    while descission == 'W':
                        print(
                            "input 'H' for 'H'orizontal and 'V' for 'V'ertical walls or input 'A' to 'A'bort and go back")
                        wall_type = input()
                        if wall_type == 'H':
                            print("input row of the wall (0-6)")
                            row = int(input())
                            print(
                                "input two covering columns of the wall seperated by blank(0-7)")
                            l = list(map(int, input().split()))
                            l.sort()
                            c1, c2 = l
                            if c1-c2 != -1:
                                print("invalid wall input")
                            elif wall_is_valid(('H', row, c1, c2), wall_places):
                                wall_places.append(('H', row, c1, c2))
                                player_1_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'V':
                            print("input column of the wall (0-6)")
                            column = int(input())
                            print(
                                "input two covering rows of the wall seperated by blank(0-7)")
                            r1, r2 = list(map(int, input().split()))
                            if (r1-r2 != 1 and r1-r2 != -1):
                                print("invalid wall input")
                            elif wall_is_valid(('V', column, r1, r2), wall_places):
                                wall_places.append(('V', column, r1, r2))
                                player_1_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'A':
                            break
                    else:
                        while descission == 'M':
                            print(
                                "input direction with WASD!(or 'B' to go 'B'ACK)")
                            move_d = input()
                            if move_d == 'B':
                                break
                            elif move_d not in ['W', 'A', 'S', 'D']:
                                print("invalid input")
                            elif move_is_valid(player_1_place, wall_places, move_d, [player_2_place]):
                                move_player(player_1_place, move_d, wall_places,
                                            [player_2_place])
                                invalid_input = False
                                break
                            else:
                                print("can't move that way")
            else:
                while invalid_input:
                    print("input direction with WASD!(You don't have walls anymore!)")
                    move_d = input()
                    if move_d not in ['W', 'A', 'S', 'D']:
                        print("invalid input")
                    elif move_is_valid(player_1_place, wall_places, move_d, [player_2_place]):
                        move_player(player_1_place, move_d,
                                    wall_places, [player_2_place])
                        invalid_input = False
                    else:
                        print("can't move that way")
            turn = 2
        elif turn == 2:
            invalid_input = True
            print("second player's turn")
            if player_2_walls != 0:
                while invalid_input:
                    print("input 'W' to place 'W'all and 'M' to 'M'OVE player")
                    descission = input()
                    while descission == 'W':
                        print(
                            "input 'H' for 'H'orizontal and 'V' for 'V'ertical walls or input 'A' to 'A'bort and go back")
                        wall_type = input()
                        if wall_type == 'H':
                            print("input row of the wall (0-6)")
                            row = int(input())
                            print(
                                "input two covering columns of the wall seperated by blank(0-7)")
                            l = list(map(int, input().split()))
                            l.sort()
                            c1, c2 = l
                            if c1-c2 != -1:
                                print("invalid wall input")
                            elif wall_is_valid(('H', row, c1, c2), wall_places):
                                wall_places.append(('H', row, c1, c2))
                                player_2_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'V':
                            print("input column of the wall (0-6)")
                            column = int(input())
                            print(
                                "input two covering rows of the wall seperated by blank(0-7)")
                            r1, r2 = list(map(int, input().split()))
                            if (r1-r2 != 1 and r1-r2 != -1):
                                print("invalid wall input")
                            elif wall_is_valid(('V', column, r1, r2), wall_places):
                                wall_places.append(('V', column, r1, r2))
                                player_2_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'A':
                            break
                    else:
                        while descission == 'M':
                            print(
                                "input direction with WASD!(or 'B' to go 'B'ACK)")
                            move_d = input()
                            if move_d == 'B':
                                break
                            elif move_d not in ['W', 'A', 'S', 'D']:
                                print("invalid input")
                            elif move_is_valid(player_2_place, wall_places, move_d, [player_1_place]):
                                move_player(player_2_place, move_d, wall_places,
                                            [player_1_place])
                                invalid_input = False
                                break
                            else:
                                print("can't move that way")
            else:
                while invalid_input:
                    print("input direction with WASD!(You don't have walls anymore!)")
                    move_d = input()
                    if move_d not in ['W', 'A', 'S', 'D']:
                        print("invalid input")
                    elif move_is_valid(player_2_place, wall_places, move_d, [player_1_place]):
                        move_player(player_2_place, move_d,
                                    wall_places, [player_1_place])
                        invalid_input = False
                    else:
                        print("can't move that way")
            turn = 1
        if not has_way_to_goal(player_1_place, [[i, 7] for i in range(8)], wall_places, []) or not has_way_to_goal(player_2_place, [[i, 0] for i in range(8)], wall_places, []):
            print("walls are placed in a way which is illegal")
            game_is_over = True
        if player_1_place in [[i, 7] for i in range(8)]:
            print("player 1 won")
            game_is_over = True
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
    goal = [[3, 3], [4, 4], [3, 4], [4, 3]]
    #main game loop
    while not game_is_over:
        print_game([player_1_place, player_2_place,
                    player_3_place, player_4_place], wall_places)
        if turn == 1:
            invalid_input = True
            print("first player's turn")
            if player_1_walls != 0:
                while invalid_input:
                    print("input 'W' to place 'W'all and 'M' to 'M'OVE player")
                    descission = input()
                    while descission == 'W':
                        print(
                            "input 'H' for 'H'orizontal and 'V' for 'V'ertical walls or input 'A' to 'A'bort and go back")
                        wall_type = input()
                        if wall_type == 'H':
                            print("input row of the wall (0-6)")
                            row = int(input())
                            print(
                                "input two covering columns of the wall seperated by blank(0-7)")
                            l = list(map(int, input().split()))
                            l.sort()
                            c1, c2 = l
                            if c1-c2 != -1:
                                print("invalid wall input")
                            elif wall_is_valid(('H', row, c1, c2), wall_places):
                                wall_places.append(('H', row, c1, c2))
                                player_1_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'V':
                            print("input column of the wall (0-6)")
                            column = int(input())
                            print(
                                "input two covering rows of the wall seperated by blank(0-7)")
                            r1, r2 = list(map(int, input().split()))
                            if (r1-r2 != 1 and r1-r2 != -1):
                                print("invalid wall input")
                            elif wall_is_valid(('V', column, r1, r2), wall_places):
                                wall_places.append(('V', column, r1, r2))
                                player_1_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'A':
                            break
                    else:
                        while descission == 'M':
                            print(
                                "input direction with WASD!(or 'B' to go 'B'ACK)")
                            move_d = input()
                            if move_d == 'B':
                                break
                            elif move_d not in ['W', 'A', 'S', 'D']:
                                print("invalid input")
                            elif move_is_valid(player_1_place, wall_places, move_d, [player_2_place, player_3_place, player_4_place]):
                                move_player(player_1_place, move_d, wall_places,
                                            [player_2_place, player_3_place, player_4_place])
                                invalid_input = False
                                break
                            else:
                                print("can't move that way")
            else:
                while invalid_input:
                    print("input direction with WASD!(You don't have walls anymore!)")
                    move_d = input()
                    if move_d not in ['W', 'A', 'S', 'D']:
                        print("invalid input")
                    elif move_is_valid(player_1_place, wall_places, move_d, [player_2_place, player_3_place, player_4_place]):
                        move_player(player_1_place, move_d,
                                    wall_places, [player_2_place, player_3_place, player_4_place])
                        invalid_input = False
                    else:
                        print("can't move that way")
            turn = 2
        elif turn == 2:
            invalid_input = True
            print("second player's turn")
            if player_2_walls != 0:
                while invalid_input:
                    print("input 'W' to place 'W'all and 'M' to 'M'OVE player")
                    descission = input()
                    while descission == 'W':
                        print(
                            "input 'H' for 'H'orizontal and 'V' for 'V'ertical walls or input 'A' to 'A'bort and go back")
                        wall_type = input()
                        if wall_type == 'H':
                            print("input row of the wall (0-6)")
                            row = int(input())
                            print(
                                "input two covering columns of the wall seperated by blank(0-7)")
                            l = list(map(int, input().split()))
                            l.sort()
                            c1, c2 = l
                            if c1-c2 != -1:
                                print("invalid wall input")
                            elif wall_is_valid(('H', row, c1, c2), wall_places):
                                wall_places.append(('H', row, c1, c2))
                                player_2_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'V':
                            print("input column of the wall (0-6)")
                            column = int(input())
                            print(
                                "input two covering rows of the wall seperated by blank(0-7)")
                            r1, r2 = list(map(int, input().split()))
                            if (r1-r2 != 1 and r1-r2 != -1):
                                print("invalid wall input")
                            elif wall_is_valid(('V', column, r1, r2), wall_places):
                                wall_places.append(('V', column, r1, r2))
                                player_2_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'A':
                            break
                    else:
                        while descission == 'M':
                            print(
                                "input direction with WASD!(or 'B' to go 'B'ACK)")
                            move_d = input()
                            if move_d == 'B':
                                break
                            elif move_d not in ['W', 'A', 'S', 'D']:
                                print("invalid input")
                            elif move_is_valid(player_2_place, wall_places, move_d, [player_1_place, player_3_place, player_4_place]):
                                move_player(player_2_place, move_d, wall_places,
                                            [player_1_place, player_3_place, player_4_place])
                                invalid_input = False
                                break
                            else:
                                print("can't move that way")
            else:
                while invalid_input:
                    print("input direction with WASD!(You don't have walls anymore!)")
                    move_d = input()
                    if move_d not in ['W', 'A', 'S', 'D']:
                        print("invalid input")
                    elif move_is_valid(player_2_place, wall_places, move_d, [player_1_place, player_3_place, player_4_place]):
                        move_player(player_2_place, move_d,
                                    wall_places, [player_1_place, player_3_place, player_4_place])
                        invalid_input = False
                    else:
                        print("can't move that way")
            turn = 3
        elif turn == 3:
            invalid_input = True
            print("third player's turn")
            if player_3_walls != 0:
                while invalid_input:
                    print("input 'W' to place 'W'all and 'M' to 'M'OVE player")
                    descission = input()
                    while descission == 'W':
                        print(
                            "input 'H' for 'H'orizontal and 'V' for 'V'ertical walls or input 'A' to 'A'bort and go back")
                        wall_type = input()
                        if wall_type == 'H':
                            print("input row of the wall (0-6)")
                            row = int(input())
                            print(
                                "input two covering columns of the wall seperated by blank(0-7)")
                            l = list(map(int, input().split()))
                            l.sort()
                            c1, c2 = l
                            if c1-c2 != -1:
                                print("invalid wall input")
                            elif wall_is_valid(('H', row, c1, c2), wall_places):
                                wall_places.append(('H', row, c1, c2))
                                player_3_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'V':
                            print("input column of the wall (0-6)")
                            column = int(input())
                            print(
                                "input two covering rows of the wall seperated by blank(0-7)")
                            r1, r2 = list(map(int, input().split()))
                            if (r1-r2 != 1 and r1-r2 != -1):
                                print("invalid wall input")
                            elif wall_is_valid(('V', column, r1, r2), wall_places):
                                wall_places.append(('V', column, r1, r2))
                                player_3_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'A':
                            break
                    else:
                        while descission == 'M':
                            print(
                                "input direction with WASD!(or 'B' to go 'B'ACK)")
                            move_d = input()
                            if move_d == 'B':
                                break
                            elif move_d not in ['W', 'A', 'S', 'D']:
                                print("invalid input")
                            elif move_is_valid(player_3_place, wall_places, move_d, [player_1_place, player_2_place, player_4_place]):
                                move_player(player_3_place, move_d, wall_places,
                                            [player_1_place, player_2_place, player_4_place])
                                invalid_input = False
                                break
                            else:
                                print("can't move that way")
            else:
                while invalid_input:
                    print("input direction with WASD!(You don't have walls anymore!)")
                    move_d = input()
                    if move_d not in ['W', 'A', 'S', 'D']:
                        print("invalid input")
                    elif move_is_valid(player_3_place, wall_places, move_d, [player_1_place, player_2_place, player_4_place]):
                        move_player(player_3_place, move_d,
                                    wall_places, [player_1_place, player_2_place, player_4_place])
                        invalid_input = False
                    else:
                        print("can't move that way")
            turn = 4
        elif turn == 4:
            invalid_input = True
            print("fourth player's turn")
            if player_4_walls != 0:
                while invalid_input:
                    print("input 'W' to place 'W'all and 'M' to 'M'OVE player")
                    descission = input()
                    while descission == 'W':
                        print(
                            "input 'H' for 'H'orizontal and 'V' for 'V'ertical walls or input 'A' to 'A'bort and go back")
                        wall_type = input()
                        if wall_type == 'H':
                            print("input row of the wall (0-6)")
                            row = int(input())
                            print(
                                "input two covering columns of the wall seperated by blank(0-7)")
                            l = list(map(int, input().split()))
                            l.sort()
                            c1, c2 = l
                            if c1-c2 != -1:
                                print("invalid wall input")
                            elif wall_is_valid(('H', row, c1, c2), wall_places):
                                wall_places.append(('H', row, c1, c2))
                                player_4_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'V':
                            print("input column of the wall (0-6)")
                            column = int(input())
                            print(
                                "input two covering rows of the wall seperated by blank(0-7)")
                            r1, r2 = list(map(int, input().split()))
                            if (r1-r2 != 1 and r1-r2 != -1):
                                print("invalid wall input")
                            elif wall_is_valid(('V', column, r1, r2), wall_places):
                                wall_places.append(('V', column, r1, r2))
                                player_4_walls -= 1
                                invalid_input = False
                                break
                            else:
                                print("can't place wall there")
                        elif wall_type == 'A':
                            break
                    else:
                        while descission == 'M':
                            print(
                                "input direction with WASD!(or 'B' to go 'B'ACK)")
                            move_d = input()
                            if move_d == 'B':
                                break
                            elif move_d not in ['W', 'A', 'S', 'D']:
                                print("invalid input")
                            elif move_is_valid(player_4_place, wall_places, move_d, [player_1_place, player_2_place, player_3_place]):
                                move_player(player_4_place, move_d, wall_places,
                                            [player_1_place, player_2_place, player_3_place])
                                invalid_input = False
                                break
                            else:
                                print("can't move that way")
            else:
                while invalid_input:
                    print("input direction with WASD!(You don't have walls anymore!)")
                    move_d = input()
                    if move_d not in ['W', 'A', 'S', 'D']:
                        print("invalid input")
                    elif move_is_valid(player_4_place, wall_places, move_d, [player_1_place, player_2_place, player_3_place]):
                        move_player(player_4_place, move_d,
                                    wall_places, [player_1_place, player_2_place, player_3_place])
                        invalid_input = False
                    else:
                        print("can't move that way")
            turn = 1

        if not has_way_to_goal(player_1_place, goal, wall_places, []) or not has_way_to_goal(player_2_place, goal, wall_places, [])or not has_way_to_goal(player_3_place, goal, wall_places, [])or not has_way_to_goal(player_3_place, goal, wall_places, []):
            print("walls are placed in a way which is illegal")
            game_is_over = True
        if player_1_place in goal:
            print("player 1 won")
            game_is_over = True
        if player_2_place in goal:
            print("player 2 won")
            game_is_over = True
        if player_3_place in goal:
            print("player 3 won")
            game_is_over = True
        if player_4_place in goal:
            print("player 4 won")
            game_is_over = True


game_mode = input("enter 4 for four players and 2 for two players")
if game_mode == '4':
    four_player_game()
elif game_mode == '2':
    two_player_game()

print("GOODBYE")
