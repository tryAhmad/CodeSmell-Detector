import hashlib
import ast
from radon.complexity import cc_visit

# Example of a function with a long parameter list (more than 7 parameters)
def process_data(param1, param2, param3, param4, param5, param6, param7, param8, param9):
    print(param1, param2, param3, param4, param5, param6, param7, param8, param9)

# Duplicated code block 1
def find_duplicates(data):
    hashes = set()
    duplicates = []
    for item in data:
        hash_val = hashlib.md5(item.encode('utf-8')).hexdigest()
        if hash_val in hashes:
            duplicates.append(item)
        else:
            hashes.add(hash_val)
    return duplicates

# Duplicated code block 2 (duplicate of the above function)
def find_duplicate_items(data):
    hash_set = set()
    duplicate_items = []
    for element in data:
        hash_val = hashlib.md5(element.encode('utf-8')).hexdigest()
        if hash_val in hash_set:
            duplicate_items.append(element)
        else:
            hash_set.add(hash_val)
    return duplicate_items

# Example of a God Class with too many methods (high cyclomatic complexity)
class GodClass:
    def __init__(self):
        self.attribute1 = 0
        self.attribute2 = "Hello"
        self.attribute3 = []

    def method1(self):
        print("Method 1 executed")
        self.attribute1 += 1

    def method2(self):
        print("Method 2 executed")
        self.attribute2 += " World"

    def method3(self):
        print("Method 3 executed")
        self.attribute3.append(self.attribute1)

    def method4(self):
        print("Method 4 executed")
        self.attribute1 -= 1

    def method5(self):
        print("Method 5 executed")
        self.attribute2 = self.attribute2.replace("World", "Python")

    def method6(self):
        print("Method 6 executed")
        self.attribute3.pop()

    def method7(self):
        print("Method 7 executed")
        self.attribute1 += 10

    def method8(self):
        print("Method 8 executed")
        self.attribute2 += " is amazing"

    def method9(self):
        print("Method 9 executed")
        self.attribute3 = [1, 2, 3]

    def method10(self):
        print("Method 10 executed")
        self.attribute1 -= 10

# Example of a Large Class (with many lines of code)
class LargeClass:
    def __init__(self):
        self.data = []
        self.length = 0

    def add_data(self, value):
        self.data.append(value)
        self.length += 1

    def remove_data(self, value):
        if value in self.data:
            self.data.remove(value)
            self.length -= 1

    def get_data(self):
        return self.data

    def count_data(self):
        return self.length

    def clear_data(self):
        self.data = []
        self.length = 0

    def find_max(self):
        return max(self.data) if self.data else None

    def find_min(self):
        return min(self.data) if self.data else None

    def calculate_average(self):
        return sum(self.data) / len(self.data) if self.data else 0

    def display_data(self):
        print(self.data)

    def data_size(self):
        return len(self.data)

    def add_multiple_data(self, values):
        self.data.extend(values)
        self.length += len(values)

    def remove_multiple_data(self, values):
        for value in values:
            if value in self.data:
                self.data.remove(value)
                self.length -= 1

    def data_sum(self):
        return sum(self.data)
