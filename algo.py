import pprint
import random


class PrimsRandomized:

    def __init__(self, row_len):
        self.row_len = row_len

        self.total_nodes = row_len**2

        self.TOP = 0
        self.LEFT = 1
        self.BOTTOM = 2
        self.RIGHT = 3

    def prims_mst(self):
        mst = [
            [0, 0, 0, 0] for _ in range(self.total_nodes)
        ]

        to_visit = [node for node in range(self.total_nodes)]

        node = to_visit[0]
        visited = [node]
        to_visit.remove(node)

        while len(to_visit) > 0:

            edges_pool = self.edges_to_unvisited_nodes(visited)
            # pick a random edge
            edge = random.choice(edges_pool)
            node, next_node = edge

            direction = self.get_neighbour_dir(node, next_node)
            mst[node][direction] = 1

            neighbour_dir = self.get_neighbour_dir(next_node, node)
            mst[next_node][neighbour_dir] = 1

            visited.append(next_node)
            to_visit.remove(next_node)

        return mst

    def edges_to_unvisited_nodes(self, visited):

        edges_pool = []

        for node in visited:

            row = node // self.row_len
            col = node % self.row_len

            if row > 0:
                top_node = node - self.row_len
                if top_node not in visited:
                    edges_pool.append((node, top_node))

            if col > 0:
                left_node = node - 1
                if left_node not in visited:
                    edges_pool.append((node, left_node))

            if row < self.row_len - 1:
                bottom_node = node + self.row_len
                if bottom_node not in visited:
                    edges_pool.append((node, bottom_node))

            if col < self.row_len - 1:
                right_node = node + 1
                if right_node not in visited:
                    edges_pool.append((node, right_node))

        return edges_pool

    def get_neighbour_dir(self, node, next_node):
        if node - self.row_len == next_node:
            return self.TOP
        if node - 1 == next_node:
            return self.LEFT
        if node + self.row_len == next_node:
            return self.BOTTOM
        if node + 1 == next_node:
            return self.RIGHT


if __name__ == '__main__':
    n = 4
    pr = PrimsRandomized(n)

    