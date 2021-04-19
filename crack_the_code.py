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
