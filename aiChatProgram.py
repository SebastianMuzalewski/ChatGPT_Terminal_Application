# Networking Project
import openai


# Set personal API key
personal_key = ""
openai.api_key = personal_key


# Prompt user to ask chat anything. Type exit to end session.
def user_input():
    print("ChatGPT: Enter prompt! (Type 'exit' to end the conversation)")
    v_input = input("You: ")
    return v_input


# Sends user input to the chat api and retrieves a response.
def chatgpt_execute(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages={
            "role": "user",
            "content": prompt
        },
    )
    return response['content']


# Main block where everything is called.
def main():
    # Return user_input into a variable to be used.
    prompt = user_input()
    if prompt.lower() == "exit":
        print("ChatGPT: Thank you for using ChatGPT. Have a great day!")
        exit()

    # Run the chatgpt_execute to send the user_input as a prompt and create the answer from chat.
    response = chatgpt_execute(prompt)

    # Print results
    print("ChatGPT:", response)


if __name__ == "__main__":
    main()
