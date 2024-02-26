# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import queue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

class Node_():
    def __init__ (self, state, parentNode, action, cost):
        self.state = state
        self.parentNode = parentNode
        self.action = action
        self.cost = cost

    def __eq__(self, other):
        return self.state == other.state

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    visited = []
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    while not stack.isEmpty():
        state, actions = stack.pop()
        if problem.isGoalState(state):
            return actions
        visited.append(state)
        for next_state, action, cost in problem.getSuccessors(state):
            if next_state not in visited:
                new_nodes = actions + [action]
                stack.push((next_state, new_nodes))
    return []


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = []
    my_queue = util.Queue()
    my_queue.push((problem.getStartState(), []))
    while not my_queue.isEmpty():
        state, actions = my_queue.pop()
        if problem.isGoalState(state):
            return actions
        visited.append(state)
        for next_state, action, _ in problem.getSuccessors(state):
            if next_state not in visited and next_state not in [item[0] for item in my_queue.list]:
                new_nodes = actions + [action]
                my_queue.push((next_state, new_nodes))
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = []
    my_pqueue = util.PriorityQueue()
    my_pqueue.push((problem.getStartState(), []), 0)
    while not my_pqueue.isEmpty():
        state, actions = my_pqueue.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.append(state)
            for next_state, action, cost in problem.getSuccessors(state):
                if next_state not in visited:
                    new_nodes = actions + [action]
                    my_pqueue.push((next_state, new_nodes), problem.getCostOfActions(new_nodes))
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = []
    my_pqueue = util.PriorityQueue()
    my_pqueue.push((problem.getStartState(), []), 0)
    while not my_pqueue.isEmpty():
        state, actions = my_pqueue.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.append(state)
            for next_state, action, cost in problem.getSuccessors(state):
                if next_state not in visited:
                    new_nodes = actions + [action]
                    my_pqueue.push((next_state, new_nodes), problem.getCostOfActions(new_nodes) + heuristic(next_state, problem))
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
