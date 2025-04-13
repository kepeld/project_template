import unittest
import os
import pandas as pd
from app.io import input

class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        with open("data/test_input.txt", "w", encoding="utf-8") as f:
            f.write("Hello from test file!")

        df = pd.DataFrame({
            "name": ["Alice", "Bob"],
            "score": [90, 85]
        })
        df.to_csv("data/test_input.csv", index=False)

    def tearDown(self):
        os.remove("data/test_input.txt")
        os.remove("data/test_input.csv")

    def test_read_from_file_exact_match(self):
        result = input.read_from_file("data/test_input.txt")
        self.assertEqual(result, "Hello from test file!")

    def test_read_from_file_not_empty(self):
        result = input.read_from_file("data/test_input.txt")
        self.assertTrue(len(result) > 0)

    def test_read_from_file_contains_word(self):
        result = input.read_from_file("data/test_input.txt")
        self.assertIn("Hello", result)

    def test_read_with_pandas_shape(self):
        df = input.read_with_pandas("data/test_input.csv")
        self.assertEqual(df.shape, (2, 2))

    def test_read_with_pandas_column_names(self):
        df = input.read_with_pandas("data/test_input.csv")
        self.assertListEqual(list(df.columns), ["name", "score"])

    def test_read_with_pandas_row_values(self):
        df = input.read_with_pandas("data/test_input.csv")
        self.assertEqual(df.loc[0, "name"], "Alice")
        self.assertEqual(df.loc[1, "score"], 85)

if __name__ == '__main__':
    unittest.main()
