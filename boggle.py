def make_grid(width, height):
    """
    Creats a grid that will hold all of the tiles
    for boggle game
    """
    return {(row, col): ' ' for row in range(height)
        for col in range(width)}
    