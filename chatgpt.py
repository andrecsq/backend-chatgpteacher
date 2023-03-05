import openai

class GPTHandler:
    def __init__(self) -> None:
        self.model = "gpt-3.5-turbo"
        self.messages = []

    def generate_messages(conversation):
        messages = []
        for tuple in conversation:
            messages.append({
                "role": tuple[0],
                "content": tuple[1],
            })
        return messages
    
    def chat(self, input):
        self.messages.append({
            "role": "user",
            "content": input,
        })
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        content = response['choices'][0]['message']['content']
        self.messages.append({
            "role": "system",
            "content": content
        })
        return content
