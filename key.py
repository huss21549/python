import keyword

def print_python_keywords():
  """
  Prints all reserved keywords in Python.
  """
  print("Python keywords are:")
  for kw in sorted(keyword.kwlist):
    print(f"- {kw}")

if __name__ == "__main__":
  print_python_keywords()