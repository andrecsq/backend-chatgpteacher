import json
import pandas as pd

from domain.chatgpt.gpthandler import GPTHandler

from constants import PHRASES_FILEPATH, QUIT_COMMANDS, GPT4_TAG

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

def print_big(message, title = None):
    if title:
        print(title)
    print("-----------------------------------")
    print(message)
    print("-----------------------------------")


if __name__ == '__main__':
    count = 0
    num_correct = 0
    while (True):
        phrase_portuguese = df_phrases['phrase_portuguese'][count]
        print(f"Translate \"{phrase_portuguese}\" from Portuguese to English")
        user_translation = input(">> ")

        if user_translation.lower() in QUIT_COMMANDS:
            handle_exit(count, num_correct)
            break

        if "--" in user_translation:
            argument = user_translation.split("--")[-1].strip()
            print(f"Argument: {argument}")
            if argument == GPT4_TAG:
                handler.set_model_to_gpt4()
                print("Changed handler model to GPT4")
            
            user_translation = user_translation.split("--")[0].strip()            


        correction = handler.correct_translation(phrase_portuguese, user_translation)
        try:
            correction_dict = json.loads(correction.strip())
            print("Valid JSON first try")
            print_big(correction, "This IS a valid JSON")
        except Exception as e:
            print("Trying to convert using ChatGPT")
            correction_processed = handler.convert_to_json(correction)
            try:
                correction_dict = json.loads(correction_processed.strip())
                print("Conversion successful")
            except:
                print("Wasn't able to convert")

        if "errors" in correction_dict and len(correction_dict["errors"]) == 0:
            print_big("CORRECT!!!")
            num_correct += 1
        else:
            print_big("WRONG!!!")

        print(json.dumps(correction_dict, indent=2))

        phrase_english = df_phrases['phrase_english'][count]
        print(f"Reference translation: \"{phrase_english}\"")
        print("-" * 100)

        count += 1
