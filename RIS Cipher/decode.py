#!/usr/bin/python3

import Funcs

funcs = Funcs.Funcs()


class Decode:
    def __init__(self, key, text, charset, num_times):
        self.charset = charset
        self.charset_len = len(charset)
        self.key = key
        self.text = text
        self.num_times = num_times
        self.run()

    def decode_char(self, key_char, text_char):
        """
        This function takes a character from the key an the input text,
        gets both of their indices, and subtracts the key character index value
        from the text character index value.
        For example:
        say key_char is y, and is at index 7 in the key file,
        and say text_char is b, and is at index 19 in the scrambled charset file.
        When these values are added up, the new index is 12.
        The function returns whatever character is at the new index.
        If the new value is less than 0, Then the length of the charset is
        added to the value, so no "IndexOutOfRange" error.
        """
        key_char_ind = self.charset.index(key_char)  # Gets the index of the key char in the charset
        text_char_ind = self.charset.index(text_char)  # Gets the index of the text char in the charset
        decoded_value = text_char_ind - key_char_ind  # subtracts key_index value from text_char_index.

        if decoded_value < 0:
            # If the new index is less than 0, add the length of the charset to the index
            # value. This way we don't get an "IndexOutOfRange" error.
            # NOTE: This may not actually be necessary for subtracting list indices, I think it does it automatically
            decoded_value += self.charset_len

        return self.charset[decoded_value]  # Returns an encoded character

    # main decode algorithm
    def decode(self):
        for i in range(self.num_times):
            self.text = funcs.cipher(self.text, self.key, self.charset, "d")

    # Runs the above method as many times specified, each time replacing the text with the
    # encoded text. This we can decode code that was encoded multiple times.

    def run(self):
        self.decode()
        print(self.text)


key = funcs.read_file("key.txt")
chars = funcs.read_file("scramble.txt")
text = funcs.read_file("encrypted.txt")

Decode(key, text, chars, 10)
