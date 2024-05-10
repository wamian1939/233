# COMP9021 24T1
# Assignment 2 *** Due Monday Week 11 @ 10.00am

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# IMPORT ANY REQUIRED MODULE


class MazeError(Exception):
    def __init__(self, message):
        self.message = message



class Maze:
    def __init__(self, filename):
        self.file = filename
        self.grid = []
        with open(filename) as file:
            i = 0
            for line in file:
                if line.strip() == '':
                    continue
                else:
                    self.grid.append([])
                    for e in line:
                        if e.isdigit():
                            self.grid[i].append(int(e))
                    i += 1
        self.check()
        # gates
        self.gates = {
            'top': [],
            'bottom': [],
            'left': [],
            'right': []
        }
        self.num_of_gates = self.find_gate()
        self.inaccessible_point_four = set()
        # wall
        self.wall = []
        self.num_of_walls = self.find_walls()
        # point
        self.inaccessible_points = set()
        self.grid_four = self.big_grid()
        self.height = len(self.grid_four)
        self.width = len(self.grid_four[0])
        self.pillar = self.count_pillar()
        self.areas = self.find_accessible_areas()
        self.inaccessible_point = set()
        self.cul_de_sacs = self.find_cul_de_sacs()
        self.num_entry_exit_path = self.find_entry_exit_paths()

    def check(self):
        if len(self.grid) < 2 or len(self.grid) > 41:
            raise MazeError('Incorrect input.')
        
        row_lengths = set(len(row) for row in self.grid)
        if len(row_lengths) > 1 or any(length < 2 or length > 31 for length in row_lengths):
            raise MazeError('Incorrect input.')

        for row in self.grid:
            if any(e not in [0, 1, 2, 3] for e in row):
                raise MazeError('Incorrect input.')

        if any(self.grid[i][-1] not in [0, 2] for i in range(len(self.grid) - 1)):
            raise MazeError('Input does not represent a maze.')

        if any(self.grid[-1][j] not in [0, 1] for j in range(len(self.grid[0]))):
            raise MazeError('Input does not represent a maze.')

        if self.grid[-1][-1] != 0:
            raise MazeError('Input does not represent a maze.')

    def find_gate(self):
        num_of_gate = 0
        # top and bottom
        for x in range(len(self.grid[0]) - 1):
            if self.grid[0][x] in [0, 2]:
                self.gates['top'].append((0, x))
                num_of_gate += 1
            if self.grid[len(self.grid) - 1][x] in [0, 2]:
                self.gates['bottom'].append((len(self.grid) - 1, x))
                num_of_gate += 1
        for y in range(len(self.grid) - 1):
            if self.grid[y][0] in [1, 0]:
                self.gates['left'].append((y, 0))
                num_of_gate += 1
            if self.grid[y][len(self.grid[0]) - 1] in [0]:
                self.gates['right'].append((y, len(self.grid[0]) - 1))
                num_of_gate += 1
        return num_of_gate

    def find_walls(self):
        visited = [[False] * len(self.grid[0]) for _ in range(len(self.grid))]

        def dfs(x, y):
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            stack = [(x, y)]
            while stack:
                i, j = stack.pop()
                if not visited[i][j]:
                    visited[i][j] = True
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(self.grid) and 0 <= nj < len(self.grid[0]):
                            if not visited[ni][nj] and is_connected(i, j, ni, nj):
                                stack.append((ni, nj))

        def is_connected(i1, j1, i2, j2):
            if i1 == i2:
                if j1 < j2:
                    return self.grid[i1][j1] in [1, 3]
                else:
                    return self.grid[i2][j2] in [1, 3]
            if j1 == j2:
                if i1 < i2:
                    return self.grid[i1][j1] in [2, 3]
                else:
                    return self.grid[i2][j2] in [2, 3]
            return False

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] != 0 and not visited[i][j]:
                    self.wall.append([])
                    dfs(i, j)
        num_of_walls = len(self.wall)
        return num_of_walls

    def big_grid(self):
        grid_four = []
        for row in self.grid:
            new_row_top = []
            new_row_bottom = []
            for num in row:
                if num == 0:
                    new_row_top.extend([1, 0])
                    new_row_bottom.extend([0, 0])
                elif num == 1:
                    new_row_top.extend([1, 1])
                    new_row_bottom.extend([0, 0])
                elif num == 2:
                    new_row_top.extend([1, 0])
                    new_row_bottom.extend([1, 0])
                elif num == 3:
                    new_row_top.extend([1, 1])
                    new_row_bottom.extend([1, 0])
            grid_four.append(new_row_top)
            grid_four.append(new_row_bottom)
        grid_four = grid_four[:-1]
        grid_four = [row[:-1] for row in grid_four]
        return grid_four

    def count_pillar(self):
        pillar = []
        direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        for row in range(len(self.grid_four)):
            for col in range(len(self.grid_four[0])):
                count = 0
                for dx, dy in direction:
                    nx, ny = row + dx, col + dy
                    if 0 <= nx < len(self.grid_four) and 0 <= ny < len(self.grid_four[0]):
                        if self.grid_four[nx][ny] == 1:
                            count += 1
                if count == 0 and self.grid_four[row][col] == 1:
                    pillar.append((row, col))
        return pillar

    def find_four_gates(self):
        four_gate = []
        for row in range(len(self.grid_four)):
            for col in range(len(self.grid_four[0])):
                if row in (0, len(self.grid_four) - 1) or col in (0, len(self.grid_four[0]) - 1):
                    if self.grid_four[row][col] == 0:
                        four_gate.append((row, col))
        return four_gate

    def find_four_walls(self):
        def dfs(x, y, path, component_id):
            direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            self.grid_four[x][y] = component_id
            path.append((row, col))
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.grid_four) and 0 <= ny < len(self.grid_four[0]):
                    if self.grid_four[nx][ny] == 1:
                        dfs(nx, ny, path, component_id)

        component_id = 2
        four_walls = []
        for row in range(len(self.grid_four)):
            for col in range(len(self.grid_four[0])):
                if self.grid_four[row][col] == 1 and (row, col) not in self.pillar:
                    path = []
                    dfs(row, col, path, component_id)
                    four_walls.append(path)
                    component_id += 1
        for row in range(len(self.grid_four)):
            for col in range(len(self.grid_four[0])):
                if self.grid_four[row][col] != 0:
                    self.grid_four[row][col] = 1
        return four_walls

    def find_accessible_areas(self):
        gates = self.find_four_gates()

        def dfs(x, y, path, component_id):
            direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            self.grid_four[x][y] = component_id
            path.append((row, col))
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.grid_four) and 0 <= ny < len(self.grid_four[0]):
                    if self.grid_four[nx][ny] == 0:
                        dfs(nx, ny, path, component_id)

        component_id = 2
        areas = []
        for row, col in gates:
            if self.grid_four[row][col] == 0:
                path = []
                dfs(row, col, path, component_id)
                areas.append(path)
                component_id += 1
        for row in range(len(self.grid_four)):
            for col in range(len(self.grid_four[0])):
                if self.grid_four[row][col] == 0:
                    self.inaccessible_points.add((row // 2, col // 2))
                    if row % 2 == 1 and col % 2 == 1:
                        self.inaccessible_point_four.add((row, col))
        for row in range(len(self.grid_four)):
            for col in range(len(self.grid_four[0])):
                if self.grid_four[row][col] != 1:
                    self.grid_four[row][col] = 0
        return areas

    def find_cul_de_sacs(self):
        def get_around(x, y):
            get_point = {0: [], 1: []}
            direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.grid_four) and 0 <= ny < len(self.grid_four[0]):
                    v = self.grid_four[nx][ny]
                    get_point[v].append((nx, ny))
            return get_point

        cul_de_sacs = []
        for row in range(len(self.grid_four)):
            for col in range(len(self.grid_four[0])):
                if self.grid_four[row][col] == 0 and (row, col) not in self.inaccessible_point_four:
                    point_list = get_around(row, col)
                    if len(point_list[1]) == 3 and len(point_list[0]) == 1:
                        cul_de_sacs.append((row, col))

        return cul_de_sacs

    def find_entry_exit_paths(self):
        gates = self.find_four_gates()
        valid_paths = []
        gate_connections = {}

        for start_gate in gates:
            unique_exit = None
            for end_gate in gates:
                if start_gate != end_gate:
                    path = self.bfs_find_path(start_gate, end_gate)
                    if path:
                        if start_gate not in gate_connections:
                            gate_connections[start_gate] = end_gate
                            unique_exit = end_gate
                            valid_paths.append(path)
                        elif gate_connections[start_gate] == end_gate:
                            valid_paths.append(path)
                        else:
                            valid_paths = [p for p in valid_paths if p[0] != start_gate]
        unique_data = []
        added_sets = []
        for i in valid_paths:
            current_set = set(i)
            if not any(set(other) == current_set and i == other[::-1] for other in unique_data):
                if current_set not in added_sets:
                    unique_data.append(i)
                    added_sets.append(current_set)

        return unique_data

    def bfs_find_path(self, start, end):
        queue = [(start, [start])]
        visited = set()
        while queue:
            current, path = queue.pop(0)
            if current == end:
                return path
            current_row, current_col = current
            for neighbor in self.get_neighbors(current_row, current_col):
                if neighbor not in visited and neighbor not in self.cul_de_sacs:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def get_neighbors(self, row, col):
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右，下，左，上
        for dx, dy in directions:
            nx, ny = row + dx, col + dy
            if 0 <= nx < len(self.grid_four) and 0 <= ny < len(self.grid_four[0]) and self.grid_four[nx][ny] == 0:
                neighbors.append((nx, ny))
        return neighbors

    def analyse(self):
        if self.num_of_gates == 0:
            print('The maze has no gate.')
        elif self.num_of_gates == 1:
            print('The maze has a single gate.')
        else:
            print('The maze has', self.num_of_gates, 'gates.')

        if self.num_of_walls == 0:
            print('The maze has no wall.')
        elif self.num_of_walls == 1:
            print('The maze has walls that are all connected.')
        else:
            print('The maze has', self.num_of_walls, 'sets of walls that are all connected.')

        if len(self.inaccessible_points) == 0:
            print('The maze has no inaccessible inner point.')
        elif len(self.inaccessible_points) == 1:
            print('The maze has a unique inaccessible inner point.')
        else:
            print('The maze has', len(self.inaccessible_points), 'inaccessible inner points.')

        if len(self.areas) == 0:
            print('The maze has no accessible area.')
        elif len(self.areas) == 1:
            print('The maze has a unique accessible area.')
        else:
            print('The maze has', len(self.areas), 'accessible areas.')

        if len(self.cul_de_sacs) == 0:
            print('The maze has no accessible cul-de-sac.')
        elif len(self.cul_de_sacs) == 1:
            print('The maze has accessible cul-de-sacs that are all connected.')
        else:
            print('The maze has', len(self.cul_de_sacs), 'sets of accessible cul-de-sacs that are all connected.')

        if len(self.num_entry_exit_path) == 0:
            print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
        elif len(self.num_entry_exit_path) == 1:
            print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        else:
            print('The maze has', len(self.num_entry_exit_path),
                  'entry-exit paths with no intersections not to cul-de-sacs.')

    def display(self):
        lines = []
        lines.append('\\documentclass[10pt]{article}')
        lines.append('\\usepackage{tikz}')
        lines.append('\\usetikzlibrary{shapes.misc}')
        lines.append('\\usepackage[margin=0cm]{geometry}')
        lines.append('\\pagestyle{empty}')
        lines.append('\\tikzstyle{every node}=[cross out, draw, red]\n')

        lines.append('\\begin{document}\n')
        lines.append('\\vspace*{\\fill}')
        lines.append('\\begin{center}')
        lines.append('\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]')
        lines.append('% Walls')
        for y in range(0, len(self.grid_four), 2):
            x = 1
            while x < len(self.grid_four[0]):
                if self.grid_four[y][x] == 1:
                    x1, x2 = x, x
                    while x2 + 2 < len(self.grid_four[0]) and self.grid_four[y][x2 + 2] == 1:
                        x2 += 2
                    lines.append(f"    \\draw ({x1 // 2},{y // 2}) -- ({x2 // 2 + 1},{y // 2});")  # 添加线段
                    x = x2 + 2
                else:
                    x += 2
        for x in range(0, len(self.grid_four[0]), 2):
            y = 1
            while y < len(self.grid_four):
                if self.grid_four[y][x] == 1:
                    y1, y2 = y, y
                    while y2 + 2 < len(self.grid_four) and self.grid_four[y2 + 2][x] == 1:
                        y2 += 2
                    lines.append(f"    \\draw ({x // 2},{y1 // 2}) -- ({x // 2},{y2 // 2 + 1});")  # 添加线段
                    y = y2 + 2
                else:
                    y += 2
        lines.append("% Pillars")
        for y, x in self.pillar:
            lines.append(f"    \\fill[green] ({x // 2},{y // 2}) circle(0.2);")

        lines.append("% Inner points in accessible cul-de-sacs")
        inner_points = []
        for y, x in self.cul_de_sacs:
            if y % 2 == 1 and x % 2 == 1:
                inner_points.append((x // 2, y // 2))
        for x, y in sorted(inner_points, key=lambda items: (items[1], items[0])):
            lines.append(f"    \\node at ({x + 0.5},{y + 0.5}) {{}};")
        lines.append("% Entry-exit paths without intersections")
        points = set()
        for path in self.num_entry_exit_path:
            points.update(path)

        for y in range(1, len(self.grid_four), 2):
            x = 0
            while x < len(self.grid_four[0]):
                if (y, x) in points and (y, x + 1) in points:
                    x1 = x
                    while x + 1 < len(self.grid_four[0]) and (y, x + 1) in points:
                        x += 1
                    x_offset = -0.5 if x1 == 0 else 0.5  
                    lines.append(
                        f'    \\draw[dashed, yellow] ({x1 // 2 + x_offset},{y // 2 + 0.5}) -- ({x // 2 + 0.5},{y // 2 + 0.5});')
                x += 1

        for x in range(1, len(self.grid_four[0]), 2):
            y = 0
            while y < len(self.grid_four):
                if (y, x) in points and (y + 1, x) in points:
                    y1 = y
                    while y + 1 < len(self.grid_four) and (y + 1, x) in points:
                        y += 1
                    y_offset = -0.5 if y1 == 0 else 0.5 
                    lines.append(
                        f'    \\draw[dashed, yellow] ({x // 2 + 0.5},{y1 // 2 + y_offset}) -- ({x // 2 + 0.5},{y // 2 + 0.5});')
                y += 1
        lines.append('\\end{tikzpicture}')
        lines.append('\\end{center}')
        lines.append('\\vspace*{\\fill}\n')
        lines.append('\\end{document}\n')
        with open(self.file[0:-3] + 'tex', 'w') as latex_file:
            latex_file.writelines('\n'.join(lines))

