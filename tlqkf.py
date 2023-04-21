import sys
import subprocess
from hangul_utils import split_syllable_char, join_jamos

# Define a dictionary to map Korean characters to English characters based on the keyboard layout
korean_to_english = {
    'ㅂ': 'q', 'ㅈ': 'w', 'ㄷ': 'e', 'ㄱ': 'r', 'ㅅ': 't', 'ㅛ': 'y', 'ㅕ': 'u', 'ㅑ': 'i', 'ㅐ': 'o', 'ㅔ': 'p',
    'ㅁ': 'a', 'ㄴ': 's', 'ㅇ': 'd', 'ㄹ': 'f', 'ㅎ': 'g', 'ㅗ': 'h', 'ㅓ': 'j', 'ㅏ': 'k', 'ㅣ': 'l',
    'ㅋ': 'z', 'ㅌ': 'x', 'ㅊ': 'c', 'ㅍ': 'v', 'ㅠ': 'b', 'ㅜ': 'n', 'ㅡ': 'm'
}

def translate_input(input_str):
    translated_str = ''
    for char in input_str:
        if char in korean_to_english:
            translated_str += korean_to_english[char]
        else:
            try:
                jamos = split_syllable_char(char)
                translated_jamos = [korean_to_english.get(jamo, jamo) for jamo in jamos]
                translated_str += join_jamos(translated_jamos)
            except ValueError:
                translated_str += char
    return translated_str


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: tlqkf.py <korean_input>")
        sys.exit(1)

    korean_input = sys.argv[1]
    english_input = translate_input(korean_input)

    # Execute the translated command
    process = subprocess.Popen(english_input.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(stdout.decode('utf-8'))
    else:
        print(stderr.decode('utf-8'))
