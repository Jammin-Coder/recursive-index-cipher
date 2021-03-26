# Recursive Index Cipher
This program encrypts text using a random key, and a scrambled character set.  
It's decrypted using the same random key, and the same scrambled character set.
  
This program is written specifcaly for Python3, so run it with a Pyhton3 interpreter, using:  
`python3 encoder.py`  
Or  
`python3 decoder.py`  

## How exactly this program works.
### Encoder:  
The encoder starts by reading the charset file, which contains all of the characters that  
can be used in the program. Then a random key is generated using those characters.  
Then you enter some text to encrypt. Every character has its own index value. Its value is determined by the 
order of the characters in the "scramble.txt" file. The first character's index value is 0, the last is the 
number of characters - 1, (or 66, for now).  

The main decode method loops over the characters of the text and key, and adds their index values together. 
If that value is greater than the length of the key, the key length is subracted from the value's total. It  
then uses that value to grab a character from the "scramble.txt" file at whatever index the value holds; this 
character is now the ciphered version of the plain text character. Since the key is almost definitely longer 
than the text, when the loop reaches the length of the original text, the text is set to the ciphered text, 
and then the loop goes back to the beginning of the text, which has now gone through 1 round of ciphering. It 
repeats this process for the length of the key.

### Decoder:
The decoder first reads teh contents of "scramble.txt" and "key.txt". Other than that, 
the decoder works the same way, except it subtracts the key index values from the text index values.
