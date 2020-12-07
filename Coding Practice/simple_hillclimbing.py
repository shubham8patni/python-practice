import numpy as np
from multiprocessing import Pool
import sys

np.set_printoptions(threshold=sys.maxsize)


class HillClimbMatrix(object):
    def __init__(self):
        np.random.seed(5)
        self.matrix = np.random.randint(1, 30, (20, 20))

    def get_vertex_neighbours(self, pos):
        n = []
        for dx, dy in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]:  # [(1, 1), (1, -1), (-1, 1), (-1, -1)]  can be added for diagonal search!
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            if x2 < 0 or x2 > 19 or y2 < 0 or y2 > 19:
                continue
            n.append((x2, y2))
        return n

    def find(self, current):
        z = 0

        for n in graph.get_vertex_neighbours(current):
            z = 0
            if graph.matrix[n] > graph.matrix[current]:
                z = z + 1
                print("next step  -> ", graph.matrix[n])
                print("next", n)
                print("current", current)
                current = n
                self.find(current)
                break


def HillClimbSearch(start, graph):
    start_point = graph.matrix[start]
    print("starting value is ", start_point)
    current = start

    current_val = start_point
    search = graph.find(current)
    return search


if __name__ == "__main__":

    graph = HillClimbMatrix()
    print(graph.matrix)

    s1, s2 = map(
        int, input("Enter row number 1 and column number 1 for start point = ").split()
    )

    result = HillClimbSearch((s1, s2), graph)
