def clean_translate_content(input_string):
  """Remove triple backticks from the start and end of the input string."""
  input_string = input_string.strip()
  if input_string.startswith("```") and input_string.endswith("```"):
    lines = input_string.splitlines()
    content_lines = lines[1:-1]
    clean_content = "\n".join(content_lines).strip()
    return clean_content
  else:
    return input_string
