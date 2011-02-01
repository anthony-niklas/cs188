# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    
    You do not need to change anything in this class, ever.
    """
    
    def getStartState(self):
         """
         Returns the start state for the search problem 
         """
         util.raiseNotDefined()
        
    def isGoalState(self, state):
         """
             state: Search state
        
         Returns True if and only if the state is a valid goal state
         """
         util.raiseNotDefined()

    def getSuccessors(self, state):
         """
             state: Search state
         
         For a given state, this should return a list of triples, 
         (successor, action, stepCost), where 'successor' is a 
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental 
         cost of expanding to that successor
         """
         util.raiseNotDefined()

    def getCostOfActions(self, actions):
         """
            actions: A list of actions to take
 
         This method returns the total cost of a particular sequence of actions.    The sequence must
         be composed of legal moves
         """
         util.raiseNotDefined()
                     

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.    For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return    [s,s,w,s,w,w,s,w]

class Node:
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
          
def _search(problem, fringe):
    
    fringe.push(Node(None, (problem.getStartState(), None, 0)))
    explored = set()
    expanded = []
    
    while not fringe.isEmpty():
        node = fringe.pop()
        state, action, cost = node.data
        if problem.isGoalState(state):
            # Solved
            solution = []
            current = node
            while current is not None:
                state, action, cost = current.data
                # Don't append the root node to the solution
                current.parent and solution.append(action)
                current = current.parent

            solution.reverse()
            return solution
        else:
            for applicable in problem.getSuccessors(state):
                reachableState, _, _ = applicable
                if reachableState not in explored:
                    # If not in fringe:
                    # Only push onto fringe if applicable's state is not in fringe
                    fringe.push(Node(node, applicable))
                    explored.add(reachableState)
                    
    # No solution
    return []

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]
    
    Your search algorithm needs to return a list of actions that reaches
    the goal.    Make sure to implement a graph search algorithm 
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
    
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    return _search(problem, util.Stack())

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    return _search(problem, util.Queue())
            
def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueueWithFunction(lambda node: node.data[2])
    fringe.push(Node(None, (problem.getStartState(), None, 0)))
    explored = set()
    expanded = []
    
    while not fringe.isEmpty():
        node = fringe.pop()
        state, action, cost = node.data
        explored.add(state)
        
        for applicable in problem.getSuccessors(state):
            newState, newAction, newCost = applicable
            if newState not in explored:
                explored.add(newState)
                newNode = Node(node, applicable)
                if problem.isGoalState(newState):
                    # Solved
                    solution = []
                    current = newNode
                    while current is not None:
                        state, action, cost = current.data
                        # Don't append the root node to the solution
                        current.parent and solution.append(action)
                        current = current.parent
        
                    solution.reverse()
                    return solution
                    
                fringe.push(Node(node, applicable))
                    
    # No solution
    return []
    
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.    This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
        
    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
