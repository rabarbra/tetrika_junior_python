#-*- encoding: utf-8 -*-
import unittest
from appearance import appearance, intersect_interval_arrays

class TaskTestCase(unittest.TestCase):
    def test_intersect_interval_arrays(self):
        self.assertEqual(intersect_interval_arrays([0, 0], [0, 0]), [])
        self.assertEqual(intersect_interval_arrays([0, 1], [0, 0]), [0, 0])
        self.assertEqual(intersect_interval_arrays([0, 0], [0, 1]), [])
        self.assertEqual(intersect_interval_arrays([0, 1], [0, 1]), [0, 1])
        self.assertEqual(intersect_interval_arrays([0, 5], [0, 3]), [0, 3])
        self.assertEqual(intersect_interval_arrays([0, 1, 5, 10, 60, 200], [1, 6, 40, 100]), [5, 6, 60, 100])

    def test_appearance(self):
        self.assertEqual(appearance({"lesson": [0, 0],
                                     "pupil": [0, 0],
                                     "tutor": [0, 0]}), 
                                     0)
        self.assertEqual(appearance({"lesson": [0, 1],
                                     "pupil": [0, 0],
                                     "tutor": [0, 0]}), 
                                     0)
        self.assertEqual(appearance({"lesson": [0, 0],
                                     "pupil": [0, 1],
                                     "tutor": [0, 0]}), 
                                     0)
        self.assertEqual(appearance({"lesson": [0, 0],
                                     "pupil": [0, 0],
                                     "tutor": [0, 1]}), 
                                     0)
        self.assertEqual(appearance({"lesson": [0, 1],
                                     "pupil": [0, 1],
                                     "tutor": [0, 0]}), 
                                     0)
        self.assertEqual(appearance({"lesson": [0, 1],
                                     "pupil": [0, 0],
                                     "tutor": [0, 1]}), 
                                     0)
        self.assertEqual(appearance({"lesson": [0, 0],
                                     "pupil": [0, 1],
                                     "tutor": [0, 1]}), 
                                     0)
        self.assertEqual(appearance({"lesson": [0, 1],
                                     "pupil": [0, 1],
                                     "tutor": [0, 1]}), 
                                     1)
        self.assertEqual(appearance({"lesson": [1, 1],
                                     "pupil": [0, 0],
                                     "tutor": [0, 0]}), 
                                     0)
        self.assertEqual(appearance({"lesson": [0, 1],
                                     "pupil": [0, 2],
                                     "tutor": [0, 6]}), 
                                     1)
        self.assertEqual(appearance({"lesson": [1, 4],
                                     "pupil": [0, 5],
                                     "tutor": [0, 3]}), 
                                     2)
        self.assertEqual(appearance({"lesson": [10, 360],
                                     "pupil": [1, 60, 70, 100, 200, 500],
                                     "tutor": [0, 50, 51, 80, 90, 250, 300, 360]}), 
                                     179)

if __name__ == "__main__":
    unittest.main()
