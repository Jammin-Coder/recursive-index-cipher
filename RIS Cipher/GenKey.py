#!/usr/bin/python3

import Funcs

funcs = Funcs.Funcs()


class GenKey:
    def __init__(self, charset):
        self.key = ""
        self.charset = list(charset)
        self.len = len(charset)
        self.max_index = self.len - 1
        self.run()

    def scramble(self):
        scramble_count = 4
        for i in range(self.len * scramble_count):
            rand_index1 = funcs.rand(0, self.max_index)
            rand_index2 = funcs.rand(0, self.max_index)
            char1 = self.charset[rand_index1]
            char2 = self.charset[rand_index2]
            self.charset[rand_index1] = char2
            self.charset[rand_index2] = char1
        return funcs.stringify(self.charset)

    def gen_key(self):
        for i in range(self.len):
            rand_index = funcs.rand(0, self.max_index)
            self.key += self.charset[rand_index]

    def run(self):
        scrambled_charset = self.scramble()
        self.gen_key()
        funcs.write_file("key.txt", self.key)
        funcs.write_file("scramble.txt", scrambled_charset)


charset = funcs.read_file("charset.txt")
GenKey(charset)
