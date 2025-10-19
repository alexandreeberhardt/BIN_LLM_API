# Chat CLI with OpenAI API

This is a simple command-line interface (CLI) script that allows you to interact with OpenAI’s API directly from your terminal using natural language prompts.
It sends your input message to an OpenAI model (by default, `gpt-4o-mini`) and displays the formatted response in Markdown using the `rich` library.

## Installation

### 1. Create a virtual environment to use a clean python env to run the script

```bash
python3 -m venv ~/.venvs/chat
source ~/.venvs/chat/bin/activate
```

### 2. Install dependencies (openai for ChatGPT ans rich for Markdown display)

```bash
pip install --upgrade pip
pip install openai rich
```
## Configuration

1. **Update the Python shebang line** in the script with the correct path to your virtual environment:

   ```python
   #!/home/USER/.venvs/chat/bin/python
   ```

   Replace `USER` with your actual system username.

2. **Set your OpenAI API key:**
   Replace the placeholder in the script with your actual key:

   ```python
   client = OpenAI(api_key="YOUR_API_KEY")
   ```

   > You can get your API key and credits from [OpenAI’s Billing page](https://platform.openai.com/settings/organization/billing/overview).
## Move the script to a global location

```bash
sudo mv chat.py /usr/local/bin/chat
```

This lets you run the command simply by typing `chat` in your terminal.

## Usage

Once installed, you can use the command like this:

```bash
chat "Explain how to star a github repo"
```

The response will be displayed directly in your terminal with **Markdown formatting** for readability.

## Troubleshooting

**Command not found:**
  Make sure `/usr/local/bin` is in your `PATH`.

**Invalid API key:**
  Double-check your API key and ensure your OpenAI account has enough credits.

**Missing dependencies:**
  Reactivate your virtual environment and reinstall packages:

  ```bash
  source ~/.venvs/chat/bin/activate
  pip install XXX
  ```

## License

This project is open source and available under the MIT License.
