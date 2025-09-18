def analyze(chess, display=True):
    grid = [list(row) for row in chess.splitlines()]
    rows, cols = len(grid), len(grid[0]) if grid else 0

    def sweep(r, c, moves, blockers):
        for dr, dc in moves:
            x, y = r + dr, c + dc
            while 0 <= x < rows and 0 <= y < cols:
                val = grid[x][y]
                if val == ".":
                    grid[x][y] = "X"
                elif val not in blockers:
                    grid[x][y] = val.replace("X", "") + "X"
                if val in blockers:
                    grid[x][y] = val.replace("X", "") + "X"
                    break
                x += dr
                y += dc

    for r in range(rows):
        for c in range(cols):
            piece = grid[r][c].replace("X", "")
            if piece == "R":
                sweep(r, c, [(-1,0),(1,0),(0,-1),(0,1)], {"B","R","P"})
            elif piece == "B":
                sweep(r, c, [(-1,-1),(-1,1),(1,-1),(1,1)], {"B","R","P"})
            elif piece == "Q":
                sweep(r, c,
                      [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)],
                      {"B","R","P","Q"})
            elif piece == "P":
                for dc in [-1, 1]:
                    nr, nc = r-1, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        tgt = grid[nr][nc]
                        grid[nr][nc] = "X" if tgt == "." else tgt.replace("X", "") + "X"
                grid[r][c] = "PX"  

    for r in range(rows):
        for c in range(cols):
            if grid[r][c].replace("X", "") == "K":
                if "X" in grid[r][c]:
                    grid[r][c] = "KX"

    result = "Fail"
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "KX":
                safe = False
                for dr, dc in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if "X" not in grid[nr][nc]:
                            safe = True
                            break
                result = "Fail" if safe else "Success"

    if display:
        for row in grid:
            print("  ".join(cell for cell in row))
        print(result)

    return result


def checkmate(chess):
    return analyze(chess)