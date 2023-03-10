from gpthandler import GPTHandler

handler = GPTHandler()

while (True):
    user_input = input(">> ")
    response = handler.chat(user_input)
    print(response.strip())
