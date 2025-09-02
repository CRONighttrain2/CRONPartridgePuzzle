import Tree

def node(filled_lengths_map: dict[int, list[str]], side_lengths_map: dict[int, int], current_row: str, current_length: int, target_length: int):
    length_difference: int = target_length - current_length
    available_side_lengths = Tree.get_available_side_lengths(side_lengths_map)
    if not filled_lengths_map.keys().__contains__(target_length):
        filled_lengths_map[target_length] = []
    if current_length == target_length:
        filled_lengths_map[target_length].append(current_row)
    #if we have already calculated the states for the rest of a partially filled row insert those plus the row into the map
    if filled_lengths_map.keys().__contains__(length_difference) and current_length != 0:
        for row in filled_lengths_map[length_difference]:
            #check to see if we are going to use too many of one number and go to the next row if we do
            if not valid_row(row, side_lengths_map):
                continue
            new_row = current_row + row
            #if there is a 1 in the new row and the one isn't at the front or back then the row is invalid due to us only having one 1
            if new_row.__contains__("1") and not (new_row[0] == "1" or new_row[len(new_row)-1] == "1"):
                continue
            filled_lengths_map[target_length].append(new_row)
    else:
        new_lengths = []
        for side_length in available_side_lengths:
            if int(side_length) <= length_difference:
                new_lengths.append(side_length)
        available_side_lengths = new_lengths
        for side_length in available_side_lengths:
            new_row =  current_row + str(side_length)
            new_length = current_length + side_length
            new_map = side_lengths_map.copy()
            new_map[side_length] -= 1
            node(filled_lengths_map, new_map, new_row, new_length, target_length)

def get_number_count_in_row(row: str)-> dict[int, int]:
    output: dict[int,int] = dict()
    for char in row:
        if not output.keys().__contains__(int(char)):
            output[int(char)] = 0
        output[int(char)] += 1
    return output

def valid_row(row: str, side_lengths_map: dict[int, int]) -> bool:
    numbers_in_row: dict[int, int] = get_number_count_in_row(row)
    check_map: dict[int, int] = side_lengths_map.copy()
    for key in numbers_in_row.keys():
        check_map[key] -= numbers_in_row[key]
    for key in check_map.keys():
        if check_map[key] < 0:
            return False
    return True
