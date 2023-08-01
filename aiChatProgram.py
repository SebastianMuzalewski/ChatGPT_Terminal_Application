import openai
import time

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
# openai.api_key = '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'


def get_gpt_answer(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use other engines as well
        prompt=prompt,
        max_tokens=150,  # You can adjust this value based on your needs
        temperature=0.5,  # You can adjust this value to control the creativity of the response
    )
    time.sleep(2)
    return response.choices[0].text.strip()


def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Exiting...")
            break
        prompt = f"You asked: {user_input}\nChatGPT: "
        answer = get_gpt_answer(prompt)
        print("ChatGPT:", answer)


if __name__ == "__main__":
    print("ChatGPT is ready to answer your questions! Type 'exit', 'quit', or 'bye' to end the conversation.")
    main()
