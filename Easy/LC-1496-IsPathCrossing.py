class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur_pos = [0,0]
        visited = set()
        visited.add((0,0))
        
        for pos in range(len(path)):
            if path[pos] == 'N':
                cur_pos[1] += 1
            elif path[pos] == 'E':
                cur_pos[0] += 1
            elif path[pos] == 'S':
                cur_pos[1] -= 1
            else:
                cur_pos[0] -= 1

            if tuple(cur_pos) in visited:
                return True
            visited.add(tuple(cur_pos))

        return False
        