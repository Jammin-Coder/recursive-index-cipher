#!/usr/bin/python3

import random
import argparse


class Funcs:
    def read_file(self, path):
        with open(path, "r") as f:
            content = f.read()
        return content

    def write_file(self, path, content):
        with open(path, "w") as f:
            f.write(content)

    def rand(self, low, max):
        return round(random.random() * max) + low

    def stringify(self, array):
        string = ""
        for item in array:
            string += str(item)
        return string

    def get_args(self, args_array):
        parser = argparse.ArgumentParser()
        for i in range(len(args_array)):
            short_flag = f"{args_array[i][i]}"
            long_flag = f"{args_array[i][i+1]}"
            dest = f"{args_array[i][i+2]}"
            help = f"{args_array[i][i+3]}"
            parser.add_argument(short_flag, long_flag, dest=dest, help=help)
        return parser.parse_args()
