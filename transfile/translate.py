import os
import json
import argparse

from openai import OpenAI

from transfile.constants import SUPPORTED_FORMATS
from transfile.helpers import clean_translate_content
from transfile.parsers import dict_to_properties
from transfile.io import read_json_file, read_properties_file


# Instantiate the OpenAI client using the API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_file_extension(file_path):
  """Extract the file extension from a given file path."""
  _, ext = os.path.splitext(file_path)
  return ext[1:]

def extract_language_from_filename(filename):
  """Extract the language code from the filename (e.g., 'en' from 'en.json')."""
  return os.path.splitext(os.path.basename(filename))[0]

def validate_file_extensions(input_file, output_files):
  # Check input file extension
  input_ext = get_file_extension(input_file)
  if input_ext not in SUPPORTED_FORMATS:
    print(f"Error: The input file '{input_file}' has an unsupported extension '.{input_ext}'. Supported formats are: {SUPPORTED_FORMATS}")
    return False
  
  # Check each output file extension
  for output_file in output_files:
    output_ext = get_file_extension(output_file)
    if output_ext not in SUPPORTED_FORMATS:
      print(f"Error: The output file '{output_file}' has an unsupported extension '.{output_ext}'. Supported formats are: {SUPPORTED_FORMATS}")
      return False

  return True

def translate_content(content, source_lang, target_lang):
  """Translates content using the OpenAI API from source_lang to target_lang."""
  text_to_translate = json.dumps(content)
  
  prompt = (
    f"You are a translation assistant. Translate from {source_lang} to {target_lang}. "
    "The output should be in UTF-8 format."
  )
  
  messages = [
    {"role": "system", "content": prompt},
    {"role": "user", "content": text_to_translate}
  ]

  try:
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=messages,
    )
    translated_text = response.choices[0].message.content.strip()
    print(json.loads(clean_translate_content(translated_text)))
    return json.loads(clean_translate_content(translated_text))

  except Exception as e:
    print(f"An error occurred while translating to {target_lang}: {e}")
    return None

def translate_file(input_file, output_files):
  """Translates the input file into multiple target languages and saves to respective output files."""
  if not validate_file_extensions(input_file, output_files):
    return

  source_lang = extract_language_from_filename(input_file)
  source_lang_ext = get_file_extension(input_file)

  if source_lang_ext == 'json':
    content = read_json_file(input_file)
  elif source_lang_ext == 'properties':
    content = read_properties_file(input_file)
  else:
    raise ValueError(f"Unsupported format: {source_lang}")

  # Translate and save to each target file
  for target_file in output_files:
    target_lang = extract_language_from_filename(target_file)
    target_lang_ext = get_file_extension(target_file)
    print(f"Translating '{input_file}' to '{target_file}' ...")

    translated_content = translate_content(content, source_lang, target_lang)

    if translated_content:
      if target_lang_ext == 'json':
        with open(target_file, 'w', encoding='utf-8') as f:
          json.dump(translated_content, f, indent=2, ensure_ascii=False)
      elif target_lang_ext == 'properties':
        with open(target_file, 'w', encoding='utf-8') as f:
          f.write(dict_to_properties(translated_content))
      else:
        raise ValueError(f"Unsupported format: {format}")
      print(f"Successfully saved translated content to {target_file}")
    else:
      print(f"Failed to translate {input_file} to {target_file}.")

def main():
  parser = argparse.ArgumentParser(description="Translate a JSON file into multiple languages using OpenAI API")
  parser.add_argument("-s", "--source", type=str, required=True, help="Path to the input JSON file (source file)")
  parser.add_argument("-t", "--targets", type=str, nargs='+', required=True, help="Paths to the output JSON files (target files)")

  args = parser.parse_args()
  translate_file(args.source, args.targets)

if __name__ == "__main__":
  main()
