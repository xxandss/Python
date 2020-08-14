import unittest

from rect import Rect


class RectTest(unittest.TestCase):
    def test_intersect_for_crossing_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1, 1, 0.5, 0.5)))
    
    def test_intersect_for_right_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1.5, 1, 0.5, 0.5)))

    def test_intersect_for_up1_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1.5, 1.5, 0.5, 0.5)))

    def test_intersect_for_up2_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1, 1.5, 0.5, 0.5)))
        
    def test_intersect_for_left1_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(0.5, 1.5, 0.5, 0.5)))
        
    def test_intersect_for_left2_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(0.5, 1, 0.5, 0.5)))
        
    def test_intersect_for_down1_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(0.5, 0.5, 0.5, 0.5)))
        
    def test_intersect_for_down2_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1, 0.5, 0.5, 0.5)))
        
    def test_intersect_for_w_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(-1, 1, 4, 0.5)))
    
    def test_intersect_for_h_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1, -5, 0.5, 8)))


if __name__ == '__main__':
    unittest.main()
