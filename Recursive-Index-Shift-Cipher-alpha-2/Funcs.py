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

    def add_index_value(self, chars, key_char, text_char, key_len):
        key_char_ind = chars.index(key_char)
        text_ind = chars.index(text_char)
        new_value = key_char_ind + text_ind
        if new_value >= key_len:
            new_value -= key_len

        return chars[new_value]
