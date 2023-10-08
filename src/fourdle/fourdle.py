import random


class Fourdle:
    def __init__(self, word_list):
        self.word_history = []
        self.word_list = word_list
        self.target_word = ""


    def validate_word(self, guess: str):
        hint = ''
        target_word_list = list(self.target_word)
        
        # First pass: Check for letters in the correct positions ('G')
        for g, t in zip(guess, target_word_list):
            if g == t:
                hint += 'G'
                target_word_list[target_word_list.index(g)] = None  # Mark as used
            else:
                hint += 'X'  # Placeholder
        
        # Second pass: Check for correct letters in the wrong positions ('Y')
        for i, (g, h) in enumerate(zip(guess, hint)):
            if h == 'X':  # Only check the letters that were not already marked 'G'
                if g in target_word_list:
                    hint = hint[:i] + 'Y' + hint[i+1:]
                    target_word_list[target_word_list.index(g)] = None  # Mark as used

        # Replace remaining 'X' placeholders with 'W'
        hint = hint.replace('X', 'W')

        return hint


    def set_random_word(self):
        self.target_word = random.choice(self.word_list)

    def set_target_word(self, word: str):
        self.target_word = word

    @staticmethod
    def load_words_from_file(file_path: str) -> list:
        with open(file_path, 'r') as f:
            return f.read().splitlines()

def main():
    word_path = "data/words.txt"
    word_list = Fourdle.load_words_from_file(word_path)
    fourdle = Fourdle(word_list)
    fourdle.set_random_word()
    colors = fourdle.validate_word("flop")
    print(colors)

if __name__=="__main__":
    main()