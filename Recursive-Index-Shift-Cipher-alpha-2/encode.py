#!/usr/bin/python3

import Funcs
import argparse

funcs = Funcs.Funcs()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key-dir", dest="key_dir", help="Directory where the desired key and scrambled charset are located.")
    parser.add_argument("-i", "--in_file", dest="in_file", help="Input text file.")
    parser.add_argument("-o", "--outfile", dest="outfile", help="File to output encoded text.")
    args = parser.parse_args()
    if not args.key_dir:
        parser.error("[-] Please specify a key directory to use.")
    if not args.in_file:
        parser.error("[-] Please specify an input file.")
    if not args.outfile:
        parser.error("[+] Please specify an output file")
    return args


class Encode:
    def __init__(self, in_file, out_file, key_dir, num_times):
        self.chars = list(funcs.read_file(f"{key_dir}/scrambled_charset.txt"))
        self.key = funcs.read_file(f"{key_dir}/key.txt")
        self.text = funcs.read_file(in_file)
        self.num_times = num_times
        self.out_file = out_file
        self.run()

    def encode(self, text, key):
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
            new_value = funcs.add_index_value(self.chars, key_char, text_char, key_len)
            encoded_string += new_value
            i += 1
        return text

    def multi_encode(self, text):
        for i in range(self.num_times):
            new_text = self.encode(text, self.key)
            text = new_text
        return text

    def run(self):
        text = self.multi_encode(self.text)
        funcs.write_file(self.out_file, text)


args = get_args()
key_dir = args.key_dir
in_file = args.in_file
outfile = args.outfile

Encode(in_file, outfile, key_dir, 4)
