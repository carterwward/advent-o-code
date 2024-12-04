import os
import numpy as np

word = "XMAS"

def check_word(i, j, i_mod, j_mod, char_index, xmas_grid, previous_coords):
    i += i_mod
    j += j_mod
    if i >= 0 and j >= 0 and i < xmas_grid.shape[0] and j < xmas_grid.shape[1]:
        is_match = xmas_grid[i, j] == word[char_index]
    else:
        return False

    if is_match and char_index < len(word) - 1:
        previous_coords.append((i,j))
        return check_word(i, j, i_mod, j_mod, char_index + 1, xmas_grid, previous_coords)
    elif is_match and char_index == len(word) - 1:
        previous_coords.append((i, j))
        return True
    return False

if __name__ == "__main__":
    filepath = os.path.join("data", "search.txt")
    with open(filepath, "r") as file:
        words = file.readlines()
    xmas_grid = np.array([np.array(list(line.rstrip("\n"))) for line in words])
    total_matches = 0
    for i in range(xmas_grid.shape[0]):
        for j in range(xmas_grid.shape[1]):
            char_index = 0
            directions = [(- 1, 0), (- 1, - 1), (0, - 1), (1, - 1), (1, 0), (1, 1), (0, 1), (- 1, 1)]
            if xmas_grid[i,j] == word[0]:
                for direction in directions:
                    full_match = check_word(i, j, direction[0], direction[1], 1, xmas_grid, [(i,j)])
                    if full_match:
                        total_matches += 1
    print(total_matches)
