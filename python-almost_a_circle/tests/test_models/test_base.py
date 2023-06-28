import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    def test_automatic_id(self):
        b1 = Base()

        self.assertEqual(b1.id, 1)

    def test_automatic_increment(self):
        b2 = Base()
        b3 = Base()

        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_saving_id(self):
        b4 = Base(89)
        self.assertEqual(b4.id, 89)

    # def test_base_id_generation(self):
    #     base1 = Base()
    #     base2 = Base()
    #     base3 = Base(89)
    #     self.assertEqual(base1.id, 1)
    #     self.assertEqual(base2.id, 2)
    #     self.assertEqual(base3.id, 89)

    def test_base_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string_with_data(self):
        json_string = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_string, '[{"id": 12}]')

    def test_base_to_json_string_with_data_returning_string(self):
        json_string = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(json_string, str)

    def test_base_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_base_from_json_string_empty_list(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_base_from_json_string_with_data(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{'id': 89}])

    def test_base_from_json_string_with_data_returning_list(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
