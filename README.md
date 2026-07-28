# Gemini-AI-custom-console-client


A fast, lightweight, terminal-based AI client for Google Gemini built with Python. It supports real-time streaming, rich markdown formatting, continuous interactive chat, and single-shot queries directly from your command line.

---

## Table of Contents
1. [Installation & Requirements](#1-installation--requirements)
   - [1.1 Required Packages](#11-required-packages)
2. [API Key Configuration](#2-api-key-configuration)
   - [2.1 Obtaining an API Key](#21-obtaining-an-api-key)
   - [2.2 Setting Up the Environment File (.env)](#22-setting-up-the-environment-file-env)
3. [Models](#3-models)
   - [3.1 Available Gemini Models](#31-available-gemini-models)
4. [Configuration Parameters & System Instructions](#4-configuration-parameters--system-instructions)
   - [4.1 System Instruction Presets](#41-system-instruction-presets)
   - [4.2 Parameter Reference](#42-parameter-reference)
5. [How to Use](#5-how-to-use)
   - [Interactive Chat Mode](#interactive-chat-mode)
   - [Single Query Mode](#single-query-mode)

---

## 1. Installation & Requirements

### 1.1 Required Packages

Make sure you have **Python 3.10 or higher** installed.

Open your terminal or command prompt and install the required dependencies using `pip`:

```bash
pip install google-genai python-dotenv rich
```

#### Package Breakdown:
* **`google-genai`**: Google's official, updated SDK for Gemini models.
* **`python-dotenv`**: Reads secret keys from a local `.env` file.
* **`rich`**: Formats text nicely in your terminal (renders Markdown, live typing effects, colors).

---

## 2. API Key Configuration

### 2.1 Obtaining an API Key
1. Go to **[Google AI Studio](https://aistudio.google.com/)**.
2. Sign in with your Google Account.
3. Click **"Get API key"** and create a key in a new or existing project.
4. Copy the key to your clipboard.

---

### 2.2 Setting Up the Environment File (`.env`)

To prevent putting your secret API key directly inside your source code, the script uses a `.env` file.

1. In the **same folder** where `gemini.py` is saved, create a file named `.env` (note the leading dot).
2. Open `.env` in a text editor and add your key like this:

```env
API_KEY=your_actual_api_key_here
```

> **Note:** Do not put quotes around the key unless your key contains spaces. Make sure there are no spaces around the `=` sign.

---

## 3. Models

### 3.1 Available Gemini Models

You can change the `MODEL` variable at the top of `gemini.py`:

```python
MODEL = "gemini-2.5-flash"
```

Here are recommended model options you can use:

**`gemini-3.6-flash`**- - a newest, frontier-level intelligemt model optimized for real-world tasks at a higher speed and lower cost. Designed for the agentic era, it excels at code generation, agentic execution, and spatial reasoning. This model is particularly effective for rapid agentic loops involving complex coding cycles and iterations.
**`gemini-3.5-flash`** - frontier-level intelligent model optimized for real-world tasks at a higher speed and lower cost. Designed for the agentic era, it excels at sub-agent deployment, multi-step workflows, and long-horizon tasks at scale. This model is particularly effective for rapid agentic loops involving complex coding cycles and iterations.
**`gemini-3.5-flash-lite`** - a low-latency, cost-effective multimodal model optimized for high-throughput, low-cost execution for subagent tasks and document parsing. The model supports text, image, video, audio, and PDF inputs, and is designed for high-volume agentic workflows, simple data extraction, and applications where latency and API cost are the primary constraints.

---

## 4. Configuration Parameters & System Instructions

### 4.1 System Instruction Presets

System instructions set the persona, behavior, or strict rules for how the AI responds.

Change `SYSTEM_INSTRUCTION = ""` in `gemini.py` to any of these presets:

####  Python Developer Assistant
```python
SYSTEM_INSTRUCTION = "You are an expert Python developer. Provide clean, well-commented, production-ready code with explanations."
```

####  Translator & Proofreader
```python
SYSTEM_INSTRUCTION = "You are a professional translator. Translate all user input into clear, natural English. Fix grammar and style if the input is already in English."
```

####  Concise Answer Bot
```python
SYSTEM_INSTRUCTION = "Be extremely concise. Answer questions directly without intro, filler, or wrapping fluff. Max 3 sentences unless asked for details."
```

---

### 4.2 Parameter Reference

Inside `gemini.py`, the `CONFIG` object controls generation settings:

```python
CONFIG = types.GenerateContentConfig(
    temperature=0.2,
    top_p=0.95,
    top_k=40,
    max_output_tokens=8192,
    ...
)
```

* **`temperature` (0.0 to 2.0)**: 
  * Lower values (`0.0 - 0.3`) = Logical, precise, consistent (great for code, math, factual queries).
  * Higher values (`0.7 - 1.2`) = Creative, varied, surprising (great for story writing, brainstorming).
* **`top_p` (0.0 to 1.0)**: Nucleus sampling. Controls token diversity based on cumulative probability.
* **`top_k` (integer)**: Limits token selection to top *K* choices.
* **`max_output_tokens`**: Maximum length of the generated response.
* **`safety_settings`**: Configured to `BLOCK_NONE` by default in this script to prevent output truncation when discussing complex topics.

---

## 5. How to Use

### Interactive Chat Mode
Run the script without arguments to start a ongoing conversation loop:

```bash
python gemini.py
```

* Type your message and press **Enter**.
* Answers stream in real-time rendered with Markdown syntax highlighting.
* To leave chat mode, type `exit` or `quit`, or press `Ctrl + C`.

---

### Single Query Mode
Pass your query directly as command-line arguments for quick execution:

```bash
python gemini.py "How do I reverse a string in Python?"
```

```bash
python gemini.py What is the distance between Earth and Mars?
```

The script will process your question, stream the formatted answer, and immediately return to your command prompt.
