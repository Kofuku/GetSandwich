import unittest
import GetSandwich

class GetSandwichTest(unittest.TestCase):

    get_sandwich_object = GetSandwich.GetSandwich()

    def test_should_return_empty_string(self):
        string_t1 = "bread"
        self.assertEquals("", self.get_sandwich_object.get_sandwich(string_t1))

    def test_should_return_sandwich_guts_no_garbage(self):
        string_t2 = "breadarugulabread"
        self.assertEquals("arugula", self.get_sandwich_object.get_sandwich(string_t2))

    def test_should_return_sandwich_guts_garbage(self):
        string_t3 = "zzzbreadtomatobreadyyy"
        self.assertEquals("tomato", self.get_sandwich_object.get_sandwich(string_t3))

if __name__ == '__main__':
    unittest.main()