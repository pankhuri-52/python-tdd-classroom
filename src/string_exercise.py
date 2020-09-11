class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        return input_str[::-1]

    def is_english_vowel(self, character):
        vowels = 'aeiouAEIOU'
        return character in vowels

    def find_longest_word(self, sentence):
        list_words = sentence.split()
        max_len = len(max(list_words, key=len))
        final_list = [word for word in list_words if len(word) == max_len]
        return ''.join(map(str, final_list[0]))

    def get_word_lengths(self, text):
        return list(map(len, text.split()))