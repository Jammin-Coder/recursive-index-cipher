#!/usr/bin/python3

import Funcs
import argparse
funcs = Funcs.Funcs()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key-dir", dest="key_dir", help="Directory where the desired key and scrambled charset are located.")
    parser.add_argument("-i", "--in_file", dest="in_file", help="Input text file.")
    args = parser.parse_args()
    if not args.key_dir:
        parser.error("[-] Please specify a key directory to use.")
    if not args.in_file:
        parser.error("[-] Please specify an input file.")
    return args


class Decode:
    def __init__(self, text, key_dir, num_times):
        self.key = funcs.read_file(f"{key_dir}/key.txt")
        self.chars = funcs.read_file(f"{key_dir}/scrambled_charset.txt")
        self.text = funcs.read_file(text)
        self.num_times = num_times
        self.run()

    def sub_index_value(self, key_char, text_char, key_len):
        key_char_ind = self.chars.index(key_char)
        text_ind = self.chars.index(text_char)
        new_value = text_ind - key_char_ind
        if new_value < 0:
            new_value += key_len
        return self.chars[new_value]

    def decode(self, text, key):
        encoded_string = ""
        key_len = len(key)
        text_len = len(text)
        i = 0
        for _ in range(key_len):
            if i >= text_len:
                i = 0

            if len(encoded_string) >= text_len:
                i = 0
                text = encoded_string
                encoded_string = ""

            text_char = text[i]
            key_char = key[i]
            new_value = self.sub_index_value(key_char, text_char, key_len)
            encoded_string += new_value
            i += 1
        return text

    def run(self):
        text = self.text
        for i in range(self.num_times):
            text = self.decode(text, self.key)
        print(f"Decoded to >> {text}")


args = get_args()
in_file = args.in_file
key_dir = args.key_dir

Decode(in_file, key_dir, 4)
