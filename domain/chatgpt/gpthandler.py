import openai
import json

from domain.chatgpt.constants \
    import Models, Roles, API_KEY_PATH, INITIAL_PROMPTS

class GPTHandler:
    def __init__(self) -> None:
        self.set_model_to_gpt3()
        self.initial_prompts = INITIAL_PROMPTS
        openai.api_key_path = API_KEY_PATH

    def set_model_to_gpt3(self) -> None:
        self.model = Models.GPT3.value

    def set_model_to_gpt4(self) -> None:
        self.model = Models.GPT4.value

    def get_formatted_user_input(self, phrase, translation):
        formatted_user_input = "correct this translation:"
        formatted_user_input +=  "{\n"
        formatted_user_input += f"\t\"original\": \"{phrase}\",\n"
        formatted_user_input += f"\t\"translation\": \"{translation}\"\n"
        formatted_user_input += "}"
        formatted_user_input += "R:"

        return formatted_user_input
    
    def convert_to_json(self, message_to_convert):
        message = "convert this to a proper JSON. do not output anything other than the JSON. ```"
        message += message_to_convert
        message += "```"
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": Roles.USER.value,
                    "content": message
                }
            ]
        )

        content = response['choices'][0]['message']['content']
        return content

    
    def correct_translation(self, phrase, translation):
        user_translation = {
            "role": Roles.USER.value,
            "content": self.get_formatted_user_input(phrase, translation),
        }

        messages_to_send = self.initial_prompts + [user_translation]
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages_to_send
        )

        content = response['choices'][0]['message']['content']
        content = content.strip()
        
        return content
