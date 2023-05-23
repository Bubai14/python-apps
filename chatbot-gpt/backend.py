import openai


class Chatbot:

    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,  # Max number of character the chat gpt can return the response
            temperature=0.5  # Less temperature means greater accuracy but less diverse responses
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    print(chatbot.get_response("How will be my day today?"))