#!/usr/bin/python3

import Funcs


funcs = Funcs.Funcs()

class Encode:
    def __init__(self, chars):
        self.chars = list(chars)
        self.len = len(chars)
        self.max_index = self.len - 1
        self.run()

    def scramble(self):
        for i in range(self.len * 4):
            rand_index1 = funcs.rand(0, self.max_index)
            rand_index2 = funcs.rand(0, self.max_index)
            char1 = self.chars[rand_index1]
            char2 = self.chars[rand_index2]
            self.chars[rand_index1] = char2
            self.chars[rand_index2] = char1
        scrambled_string = funcs.stringify(self.chars)
        print(scrambled_string)
        funcs.write_file("scramble.txt", scrambled_string)

    def gen_key(self):
        key = ""
        for i in range(self.len):
            rand_index = funcs.rand(0, self.max_index)
            key += self.chars[rand_index]
        return key

    def add_index_value(self, key_char, text_char, key_len):
        key_char_ind = self.chars.index(key_char)
        text_ind = self.chars.index(text_char)
        new_value = key_char_ind + text_ind
        if new_value >= key_len:
            new_value -= key_len

        return self.chars[new_value]

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
            new_value = self.add_index_value(key_char, text_char, key_len)
            encoded_string += new_value
            i += 1
        return text

    def multi_encode(self, text, key, times):
        for i in range(times):
            new_text = self.encode(text, key)
            text = new_text
        return text

    def run(self):
        self.scramble()
        key = self.gen_key()
        text = str(input("Enter Text to encode >> "))
        encoded_text = self.multi_encode(text, key, 10)

        print(f"X>>>{encoded_text}<<<X")
        funcs.write_file("encrypted.txt", encoded_text)
        funcs.write_file("key.txt", key)
        funcs.write_file("encrypted.txt", encoded_text)


chars = funcs.read_file("charset.txt")
Encode(chars)
