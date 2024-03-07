"""
    Enter your details below:

    Name:
    Student ID:
    Email:
"""

from typing import List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem


def solve(problem: SearchProblem) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """

    raise_not_defined()  # Remove this line when you have implemented BrFS
    # *** YOUR CODE HERE ***
    state = SearchProblem.get_initial_state()
    own_pos = state.get_red_bird_position()
    state.yellow_birds
    min_dist = float("inf")
    min_yb = None
    for yb in state.yellow_birds:
        dist = state.layout.distance[(own_pos, yb)]
        if dist < min_dist:
            min_dist = dist
            min_yb = yb
    if min_yb is None:
        return Directions.STOP
