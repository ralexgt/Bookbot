import os
from dotenv import load_dotenv

# checks if it's a txt
def is_txt(file_path):
  file_name = file_path.split("/")[-1]
  if '.' in file_name:
    if file_name.split(".")[1] == "txt":
      return True
  return False

# reads a .txt and returns the content of the file
def get_text_from_file(file_path):
  if not is_txt(file_path):
    raise Exception("not a txt file")
  with open(file_path) as file:
    return file.read()

# returns the file's name without the extension
def get_book_name(file_path):
  book_name = file_path.split("/")[-1]
  book_name = book_name.split(".")[0]
  return book_name

# counts how many words are in the text file
def count_words(text):
  words = text.split()
  return len(words)

# prases through each character in the text file and returns how many times each character appears
def count_characters(text):
  chars_dict = {}
  lowered_text = text.lower()
  for char in lowered_text:
    if char in chars_dict:
      chars_dict[char] += 1
    else:
      chars_dict[char] = 1
  return chars_dict

# defines the sort on number of appearances for list.sort()
def sort_on(dict):
  return dict["num"]
# takes the dictionary created from count_characters and orders the letters a-z in a list
def chars_dict_to_sorted_letters(chars_dict):
  sorted_list = []
  for char in chars_dict:
    if char.isalpha():
      sorted_list.append({"char": char, "num": chars_dict[char]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

# data gets a list [words_counter, char_counter] and generates a proper report to be printed in the console
def generate_report(book, data):
  print(f"\n############## Begin report of {book} ##############\n")
  print("### There are", data["words_count"], "words in the file\n")
  
  print("### Letters sorted by appearances: ")
  for letter in data["letters"]:
    print("The letter", "'" + letter["char"] + "'", "appears", letter["num"], "times")
  
  print("\n### All characters and the number of appearances (unordered)")
  for char in data["all_chars"]:
    if char != '\n':
      print("The character", "'" + char + "'", "appears", data["all_chars"][char], "times")
  print("\n############## End of report ##############")
    


def main():
  load_dotenv()
  
  file_path = os.getenv("FILE_PATH")
  text = ""
  try: 
    text = get_text_from_file(file_path)
  except Exception as e:
    print(e)
    return 1
  
  book_name = get_book_name(file_path)
  
  words_counter = count_words(text) 
  char_counter = count_characters(text)
  sorted_letters = chars_dict_to_sorted_letters(char_counter)
  
  # data dictionary to be passed to the report generation
  data = {
    "words_count": words_counter, # integer
    "all_chars": char_counter, # unordered dictionary
    "letters": sorted_letters, # list of dictionaries
    }
  
  generate_report(book_name, data)

main()