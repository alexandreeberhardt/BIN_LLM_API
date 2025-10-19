#!/home/USER/.venvs/chat/bin/python
import sys
from openai import OpenAI
from rich.markdown import Markdown
from rich.console import Console

client = OpenAI(api_key="YOUR_API_KEY") # You need to buy credits at https://platform.openai.com/settings/organization/billing/overview


if len(sys.argv) < 2:
    print("Usage: chat <message>")
    sys.exit(1)

question = " ".join(sys.argv[1:])

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": question}
    ]
)

content = response.choices[0].message.content
Console.print(Markdown(content))
