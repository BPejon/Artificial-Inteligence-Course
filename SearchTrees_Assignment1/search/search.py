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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    """How it works
    First, we create a Stack.
    Then we put a Node which saves the coordenate and path of Pacman
    Moreover, we put on the Stack all of the 
    """

    #2 types of Implementation
    #2 Stacks - 1 for Next Moves and another for paths
    #1 Stacks - Nodes have Next Moves and path inside them  -> Using this one
        
    Stack = util.Stack()
    Stack.push((problem.getStartState(), []))

    VisitedNodes = []
    Path = []

    

    while Stack.isEmpty() != True:
        CurrentNode, Path = Stack.pop()
        if problem.isGoalState(CurrentNode) == True:
            return Path
        
        if CurrentNode not in VisitedNodes:
            VisitedNodes.append(CurrentNode)
            for NextNode, Action, Cost in problem.getSuccessors(CurrentNode):
                NewPath = Path + [Action]
                Stack.push((NextNode, NewPath))
    else:
        print "Path is Blocked!"
        return -1

    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Same thing as the DFS above, although it's implemented with a Queue
    """So instead of exploring in deep, it explores in breadth"""

    Queue = util.Queue()
    Queue.push((problem.getStartState(), []))

    VisitedNodes = []
    Path = []

    while Queue.isEmpty() != True:
        CurrentNode, Path = Queue.pop()
        if problem.isGoalState(CurrentNode) == True:
            return Path

        if CurrentNode not in VisitedNodes:
            VisitedNodes.append(CurrentNode)
            for NextNode, Action, Cost in problem.getSuccessors(CurrentNode):
                NewPath = Path + [Action]
                Queue.push((NextNode, NewPath))
    else:
        print "Path if Blocked!"
        return -1

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #Easy, the same thing as DFS and BFS although with costs
    """
    To create a UniformCostSeach, we will need a Priority Queue
    The Queue will store One Node with the Coordinates, the Path and the Total Path Cost,
    and the priority will be the cost of the actual node 
    """
    PrioQueue = util.PriorityQueue()
    PrioQueue.push((problem.getStartState(), [], 0), 0)

    VisitedNodes = []
    Path = []

    while PrioQueue.isEmpty() != True:
        CurrentNode, Path, PathCost = PrioQueue.pop()
        if problem.isGoalState(CurrentNode) == True:
            return Path
        
        if CurrentNode not in VisitedNodes:
            VisitedNodes.append(CurrentNode)
            for NextNode, Action, ActionCost in problem.getSuccessors(CurrentNode):
                NewPath = Path + [Action]
                #print "NewPath = ", NewPath
                NewPathCost = PathCost + ActionCost
                PrioQueue.push((NextNode, NewPath, NewPathCost), NewPathCost)


    else:
        print "Path is Blocked!"
        return -1


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    #The same structure as UCS but the priority now is the heuristics
    PrioQueue = util.PriorityQueue()
    PrioQueue.push((problem.getStartState(), [], 0), 0)

    VisitedNodes = []
    Path = []

    while PrioQueue.isEmpty() != True:
        CurrentNode, Path, PathCost = PrioQueue.pop()
        if problem.isGoalState(CurrentNode) == True:
            return Path

        if CurrentNode not in VisitedNodes:
            VisitedNodes.append(CurrentNode)
            for NextNode, Action, ActionCost in problem.getSuccessors(CurrentNode):
                NewPath = Path + [Action]
                NewPathCost = PathCost + ActionCost
                HeuristicCost = NewPathCost + heuristic(NextNode, problem)
                PrioQueue.push((NextNode, NewPath, NewPathCost), HeuristicCost)


    else:
        print "Path is Blocked!"
        return -1



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

'''
                if PrioQueue.heap:
                    print(PrioQueue.heap)
                else:
                    print('empty')
'''