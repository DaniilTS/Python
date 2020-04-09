import unittest
import json
from json_parser import json_parse
from Nvector import NVector
from ExternalSort import Exort

vec = NVector([1, 2, 3, 4])
test_vec = NVector([2, 4, 6, 8])

sort = Exort()
arr = []
with open('numbers.txt', 'r') as file:
    for line in file:
        arr.append(int(line))

try_bool = False
try_list = [5, 15, 17, "Meow"]
try_dict = {'r': [222, "13", 12], 't': 1, '1': 'kivi'}
try_dict_none = {'r': [2, None], 'l': 1}
tr = {"8": [False, 77]}
try_str = 'rough'
try_int = 123456
try_float = 1.2324
try_tuple = tuple('hello')
try_none = None
try_error = "ewsd"


class test(unittest.TestCase):

    def test_vec(self):
        self.assertEqual(test_vec.__str__(), (vec + [1, 2, 3, 4]).__str__())
        test_vec - [1, 2, 3, 4]
        self.assertEqual(test_vec.__str__(), (vec - [1, 2, 3, 4]).__str__())
        test_vec * [0, 0, 0, 0]
        self.assertEqual(test_vec.__str__(), (vec * [0, 0, 0, 0]).__str__())
        self.assertEqual(4, vec.__len__())
        self.assertEqual(0, vec.__index__(2))
        self.assertEqual(test_vec.__str__(), (vec.__const_mul__(1).__str__()))

    def test_exort(self):
        self.assertEqual(arr.sort(), sort.sort('numbers.txt'))

    def test_to_json(self):
        self.assertEqual(json.dumps(try_bool), json_parse().to_json(try_bool))
        self.assertEqual(json.dumps(try_dict), json_parse().to_json(try_dict))
        self.assertEqual(json.dumps(try_list), json_parse().to_json(try_list))
        self.assertEqual(json.dumps(try_dict_none), json_parse().to_json(try_dict_none))
        self.assertEqual(json.dumps(try_str), json_parse().to_json(try_str))
        self.assertEqual(json.dumps(try_int), json_parse().to_json(try_int))
        self.assertEqual(json.dumps(tr), json_parse().to_json(tr))
        self.assertEqual(json.dumps(try_float), json_parse().to_json(try_float))
        self.assertEqual(json.dumps(try_tuple), json_parse().to_json(try_tuple))
        self.assertEqual(json.dumps(try_none), json_parse().to_json(try_none))

    def test_loads(self):
        data = json.dumps(try_bool)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(try_dict)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(try_list)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(try_str)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(try_int)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(try_float)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(try_tuple)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(try_none)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        try:
            a = json.loads(try_error)
        except BaseException:
            a = None
        self.assertEqual(a, json_parse().loads(try_error))


if __name__ == '__main__':
    unittest.main()
