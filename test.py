import unittest

from Start import SearchInDataBaseBYDate, SearchInDataBaseBYAcident


obj1 = {"_id": 1, "id": 1, "name": "John", "age": 20, "address": "Highway 37", "Phone": "0100000", "height": 170,
        "weight": 60, "MedicalHistory": "sokar", "Date": "2020-12-25", "Doctor_Name": "magdy", "Diagnose": "Eds", "Accident": "Car Accident"}
obj2 = {"_id": 2, "id": 2, "name": "ahmed", "age": 30, "address": "imbaba", "Phone": "0100000", "height": 180, "weight": 80,
        "MedicalHistory": "sokar", "Date": "2020-11-25", "Doctor_Name": "hassan", "Diagnose": "cancer", "Accident": "Bus Accident"}
obj3 = {"_id": 3, "id": 1, "name": "ahmed", "age": 30, "address": "imbaba", "Phone": "0100000", "height": 180, "weight": 80,
        "MedicalHistory": "sokar", "Date": "2010-11-25", "Doctor_Name": "hassan", "Diagnose": "cancer", "Accident": "Train Accident"}


class UnitTest(unittest.TestCase):
    def test1_SearchInDataBaseBYDate(self):
        result = SearchInDataBaseBYDate(1, "2020-12-25")
        self.assertEqual(result[0], obj1)

    def test2_SearchInDataBaseBYDate(self):
        result = SearchInDataBaseBYDate(1, "2010-11-25")
        self.assertEqual(result[0], obj3)

    def test1_SearchInDataBaseBYAcident(self):
        result = SearchInDataBaseBYAcident(1, "Car Accident")
        self.assertEqual(result[0], obj1)

    def test2_SearchInDataBaseBYAcident(self):
        result = SearchInDataBaseBYAcident(1, "Train Accident")
        self.assertEqual(result[0], obj3)


if __name__ == '__main__':
    unittest.main()
