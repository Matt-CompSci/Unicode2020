def romanToInt(str):
    romanNumerals = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
    }

    integerValue = 0

    for idx in range(len(str)):
        if idx > 0 and romanNumerals[str[idx]] > romanNumerals[str[idx - 1]]:
            integerValue += romanNumerals[str[idx]] - 2 * romanNumerals[str[idx - 1]]
        else:
            integerValue += romanNumerals[str[idx]]

    return integerValue

# Tests
print(romanToInt("MCMLXI") == 1961)
print(romanToInt("III") == 3)
print(romanToInt("IV") == 4)
print(romanToInt("IX") == 9)
print(romanToInt("LVIII") == 58)
print(romanToInt("MCMXCIV") == 1994)
print(romanToInt("LXXIII") == 73)
print(romanToInt("MMXV") == 2015)

