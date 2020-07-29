import unittest
from problem2 import print_depth, Person


class TestProblem2(unittest.TestCase):
    def test_problem2(self):
        person_a = Person('User', '1', None)
        person_b = Person('User', '2', person_a)
        dataDict = {
            'key1': 1,
            'key2': {
                'key3': 1,
                'key4': {
                    'key5': 4,
                    'user': person_b
                }
            }
        }
        objects = {}
        output = {
            'key1': 1, 'key2': 1,
            'key3': 2, 'key4': 2,
            'key5': 3, 'user': 3,
            'first_name': 4,
            'last_name': 4,
            'father': 4,
            'first_name': 5,
            'last_name': 5,
            'father': 5
        }
        print_depth(dataDict, objects)
        self.assertDictEqual(objects, output)


if __name__ == '__main__':
    unittest.main()
