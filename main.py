from openai import OpenAI
from openai.types.responses.response_output_message import ResponseOutputMessage
from openai.types.responses.response_output_text import ResponseOutputText
from dotenv import load_dotenv
import os

load_dotenv()


OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

client = OpenAI(api_key=OPEN_AI_KEY)


def generate_x_post(usr_input: str) -> str:
    prompt = f"""
    You are an expert social media manager, you excel at crafting viral and highly engaging posts for X (formerly Twitter)

    Your task is to generate a post that is concise, impactful, and tailored to the topic provided but the user, avoid using hashtags and lots of emojis (a few emojis are ok, but not too many ).

    Keep the post shot and focused, structure it in a clean, readable way, using line breaks and empty 

    Here is the tipic procided by the user: 

    <topic>
    {usr_input}
    </topic>
    """
    response = client.responses.create(
        model="gpt-4.1-nano",
        input="Write a one-sentence bedtime story about a unicorn.",
    )
    output_item = response.output[0]
    if isinstance(output_item, ResponseOutputMessage) and output_item.content:
        content_item = output_item.content[0]
        if isinstance(content_item, ResponseOutputText):
            return content_item.text
    raise ValueError("Unexpected response output type")


def main():
    print("Hello from ai-agents-and-workflows!")

    usr_input = input("What should the post be about?")
    x_post = generate_x_post(usr_input)
    print(x_post)


print("Generated X post")


if __name__ == "__main__":
    main()
