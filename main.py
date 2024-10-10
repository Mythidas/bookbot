def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path)
  print_report(book_path, book_text)  


def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def get_word_count(text):
  words = text.split()
  return len(words)

def char_sort(dict):
  return dict["count"]

def get_character_counts(text):
  char_dict = {}
  char_list = []

  for char_raw in text:
    char = char_raw.lower()
    if not char.isalpha():
      continue

    if char in char_dict:
      char_dict[char] = char_dict[char] + 1
    else:
      char_dict[char] = 1
  
  for key, val in char_dict.items():
    char_list.append({ "char": key, "count": val })

  char_list.sort(reverse=True, key=char_sort)
  return char_list

def print_report(path, text):
  word_count = get_word_count(text)
  char_counts = get_character_counts(text)

  print(f"--- Begin report of {path} ---")
  print (f"{word_count} words found in the document\n")

  for char_count in char_counts:
      print(f"The '{char_count["char"]}' character was found {char_count["count"]} times")

  print("--- End report ---")
  
main()