import openai

class GPTHandler:
    def __init__(self) -> None:
        self.model = "gpt-3.5-turbo"
        self.messages = [
            {
                "role": "user",
                "content": "I tried to translate the phrase \"I like turtles\" to the Portuguese phrase \"eu gostar tartaruga\". With this, list all my errors and give me the correct translation.",
            },
            
        ]

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
            "role": "assistant",
            "content": content
        })
        return content
