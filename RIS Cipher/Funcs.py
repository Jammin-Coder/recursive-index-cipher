#!/usr/bin/python3

import random


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

    def cipher_char(self, key_char, text_char, charset, mode):
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

        This process is done in reverse when decoding a character.
        """
        charset_len = len(charset)
        key_char_ind = charset.index(key_char)  # Gets the index of the key char in the charset
        text_char_ind = charset.index(text_char)  # Gets the index of the text char in the charset

        # Encode mode
        if mode.lower() == "e":
            encoded_char = key_char_ind + text_char_ind  # Adds up their index values.
            if encoded_char >= charset_len:
                # If the new index is greater than the length of the charset, subtract the length of the charset from the index
                # value. This way we don't get an "IndexOutOfRange" error.
                encoded_char -= charset_len
            return charset[encoded_char]

        # Decode mode
        elif mode.lower() == "d":
            decoded_char = text_char_ind - key_char_ind  # subtracts key_index value from text_char_index.
            if decoded_char < 0:
                # If the new index is less than 0, add the length of the charset to the index
                # value. This way we don't get an "IndexOutOfRange" error.
                # NOTE: This may not actually be necessary for subtracting list indices, I think it does it automatically
                decoded_char += charset_len
            return charset[decoded_char]  # Returns the letter stored at the index new_value

    def cipher(self, text, key, charset, mode):
        encoded_string = ""  # Keeps track of the current encoded text
        text_len = len(text)
        charset_len = len(charset)
        i = 0  # Keeps track of the current working index.
        # I am not using a for-loop for it because its
        # value is reset after it's greater than the length of the text.
        for _ in range(charset_len):
            if i >= text_len:
                # Resets the current index to 0, so the algorithm goes back
                # to the beginning of the text.
                i = 0

            if len(encoded_string) >= text_len:
                i = 0
                text = encoded_string  # Replaces the plain text with the encoded string,
                # so it can be encoded multiple times.
                encoded_string = ""  # Resets the encoded string to be empty.

            text_char = text[i]  # Gets the current text character
            key_char = key[i]  # Gets the current key character
            encoded_char = self.cipher_char(key_char, text_char, charset, mode)  # For info, check out the "decode_char" method above.
            encoded_string += encoded_char  # Appends encoded_char to the encoded string.
            i += 1  # Increments the current working index so we move onto the next character.
        return text
