def print_depth(my_dict, result, depth=1):
    # Search items in the dictionary
    for key, value in my_dict.items():
        print(key, depth)
        result[key] = depth
        # Check given object is dictionary or not
        if isinstance(value, dict):
            # Depth increments
            print_depth(value, result, depth + 1)
    


if __name__ == "__main__":
    dataDict = {
        'key1': 1,
        'key2': {
            'key3': 1,
            'key4': {
                'key5': 5
            }
        }
    }
    result = {}
    print_depth(dataDict, result)
