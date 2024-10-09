import argparse
import json
import os
from openai import OpenAI

# Instantiate the OpenAI client using the API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_language_from_filename(filename):
  """Extract the language code from the filename (e.g., 'en' from 'en.json')."""
  return os.path.splitext(os.path.basename(filename))[0]

def translate_content(content, source_lang, target_lang):
  """Translates content using the OpenAI API from source_lang to target_lang."""
  text_to_translate = json.dumps(content)
  messages = [
    {
      "role": "system",
      "content": (
        f"You are a translation assistant. Translate from {source_lang} to {target_lang}. "
        "The output should be in UTF-8 format."
      )
    },
    {"role": "user", "content": text_to_translate}
  ]

  try:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages,
    )
    translated_text = response.choices[0].message.content.strip()
    return json.loads(translated_text)

  except Exception as e:
    print(f"An error occurred while translating to {target_lang}: {e}")
    return None

def translate_file(input_file, output_files):
    """Translates the input JSON file into multiple target languages and saves to respective output files."""
    source_lang = extract_language_from_filename(input_file)

    # Open and read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
      content = json.load(f)

    # Translate and save to each target file
    for target_file in output_files:
      # Extract the target language from the filename (e.g., 'en' from 'en.json')
      target_lang = extract_language_from_filename(target_file)
      print(f"Translating {input_file} to {target_file} ...")
      
      translated_content = translate_content(content, source_lang, target_lang)

      if translated_content:
        # Save the translated content to the output file
        with open(target_file, 'w', encoding='utf-8') as f:
          json.dump(translated_content, f, indent=2, ensure_ascii=False)
        print(f"Successfully saved translated content to {target_file}")
      else:
        print(f"Failed to translate {input_file} to {target_lang}.")
def main():
  parser = argparse.ArgumentParser(description="Translate a JSON file into multiple languages using OpenAI API")
  parser.add_argument("-s", "--source", type=str, required=True, help="Path to the input JSON file (source file)")
  parser.add_argument("-t", "--targets", type=str, nargs='+', required=True, help="Paths to the output JSON files (target files)")

  args = parser.parse_args()

  # Translate the input file to the target languages inferred from the filenames
  translate_file(args.source, args.targets)

if __name__ == "__main__":
  main()
