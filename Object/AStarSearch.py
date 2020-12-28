from typing import List, Tuple, Dict
import numpy as np


class AStarAlgorithm (object):

    weight_line = 0.5
    weight_diagonal = 0.75
    movement = [-1,0,1]

    def __init__(self, graph: List[List[int]]):
        # remember the graph goes on the top because of python indexing and our tuple indexing
        self.graph = graph

    @staticmethod
    def manhattan_distance(position1: Tuple[int, int], position2: Tuple[int, int]) -> int:
        """
        Generic function used to calculate the distance between two points in l1
             o-o-p2
             o         manhattan_distance = 6 (number of separating lines and dash)
        p1-o-o
        :param position1: first position (tuple[int, int])
        :param position2: second position (tuple[int, int])
        :return: int
        """
        return abs(position1[0]-position2[0])+abs(position1[1]-position2[1])

    def h(self, current_position: Tuple[int, int], end: Tuple[int, int], zone_multiplier: int = 1) -> float:
        """
        Method used to calculate the predicted score to reach the end, could use any
        distance measurement technique, we are currently using manhattan distance
        :param current_position: current position we want to evaluate the score for
        :param end: end position we want to reach
        :param zone_multiplier: weight multiplier based on the current zone
        :return:
        """
        return self.manhattan_distance(current_position, end)*AStarAlgorithm.weight_line*zone_multiplier

    def in_boundaries(self, position: Tuple[int, int]) -> bool:
        return (position[0] >= 0 and position[1] >= 0 and \
                position[0] < len(self.graph) and position[1] < len(self.graph[1]))

    def try_movement(self, current_position: Tuple[int, int], next_position: Tuple[int, int]) -> (bool, float):
        weight = 0

        #  We check if it's inside our graph
        if not self.in_boundaries(next_position):
            return False, weight

        #  We check if it's different than the previous position
        if current_position == next_position:
            return False, weight

        #  We check if we can go to this position
        if not self.graph[next_position[0]][next_position[1]]:
            return False, weight

        #  We get the weight
        #  horizontal or vertical movement
        if self.manhattan_distance(current_position, next_position) == 1:
            weight = AStarAlgorithm.weight_line
        #  diagonal movement
        elif self.manhattan_distance(current_position, next_position) == 2:
            weight = AStarAlgorithm.weight_diagonal
        #  impossible movement
        else:
            return False, weight

        #  we add the zone multiplier influence
        weight = weight * self.graph[next_position[0]][next_position[1]]

        return True, weight

    def best_position_to_search(self, open_set: List[Tuple[int,int]], fscore: Dict[Tuple[int, int], int]) -> Tuple[int, int]:
        #  We initialize with the first position
        best_position = open_set[0]
        best_score = np.inf
        if best_position in fscore:
            best_score = fscore[best_position]

        #  We loop on the positions available
        for position in open_set[1:]:

            #  We get the score of this position
            score = np.inf
            if position in fscore:
                score = fscore[position]

            #  If the score is better we memorise this position
            if score < best_score:
                best_score = score
                best_position = position

        return best_position

    def reconstruct_path(self, came_from: Dict[Tuple[int, int], Tuple[int, int]], position: Tuple[int, int]):
        path = [position]
        while position in came_from:
            position = came_from[position]
            path.append(position)
        return path

    def find_path(self, start_point: Tuple[int, int], end_point: Tuple[int, int]):
        if len(start_point) != 2 or len(end_point) !=2:
            return False, [], 'problem with the length of coordinates given'

        if type(start_point[0]) != int or type(start_point[1]) != int or \
           type(end_point[0]) != int or type(end_point[1]) != int:
            return False, [], 'problem with the type in coordinates given'

        # list of positions we should visit (use of a priority queue would be better)
        open_set = [start_point]
        # map used to find the path we took at the end
        came_from = {}

        # map of scores to reach the positions from the starting point
        gscore = {}
        gscore[start_point] = 0

        # map of total scores. f(point) = g(point) + h(point).
        # where h represents the function to estimate the cost to reach the end.
        fscore = {}
        fscore[start_point] = self.h(start_point, end_point)

        while open_set:
            #  We get the best position to continue searching from
            current_position = self.best_position_to_search(open_set, fscore)

            #  If the current position is the end position, we succeeded and we return the reconstructed path
            if current_position == end_point:
                return True, self.reconstruct_path(came_from, current_position), ''

            #  We remove it from the positions we still need to visit
            open_set.remove(current_position)

            #  We try a vertical movement
            for i in AStarAlgorithm.movement:
                #  We try an horizontal movement
                for j in AStarAlgorithm.movement:
                    neighbor = (current_position[0]+i, current_position[1]+j)

                    #  We calculate the cost it would take to move to the neighbour
                    success, movement_weight = self.try_movement(current_position, neighbor)

                    #  If we can't move there we ignore it
                    if not success:
                        continue

                    #  we evaluate the score
                    score = np.inf
                    if current_position in gscore:
                        score = gscore[current_position] + movement_weight

                    #  if the neighbour is not inside gscore or we have a better score now we need
                    #  to update everything
                    if neighbor not in gscore or score < gscore[neighbor]:
                        came_from[neighbor] = current_position
                        gscore[neighbor] = score
                        fscore[neighbor] = score + self.h(neighbor, end_point)
                        if neighbor not in open_set:
                            open_set.append(neighbor)

        return False, [], 'No solutions found to the problem'

if __name__ == '__main__':
    a_star_floor1 = AStarAlgorithm([[1,0,1],[1,1,1]])
    print(a_star_floor1.in_boundaries((0,0)))