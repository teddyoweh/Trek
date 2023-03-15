import unittest
import json
from trekpy.Trek import Trek

class TestTrek(unittest.TestCase):

    def setUp(self):
        self.trek = Trek('data.json',env='earth')

    def test_load_map(self):
        self.assertIsNotNone(self.trek.map)
        self.assertIsInstance(self.trek.map, dict)

    def test_load_map_graph(self):
        self.assertIsNotNone(self.trek.map_graph)
        self.assertIsInstance(self.trek.map_graph, dict)

    def test_find_optimal_path(self):
        planned = planned =['Engineering Buiding',
 'Library',
 'Nursing Building',
 'Centennial',
 'Rec',
 'Dining Hall',
 'Science Building',
 'Student Center']
        start = 'A'
        end = 'C'
        speed = 3.1
        expected_path = ['Dining Hall', 'Student Center', 'Science Building', 'Nursing Building', 'Centennial', 'Rec']
        expected_detail =  {'path': ('Dining Hall', 'Student Center', 'Science Building', 'Nursing Building', 'Centennial', 'Rec'), 'detail': [{'start': 'Dining Hall', 'end': 'Student Center', 'time': [0.39184021666746505, 1.1068377050431277, 0.4671317937827885, 1.2717470001103144, 1.494750266935083]}, {'start': 'Student Center', 'end': 'Science Building', 'time': [0.39184021666746505, 1.1068377050431277, 0.4671317937827885, 1.2717470001103144, 1.494750266935083]}, {'start': 'Science Building', 'end': 'Nursing Building', 'time': [0.39184021666746505, 1.1068377050431277, 0.4671317937827885, 1.2717470001103144, 1.494750266935083]}, {'start': 'Nursing Building', 'end': 'Centennial', 'time': [0.39184021666746505, 1.1068377050431277, 0.4671317937827885, 1.2717470001103144, 1.494750266935083]}, {'start': 'Centennial', 'end': 'Rec', 'time': [0.39184021666746505, 1.1068377050431277, 0.4671317937827885, 1.2717470001103144, 1.494750266935083]}], 'times': [0.39184021666746505, 1.1068377050431277, 0.4671317937827885, 1.2717470001103144, 1.494750266935083]}

        expected_times = [67.09, 67.09]
        result = self.trek.find_optimal_path(planned, start, end, speed)
        self.assertEqual(result['path'], expected_path)
        self.assertEqual(result['detail'], expected_detail)
        self.assertEqual(result['times'], expected_times)
 
 
   
if __name__ == '__main__':
    unittest.main()
