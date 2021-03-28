#!/usr/bin/python3

import Funcs
import os
import argparse

funcs = Funcs.Funcs()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--charset", dest="charset", help="Text file with list of characters to be used.")
    parser.add_argument("-o", "--out", dest="out", help="Directory to place the key and the scrambled charset pair.")
    args = parser.parse_args()
    if not args.charset:
        args.charset = "default.txt"
        print("[+] Using default charset.")
    if not args.out:
        parser.error("[-] No output directory specified! Please use -o to specify an output directory.\
                     \n[+] Please use --help for more info.")
    return args


class GenKey:
    def __init__(self, charset_file, out_dir, scramble_count=None):
        if not scramble_count:
            self.scramble_count = 5

        self.out_dir = out_dir
        self.chars = list(funcs.read_file(charset_file))
        self.len = len(self.chars)
        self.max_index = self.len - 1
        self.run()

    def scramble_charset(self):
        for i in range(self.len * self.scramble_count):
            rand_index1 = funcs.rand(0, self.max_index)
            rand_index2 = funcs.rand(0, self.max_index)
            char1 = self.chars[rand_index1]
            char2 = self.chars[rand_index2]
            self.chars[rand_index1] = char2
            self.chars[rand_index2] = char1
        scrambled_string = funcs.stringify(self.chars)
        funcs.write_file(f"{self.out_dir}/scrambled_charset.txt", scrambled_string)

    def gen_key(self):
        key = ""
        for i in range(self.len):
            rand_index = funcs.rand(0, self.max_index)
            key += self.chars[rand_index]
        print(key)
        funcs.write_file(f"{self.out_dir}/key.txt", key)

    def make_key_dir(self):
        self.scramble_charset()
        self.gen_key()

    def run(self):
        fail = False
        try:
            os.mkdir(self.out_dir)
        except OSError:
            opt = input("[-] That directory already exists! Would you like to overwrite it? [y\\N] ")
            if opt.lower() == "y":
                fail = True
                self.make_key_dir()
                print("[+] Operation completed.")
            else:
                exit("[+] Operation aborted.")

        if not fail:
            self.make_key_dir()


args = get_args()
chars = args.charset
out_dir = args.out
GenKey(chars, out_dir)
