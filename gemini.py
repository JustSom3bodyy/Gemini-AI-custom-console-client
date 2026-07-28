#!/usr/bin/env python3

# if you don't know what packages to install or how they are named, read README paragraph 1.1

import os
import sys
import argparse

from dotenv import load_dotenv

from google import genai
from google.genai import types

from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live

load_dotenv()

API_KEY = os.getenv("API_KEY")
# If you don't know how to use this, read README (paragraph 2.1 for API key; 2.2 for os/dotenv usage)


# === config ===


MODEL="gemini-3.6-flash"
# check README paragraph 3.1 for more models

SYSTEM_INSTRUCTION=""
# check README paragraph 4.1 for more system instructions presets

CONFIG = types.GenerateContentConfig(
    temperature=0.2,
    top_p=0.95,
    top_k=40,
    max_output_tokens=8192,
    system_instruction=SYSTEM_INSTRUCTION,
    safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        )
    ]
)
# if you don't know how to use these parameters, check README paragraph 4


# === main code ===


console = Console()

def init_client():
    if not API_KEY:
        console.print(f"[bold red]ERROR:[/bold red] API key not found. Check if [bold].env[/bold] file still exists, is in the same directory as the main file and contains API key.")
        sys.exit(1)
    return genai.Client(api_key=API_KEY)

def single_query(client, prompt):
    try:
        console.print(f"[bold blue]AI:[/bold blue] ") # feel free to change any colors

        response = client.models.generate_content_stream(
            model=MODEL,
            contents=prompt,
            config=CONFIG
        )

        full_text = ""
        with Live(console=console, refresh_per_second=10) as live:
            for chunk in response:
                if chunk.text:
                    full_text += chunk.text
                    live.update(Markdown(full_text))

    except Exception as e:
        console.print(f"[bold red]GENERATION ERROR:[/bold red] {e}")

def chat_mode(client):
    console.print(f"[bold blue]Selected model: {MODEL}.[/bold blue] Enter [bold]exit[/bold] or press Ctrl+C to exit.\n")

    chat = client.chats.create(model=MODEL, config=CONFIG)

    while True:
        try:
            console.print("\n[bold red]User:[/bold red] ", end="")
            user_input = input()

            if user_input.strip().lower() in ['exit', 'quit']:
                break
            if not user_input.strip():
                continue

            console.print(f"[bold blue]AI:[/bold blue] ")

            response = chat.send_message_stream(user_input)

            full_text = ""
            with Live(console=console, refresh_per_second=10) as live:
                for chunk in response:
                    if chunk.text:
                        full_text += chunk.text
                        live.update(Markdown(full_text))

        except (KeyboardInterrupt, EOFError):
            console.print(f"\n[yellow]Выход.[/yellow]")
            break
        except Exception as e:
            console.print(f"\n[bold red]Ошибка:[/bold red] {e}")


def main():
    parser = argparse.ArgumentParser(description="Gemini AI custom console client")
    parser.add_argument("prompt", nargs="*", help="prompt. text, yep...")
    args = parser.parse_args()

    client = init_client()

    if args.prompt:
        single_query(client, " ".join(args.prompt))
    else:
        chat_mode(client)

if __name__ == "__main__":
    main()
