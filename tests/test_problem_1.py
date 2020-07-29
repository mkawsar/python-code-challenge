import unittest
from problem1 import print_depth


class TestProblem1(unittest.TestCase):
    def test_problem1(self):
        dataDict = {
            'key1': 1,
            'key2': {
                'key3': 1,
                'key4': {
                    'key5': 5
                }
            }
        }
        objects = {}
        output = {'key1': 1, 'key2': 1, 'key3': 2, 'key4': 2, 'key5': 3}
        print_depth(dataDict, objects)
        self.assertDictEqual(objects, output)


if __name__ == '__main__':
    unittest.main()
