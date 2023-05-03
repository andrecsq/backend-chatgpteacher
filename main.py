from domain.chatgpt.gpthandler import GPTHandler
import pandas as pd
from constants import PHRASES_FILEPATH, QUIT_COMMANDS

df_phrases = pd.read_csv(PHRASES_FILEPATH)

df_phrases = df_phrases.sample(frac=1).reset_index(drop=True)

print("EXAMPLE PHRASES:")
print(df_phrases.head())
print("-" * 100)

handler = GPTHandler()

def handle_exit(total_translations, correct_translations):
    print(f"correct: {correct_translations}")
    print(f"wrong: {total_translations - correct_translations}")
    print(f"total: {total_translations}")


if __name__ == '__main__':
    count = 0
    num_correct = 0
    while (True):
        phrase_english = df_phrases['phrase_english'][count]
        print(f"Translate \"{phrase_english}\" from English to Portuguese")
        user_translation = input(">> ")

        if user_translation.lower() in QUIT_COMMANDS:
            handle_exit(count, num_correct)
            break

        response = handler.correct_translation(phrase_english, user_translation)
        clean_response = response.strip()
        if ("is correct" in clean_response):
            print("CORRECT!!!")
            num_correct += 1
        else:
            print("WRONG!!!")
        
        print(clean_response)

        phrase_portuguese = df_phrases['phrase_portuguese'][count]
        print(f"Reference translation: \"{phrase_portuguese}\"")
        print("-" * 100)

        count += 1
