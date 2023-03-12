import unittest
import classToQuan as cq


class TestClassToQuan(unittest.TestCase):

    def test_bool(self):
        # Test 1
        result = cq.canicas([[True, False, False], [False, True, True], [False, False, False]], [[0], [0], [0]],
                                   17)
        self.assertEqual(result, [[0], [0], [0]])
        # Test 2
        result = cq.canicas([[True, False, False], [False, True, True], [False, False, False]], [[0], [1], [0]],
                                   17)
        self.assertEqual(result, [[0], [1], [0]])


    def test_prob(self):
        matrix = [[0, 1 / 6, 5 / 6], [1 / 3, 1 / 2, 1 / 6], [2 / 3, 1 / 3, 0]]
        # Test 1
        result = cq.sistemaProbabilistico(matrix, [[1 / 5], [7 / 10], [1 / 10]], 1)
        self.assertEqual(result, [[0.2], [0.434], [0.366]])
        # Test 2
        result = cq.sistemaProbabilistico(matrix, [[1 / 5], [7 / 10], [1 / 10]], 3)
        self.assertEqual(result, [[0.289], [0.344], [0.366]])

    def test_cuan(self):
        matrix = [[[1 / (2 ** 0.5), 0], [0, 1 / (2 ** 0.5)]], [[1 / (2 ** 0.5), 0], [0, -1 / (2 ** 0.5)]]]
        # Test 1
        result = cq.sistemaProbabilisticoCuantico(matrix, [[[0, 0]], [[0, 0]]], 5)
        self.assertEqual(result, [[0.0], [0.0]])
        # Test 2
        result = cq.sistemaProbabilisticoCuantico(matrix, [[[1, 0]], [[0, 0]]], 1)
        self.assertEqual(result, [[0.5], [0.5]])

    
if __name__ == '__main__':
    unittest.main()
