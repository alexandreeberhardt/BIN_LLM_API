#!/Users/alexandre/.venvs/chat/bin/python
import sys
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from rich.markdown import Markdown
from rich.console import Console

# Charger le .env depuis le dossier du script (résout le lien symbolique)
load_dotenv(Path(__file__).resolve().parent / ".env")

client = OpenAI()  # Lit automatiquement OPENAI_API_KEY


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
console = Console()
console.print(Markdown(content))
