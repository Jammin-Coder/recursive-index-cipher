#!/usr/bin/python3

import Funcs

funcs = Funcs.Funcs()


class Decode:
    def __init__(self, key, text, chars, num_times):
        self.key = key
        self.text = text
        self.num_times = num_times
        self.chars = chars

    def add_index_value(self, key_char, text_char, key_len):
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
            new_value = self.add_index_value(key_char, text_char, key_len)
            encoded_string += new_value
            i += 1
        return text

    def run(self):
        text = self.text
        for i in range(self.num_times + 1):
            print(f"Round {i} >> {text}")
            text = self.decode(text, self.key)


key = funcs.read_file("key.txt")
chars = funcs.read_file("scramble.txt")
text = funcs.read_file("encrypted.txt")

decoder = Decode(key, text, chars, 10)
decoder.run()
