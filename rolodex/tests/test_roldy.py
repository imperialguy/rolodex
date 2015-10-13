from rolodex.roldy import Rolodex
from unittest import TestCase
from copy import deepcopy
import yaml
import json
import os


class TestRolodex(TestCase):

    def setUp(self):
        self.valid_cases = {
            'case001.in': 'case001.out',
            'case002.in': 'case002.out'
        }
        self.invalid_cases = {
            'case003.in': 'case003.out',
            'case004.in': 'case004.out'
        }
        self.base_dir = os.path.dirname(__file__)
        self.rolodex_config_file = os.path.abspath(os.path.join(
            self.base_dir, '..', 'data', 'config.yaml'))
        self.rolodex_fixtures = os.path.abspath(os.path.join(
            self.base_dir, '..', 'fixtures'))

        with open(self.rolodex_config_file, 'r') as f:
            self.rolodex_config = yaml.load(f)

    def test_valid_cases(self):
        for case_in, case_out in self.valid_cases.iteritems():
            config = deepcopy(self.rolodex_config)
            config['input'] = os.path.join(
                self.rolodex_fixtures, case_in)
            expected_output_json = os.path.join(
                self.rolodex_fixtures, case_out)

            with open(expected_output_json, 'r') as f:
                expected_output = json.load(f)

            rolodex = Rolodex(config)
            rolodex_output = rolodex.dump(False)
            self.assertEqual(rolodex_output, expected_output)

    def test_invalid_cases(self):
        for case_in, case_out in self.invalid_cases.iteritems():
            config = deepcopy(self.rolodex_config)
            config['input'] = os.path.join(
                self.rolodex_fixtures, case_in)
            expected_output_json = os.path.join(
                self.rolodex_fixtures, case_out)

            with open(expected_output_json, 'r') as f:
                expected_output = json.load(f)

            rolodex = Rolodex(config)
            rolodex_output = rolodex.dump(False)
            self.assertEqual(rolodex_output, expected_output)

if __name__ == '__main__':
    unittest.main()
