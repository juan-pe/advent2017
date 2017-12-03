from unittest import TestCase


class TestDay1(TestCase):

    def setUp(self):
        self.inputs = {
            '1122': 3,
            '1111': 4,
            '1234': 0,
            '91212129': 9
        }

    def test_day1_1part(self):
        for input_, result in self.inputs.items():
            sum_list = self.count(input_)
            if input_[0] == input_[-1]:
                sum_list.append(int(input_[0]))

            test_res = sum(sum_list)

            self.assertEqual(test_res, result)

    def count(self, number_list):
        first, *tail = number_list

        if len(tail) == 1:
            return [int(first)] if first == tail[0] else []

        if first == tail[0]:
            return [int(first)] + self.count(tail)
        else:
            return self.count(tail)
