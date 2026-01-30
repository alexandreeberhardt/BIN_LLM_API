# Chat CLI with OpenAI API

This is a simple command-line interface (CLI) script that allows you to interact with OpenAI's API directly from your terminal using natural language prompts.
It sends your input message to an OpenAI model (by default, `gpt-4o-mini`) and displays the formatted response in Markdown using the `rich` library.

<img width="976" height="632" alt="image" src="https://github.com/user-attachments/assets/44ccf34e-25ff-48de-bf94-959106d72f66" />

## Installation

### 1. Create a virtual environment

```bash
python3 -m venv ~/.venvs/chat
source ~/.venvs/chat/bin/activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install openai rich python-dotenv
```

## Configuration

1. **Update the Python shebang line** in the script with the correct path to your virtual environment:

   ```python
   # macOS
   #!/Users/USERNAME/.venvs/chat/bin/python

   # Linux
   #!/home/USERNAME/.venvs/chat/bin/python
   ```

   Replace `USERNAME` with your actual system username.

2. **Set your OpenAI API key:**
   Create a `.env` file in the same directory as the script:

   ```bash
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

   > You can get your API key from [OpenAI's API Keys page](https://platform.openai.com/api-keys).

## Make the script globally accessible

Create a symbolic link to make the command available system-wide (this preserves access to the `.env` file):

```bash
sudo ln -s $(pwd)/chat.py /usr/local/bin/chat
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
Check that your `.env` file exists and contains a valid `OPENAI_API_KEY`.

**Missing dependencies:**
Reactivate your virtual environment and reinstall packages:

```bash
source ~/.venvs/chat/bin/activate
pip install openai rich python-dotenv
```

## License

This project is open source and available under the MIT License.
