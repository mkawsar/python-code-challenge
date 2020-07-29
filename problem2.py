class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def as_dict(self):
        d = {self.__str__() + key: value for key, value in self.__dict__.items()}
        return d

    def __str__(self):
        return ''.format(self.first_name, self.last_name)


def print_depth(my_dict, result, depth=1):
    # Search items in the dictionary
    for key, value in my_dict.items():
        print(key, depth)
        result[key] = depth
        if isinstance(value, Person):
            # Person class convert to dictionary
            d = value.as_dict()
            print_depth(d, result, depth + 1)
        # Check value is dictionary
        elif isinstance(value, dict):
            print_depth(value, result, depth + 1)


# Person class object

if __name__ == '__main__':
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
    result = {}
    print_depth(dataDict, result)
