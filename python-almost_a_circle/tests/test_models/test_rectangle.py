import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    
    def test_valid_width_height(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
    def test_valid_width_height_x(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
    def test_valid_width_height_x_y(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
    # def test_invalid_extra_argument(self):
    #     with self.assertRaises(TypeError):
    #         Rectangle(1, 2, 3, 4, 5)
    def test_invalid_width_value(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
    def test_invalid_height_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
    def test_invalid_x_value(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
    def test_invalid_y_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
    def test_invalid_x_negative_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
    def test_invalid_y_negative_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
    def test_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)
    def test_str(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (5) 3/4 - 1/2")
    # def test_display_without_x_y(self):
    #     rect = Rectangle(3, 2)
    #     self.assertEqual(rect.display(), "###\n###\n")
    # def test_display_without_y(self):
    #     rect = Rectangle(3, 2, 1)
    #     self.assertEqual(rect.display(), " ###\n ###\n")
    # def test_display(self):
    #     rect = Rectangle(3, 2, 1, 1)
    #     self.assertEqual(rect.display(), "\n ###\n ###\n")
    def test_to_dictionary(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(rect.to_dictionary(), expected_dict)
    def test_update(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, 7, 8, 9, 10)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 10)
    # def test_update_args(self):
    #     rect = Rectangle(1, 2, 3, 4, 5)
    #     rect.update(6)
    #     self.assertEqual(rect.id, 6)
    #     self.assertEqual(rect.width, 2)
    #     self.assertEqual(rect.height, 4)
    #     self.assertEqual(rect.x, 3)
    #     self.assertEqual(rect.y, 4)
    def test_update_args_width_height(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, 7, 8)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
    def test_update_args_width_height_x(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, 7, 8, 9)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 4)
    def test_update_args_width_height_x_y(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, 7, 8, 9, 10)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 10)
    def test_update_kwargs(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(**{'id': 6})
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
    def test_update_kwargs_width_height(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(**{'id': 6, 'width': 7, 'height': 8})
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
    def test_update_kwargs_width_height_x(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(**{'id': 6, 'width': 7, 'height': 8, 'x': 9})
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 4)
    def test_update_kwargs_width_height_x_y(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(**{'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10})
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 10)
    # def test_create_id(self):
    #     rect = Rectangle.create(**{'id': 6})
    #     self.assertEqual(rect.id, 6)
    #     self.assertEqual(rect.width, 1)
    #     self.assertEqual(rect.height, 1)
    #     self.assertEqual(rect.x, 0)
    #     self.assertEqual(rect.y, 0)
    # def test_create_id_width_height(self):
    #     rect = Rectangle.create(**{'id': 6, 'width': 7, 'height': 8})
    #     self.assertEqual(rect.id, 6)
    #     self.assertEqual(rect.width, 7)
    #     self.assertEqual(rect.height, 8)
    #     self.assertEqual(rect.x, 0)
    #     self.assertEqual(rect.y, 0)
    # def test_create_id_width_height_x(self):
    #     rect = Rectangle.create(**{'id': 6, 'width': 7, 'height': 8, 'x': 9})
    #     self.assertEqual(rect.id, 6)
    #     self.assertEqual(rect.width, 7)
    #     self.assertEqual(rect.height, 8)
    #     self.assertEqual(rect.x, 9)
    #     self.assertEqual(rect.y, 0)
    # def test_create_id_width_height_x_y(self):
    #     rect = Rectangle.create(
    #         **{'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10})
    #     self.assertEqual(rect.id, 6)
    #     self.assertEqual(rect.width, 7)
    #     self.assertEqual(rect.height, 8)
    #     self.assertEqual(rect.x, 9)
    #     self.assertEqual(rect.y, 10)
if __name__ == '__main__':
    unittest.main()
#     def test_triangle_with_two_arguments(self):
#         r1 = Rectangle(1, 2)
        
#         self.assertEqual(r1.width, 1)
#         self.assertEqual(r1.height, 2)
        
#     def test_triangle_with_tree_arguments(self):
#         r2 = Rectangle(1, 2, 3)
        
#         self.assertEqual(r2.width, 1)
#         self.assertEqual(r2.height, 2)
#         self.assertEqual(r2.x, 3)
        
#     def test_triangle_with_four_arguments(self):
#         r3 = Rectangle(1, 2, 3, 4)
        
#         self.assertEqual(r3.width, 1)
#         self.assertEqual(r3.height, 2)
#         self.assertEqual(r3.x, 3)
#         self.assertEqual(r3.y, 4)
        
#     def test_triangle_with_five_arguments(self):
#         r4 = Rectangle(1, 2, 3, 4, 5)
        
#         self.assertEqual(r4.width, 1)
#         self.assertEqual(r4.height, 2)
#         self.assertEqual(r4.x, 3)
#         self.assertEqual(r4.y, 4)
#         self.assertEqual(r4.id, 5)