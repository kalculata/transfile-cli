# Transfile CLI

Transfile CLI is a command-line tool that allows you to translate JSON files using the OpenAI API. You can translate text from one language to multiple target languages in a straightforward manner.

## Features

- Translate JSON files containing text from one language to multiple target languages.
- Utilizes OpenAI's powerful translation capabilities.

## Requirements

- Python 3.7 or higher
- An OpenAI API key

## Installation

1. **Clone the repository** (or download the source code):

```bash
git clone https://github.com/kalculata/transfile-cli.git
cd transfile-cli
```

2. Install the package:

First, build the package:

```bash
python setup.py sdist bdist_wheel
```

Then, install it:

```bash
pip install .
```

3. Set up your OpenAI API Key:

Before using the script, set your OpenAI API key as an environment variable. You can do this in your terminal with the following command:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Replace "your-api-key-here" with your actual OpenAI API key.

## Usage

To use the transfile command-line tool, follow these steps:

1. Prepare your input JSON file. The filename should indicate the source language code (e.g., en.json for English).

2. Run the translation command:

```bash
transfile -s path/to/input.json -t path/to/output1.json path/to/output2.json
```

* `-s` or `--source`: Path to the input JSON file (the source file).
* `-t` or `--targets`: One or more paths to the output JSON files (the target files). Each filename should reflect the target language code (e.g., `fr.json` for French).

## Example

For example, if you have a file named `en.json` containing the following:

```json
{
  "greeting": "Hello",
  "farewell": "Goodbye"
}
```

You can translate it to French and Spanish using:

```bash
transfile -s en.json -t fr.json es.json
```

This will create fr.json and es.json containing the translations.

## Troubleshooting

- Ensure that you have the correct Python version installed (3.7 or higher).
- Verify that your OpenAI API key is correctly set in your environment variables.
- If you encounter any module errors, make sure that your package is installed correctly and that you are in the correct virtual environment (if using one).