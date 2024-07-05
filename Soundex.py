def get_soundex_code(c):
    c = c.upper()
    soundex_mapping = '01230120022455012623010202'
    index = ord(c) - ord('A')
    return soundex_mapping[index] if 0 <= index < len(soundex_mapping) else '0'


def soundex_length(soundex):
    if len(soundex) > 4:
        soundex = soundex[:4]
    return soundex

def char_mapping(soundex, name, prev_code):
    for char in name[1:]:
        code = get_soundex_code(char)        
        if code != '0' and code != prev_code:
            soundex += code
            prev_code = code
        soundex = soundex_length(soundex)
    return soundex

def generate_soundex(name):
    if not name:
        return ""

    # Start with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
    soundex = char_mapping(soundex, name, prev_code)
 
    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')

    return soundex
