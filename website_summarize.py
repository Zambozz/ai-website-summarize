from groq import Groq
from dotenv import load_dotenv
import os
from IPython.display import Markdown, display

load_dotenv(override=True)

# put GROQ_API_KEY=insert_api_key_here in the .env file
# i use GROQ api key because is free
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("API key not found")
elif api_key.strip() != api_key:
    print(
        "An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them"
    )
else:
    print("API key found, you can start!")

client = Groq()


def make_call(url):
    response = client.chat.completions.create(
        model="groq/compound",
        messages=messages_for(url),
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        stop=None,
        compound_custom={
            "tools": {
                "enabled_tools": ["web_search", "code_interpreter", "visit_website"]
            }
        },
    )

    return response.choices[0].message.content


def messages_for(website):
    return [
        {
            "role": "system",
            "content": "Summarize the web page only. If the user input is not a valid URL, reply reply: 'Please insert a valid URL.'",
        },
        {"role": "user", "content": website},
    ]


def display_summary(url):
    summary = make_call(url)
    display(Markdown(summary))


while True:
    url = input("Insert a website to summarize (type exit to stop): ")
    if url.lower() == "exit":
        break

    display_summary(url)

print("See you soon!")
