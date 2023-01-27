import random

# from https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python/

def remove_items(test_list, item):

    # remove the item for all its occurences
    c = test_list.count(item)
    for i in range(c):
        test_list.remove(item)

    return test_list


# from https://www.youtube.com/watch?v=iIu4ixFlT-w -- "Probability Calculator - Python | FreeCodeCamp" by Landon Schlangen


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        print(kwargs)
        for key, value, in kwargs.items():
            for i in range(value):
                self.contents.append(key)
        print(self.contents)

    def draw(self, number):
        all_removed = []
        if(number > len(self.contents)):
            return self.contents
        for i in range(number):
            removed = self.contents.pop(int(random.random() * len(self.contents)))
            all_removed.append(removed)
            remove_items(self.contents, removed)

        print(all_removed)
        return all_removed

