import unittest
import sys
import os

sys.path.append(os.getcwd())
import MDP

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class MDPPythonValueIterationTests(unittest.TestCase):

    def testEscapeToCorners(self):
        # This model is done manually, I'll copy the makeCornerProblem
        # C++ stuff that auto generates these tables soon enough.
        model = MDP.Model(16,4)

        t=[[[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0.2,0.8,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0.2,0,0,0,0.8,0,0,0,0,0,0,0,0,0,0],[0.8,0.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0.2,0.8,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0.2,0,0,0,0.8,0,0,0,0,0,0,0,0,0],[0,0.8,0.2,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0.2,0,0,0,0.8,0,0,0,0,0,0,0,0],[0,0,0.8,0.2,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0.8,0,0,0,0.2,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0.2,0.8,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0.2,0,0,0,0.8,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0.8,0,0,0,0.2,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0.2,0.8,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0.2,0,0,0,0.8,0,0,0,0,0,0],[0,0,0,0,0.8,0.2,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,0.8,0,0,0,0.2,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0.2,0.8,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0.2,0,0,0,0.8,0,0,0,0,0],[0,0,0,0,0,0.8,0.2,0,0,0,0,0,0,0,0,0]],
        [[0,0,0,0.8,0,0,0,0.2,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0.2,0,0,0,0.8,0,0,0,0],[0,0,0,0,0,0,0.8,0.2,0,0,0,0,0,0,0,0]],
        [[0,0,0,0,0.8,0,0,0,0.2,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0.2,0.8,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0.2,0,0,0,0.8,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]],
        [[0,0,0,0,0,0.8,0,0,0,0.2,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0.2,0.8,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0.2,0,0,0,0.8,0,0],[0,0,0,0,0,0,0,0,0.8,0.2,0,0,0,0,0,0]],
        [[0,0,0,0,0,0,0.8,0,0,0,0.2,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0.2,0.8,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0.2,0,0,0,0.8,0],[0,0,0,0,0,0,0,0,0,0.8,0.2,0,0,0,0,0]],
        [[0,0,0,0,0,0,0,0.8,0,0,0,0.2,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0.2,0,0,0,0.8],[0,0,0,0,0,0,0,0,0,0,0.8,0.2,0,0,0,0]],
        [[0,0,0,0,0,0,0,0,0.8,0,0,0,0.2,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0.2,0.8,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]],
        [[0,0,0,0,0,0,0,0,0,0.8,0,0,0,0.2,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0.2,0.8,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0.8,0.2,0,0]],
        [[0,0,0,0,0,0,0,0,0,0,0.8,0,0,0,0.2,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.2,0.8],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0.8,0.2,0]],
        [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]]


        r=[[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0],[-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0],[0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0],[0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0],[0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0],[0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0]],
        [[0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0]],
        [[0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0],[0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0]],
        [[0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0]],
        [[0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],[0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0]],
        [[0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0]],
        [[0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0]],
        [[0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0]],
        [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]]

        model.setTransitionFunction(t)
        model.setRewardFunction(r)

        vi = MDP.ValueIteration(1000000, 0.001)
        solution = vi(model)

        self.assertEqual(solution[0] < vi.getEpsilon(), True)

        qfun = solution[2]

        p = MDP.QGreedyPolicy(qfun)

        for a in xrange(0, 4):
            self.assertEqual(p.getActionProbability(0, a), 0.25)
            self.assertEqual(p.getActionProbability(6, a), 0.25)
            self.assertEqual(p.getActionProbability(9, a), 0.25)
            self.assertEqual(p.getActionProbability(15, a), 0.25)

        self.assertEqual(p.getActionProbability(1, LEFT), 1.0)
        self.assertEqual(p.getActionProbability(2, LEFT), 1.0)

        self.assertEqual(p.getActionProbability(3, LEFT), 0.5)
        self.assertEqual(p.getActionProbability(3, DOWN), 0.5)

        self.assertEqual(p.getActionProbability(4, UP), 1.0)
        self.assertEqual(p.getActionProbability(8, UP), 1.0)

        self.assertEqual(p.getActionProbability(5, LEFT), 0.5)
        self.assertEqual(p.getActionProbability(5, UP), 0.5)

        self.assertEqual(p.getActionProbability(7,  DOWN), 1.0)
        self.assertEqual(p.getActionProbability(11, DOWN), 1.0)

        self.assertEqual(p.getActionProbability(10, RIGHT), 0.5)
        self.assertEqual(p.getActionProbability(10, DOWN), 0.5)

        self.assertEqual(p.getActionProbability(12, RIGHT), 0.5)
        self.assertEqual(p.getActionProbability(12, UP), 0.5)

        self.assertEqual(p.getActionProbability(13, RIGHT), 1.0)
        self.assertEqual(p.getActionProbability(14, RIGHT), 1.0)

        vfun = solution[1]
        values = vfun[0]
        actions = vfun[1]

        for s in xrange(0, 16):
            self.assertEqual( qfun[s, actions[s]], values[s] )

if __name__ == '__main__':
    unittest.main(verbosity=2)
