import openai

from domain.chatgpt.constants import GPT_MODEL, ROLE_SYSTEM, ROLE_USER, API_KEY_PATH

class GPTHandler:
    def __init__(self) -> None:
        self.model = GPT_MODEL
        self.system_message = {
            "role": ROLE_SYSTEM,
            "content": "you are a system that corrects grammatical errors in a translation. "
            "you list out and explain each and every one of the errors in a given translation. "
            "the inputs are the sentence to be translated and the user's translation, which "
            "should be corrected. do not list out anything that wasn't wrong in the translated "
            "sentence. if the translation is gramattically correct, only respond with \'correct\'. "
            "For example:\n"
            "user: sentence to be translated: \"What kind of music do you like?\""
            "user's translation: \"Que tipo de música você gosta?\"\n"
            "assistant: The translation is correct."
            "user: sentence to be translated: \"eu gosto de vacas\""
            "user's translation: \"me like cow\""
            "assistant: The user's translation, \"me like cow,\" contains a few errors:\n"
            "1. Incorrect Subject Pronoun: \"Me\" is an object pronoun and can't be used as"
            "the subject of a sentence. The correct subject pronoun to use in this case is \"I.\""
            "Correction: \"I like cow\"\n"
            "2. Singular vs. Plural: In the original sentence, \"vacas\" is plural, meaning more than"
            "one cow. In English, we need to reflect this by using the plural form \"cows.\""
            "Correction: \"I like cows\"\n"
            "So, the correct translation of \"eu gosto de vacas\" is \"I like cows.\""
        }

        openai.api_key_path = API_KEY_PATH
    
    def correct_translation(self, phrase, translation):
        user_translation = {
            "role": ROLE_USER,
            "content": f"sentence to be translated: {phrase}"
            f"user's translation: {translation}",
        }

        messages_to_send = [self.system_message, user_translation]
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages_to_send
        )
        content = response['choices'][0]['message']['content']
        return content
