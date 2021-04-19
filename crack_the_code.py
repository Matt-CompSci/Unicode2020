def cipher(str, key):
    return "".join(map(lambda char: chr((ord(char) - (char.isupper() and ord("A") or ord("a")) + key) % 26 + (char.isupper() and ord("A") or ord("a"))) if char.isalpha() else char, str))

  # Tests
print(cipher("Zwddg ogjdv!", 8) == "Hello world!")
print(cipher("Yvccf nficu!", 9) == "Hello world!")
print(cipher("Kyv t*uv zj 1: gcvrjv ivjgfeu!", 9) == "The c*de is 1: please respond!")
print(cipher("Qnuux fxaum!", -9) == "Hello world!")
print(cipher("Ifmmp xpsme!", 25) == "Hello world!")
print(cipher("Hello world!", 0) == "Hello world!")
print(cipher("Gdkkn vnqkc!", -25) == "Hello world!")
print(cipher("123 ! *()", 1) == "123 ! *()")

# If you are reading this, then you are the Resistance.
# 
# Multiple communications have filtered into Resistance HQ from several separate cells that suggest the enemy is moving a highly classified asset. Currently we cannot confirm the truth of these claims.
# 
# After an unsuccessful resistance counter-intelligence operation the enemy are aware we broke their previous code and have updated their encryption accordingly. Now every half hour a new key is set, rendering the previous cipher obsolete.
# 
# Worse still, the Resistance itself is now under threat.
# 
# This is a blanket message being sent on all channels to every cell known to be in operation – we need you to write us a program that can crack the new cipher.
# 
# What we know:
# 
#     The new cipher has two components, a string and a cipher key.
#     It returns a string in which each letter is shifted by the cipher key.
#     Punctuation and spacing are not removed but are unaffected by the cipher.
#     Numbers are not removed but are unaffected by the cipher.
#     The case of each letter is maintained regardless of cipher applied.
#     If the key was set to 5, a -> f, b -> g, u -> z, v -> a, w -> b, A -> F, B -> G and so on
# 
# For example: given a string "Zwddg ogjdv!" and a cipher key of 8, the result would be "Hello world!"
# 
# You now know everything that we do. Good luck, stay safe and remember:
# 
# If you are reading this, then you are the Resistance.
