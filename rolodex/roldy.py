from collections import OrderedDict
from operator import itemgetter
import argparse
import ntpath
import yaml
import json
import os
import re
import sys


class Rolodex(object):

    def __init__(self, config):
        self.base_dir = os.path.dirname(__file__)
        self.config = config
        self.input = self.config['input']
        self.output = os.path.abspath(os.path.join(
            self.base_dir, 'data', self.config['output_filename']))
        self.entries = []
        self.errors = []

    def dump(self, to_file=True):
        self._setup_config()
        self._fileparser()

        if not to_file:
            return self.output_dict

        with open(self.output, 'wb') as f:
            json.dump(self.output_dict, f, indent=self.config['json_indent'])
        print 'output available at: {}'.format(self.output)

    def _setup_config(self):
        for idx, processor in enumerate(self.config['processors']):
            self.config['processors'
                        ][idx]['patterns'] = [re.compile(
                            pattern, re.IGNORECASE
                        ) for pattern in processor['patterns']]

    def _fileparser(self):
        with open(self.input, 'r') as f:
            for idx, line in enumerate(f):
                if len(line.split(',')) in (4, 5):
                    output = self._lineparser(line)
                    if output:
                        self.entries.append(output)
                    else:
                        self.errors.append(idx)
                else:
                    self.errors.append(idx)
        self.entries = sorted(
            self.entries, key=itemgetter(*self.config['sort_keys']))
        self.output_dict = OrderedDict(
            [('entries', self.entries), ('errors', self.errors)])

    def _lineparser(self, line):
        for processor in self.config['processors']:
            for pattern in processor['patterns']:
                match_object = re.search(pattern, line)
                if match_object:
                    line_content = [i.strip() for i in match_object.groups()]
                    line_content[processor[
                        'phonenumber_idx']] = '-'.join(re.findall(
                            '\d+', line_content[processor['phonenumber_idx']]))
                    return OrderedDict(sorted(zip(
                        processor['format'], line_content
                    )))
        return None


def main():
    config_file = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'data', 'config.yaml'))

    with open(config_file, 'r') as f:
        config = yaml.load(f)

    config['input'] = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'data', 'data.in'))

    Rolodex(config).dump()


if __name__ == '__main__':
    main()
