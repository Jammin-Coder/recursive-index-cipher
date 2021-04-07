#!/usr/bin/python3

import Funcs


funcs = Funcs.Funcs()  # Some functions that I use a lot

class Encode:
    def __init__(self, text, charset, key, num_times):
        self.charset = charset
        self.charset_len = len(charset)
        self.key = key
        self.text = text  # At first, this holds the input text. As the program runs, its value is updated to the encoded text.
        self.num_times = num_times
        self.run()

    def encode_char(self, key_char, text_char):
        """
        This function takes a character from the key an the input text,
        gets both of their indices, and adds them together.
        For example:
        say key_char is y, and is at index 6 in the key file,
        and say text_char is b, and is at index 20 in the scrambled charset file.
        When these values are added up, the new index is 26.
        The function returns whatever character is at the new index.
        If the new value is larger than the length of the charset
        Then the length of the charset is subtracted from the value, so no "IndexOutOfRange" error.
        """
        key_char_ind = self.charset.index(key_char)  # Gets the index of the key char in the charset
        text_ind = self.charset.index(text_char)  # Gets the index of the text char in the charset
        new_index = key_char_ind + text_ind  # Adds up their index values.

        # If the new index is greater than the length of the charset, subtract the length of the charset from the index
        # value. This way we don't get an "IndexOutOfRange" error.
        if new_index >= self.charset_len:
            new_index -= self.charset_len

        return self.charset[new_index]  # Returns the letter stored at the index new_value

    # The main encoded algorithm
    def encode(self):
        for i in range(self.num_times):
            self.text = funcs.cipher(self.text, self.key, self.charset, "e")

    def run(self):
        self.encode()
        print(f"#>>>{self.text}<<<#")
        funcs.write_file("encrypted.txt", self.text)


chars = funcs.read_file("scramble.txt")
key = funcs.read_file("key.txt")
text = "This is the cleaned up version of this.\n IT HAD BETTER WORK. Or I will cry."
Encode(text, chars, key, 10)
