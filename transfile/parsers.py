def dict_to_properties(content):
  """Convert a dictionary to a .properties formatted string."""
  return "\n".join(f"{key}={value}" for key, value in content.items())

