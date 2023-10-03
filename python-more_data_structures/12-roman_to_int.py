#!/usr/bin/python3
def roman_to_int(roman_string):
    romani_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    prev = 0
    result = 0

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    for rom in reversed(roman_string):
        if rom not in romani_dict:
            return 0
        now = romani_dict.get(rom)
        if now >= prev:
            result += now
        else:
            result -= now
        prev = now
    return result
