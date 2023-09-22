def read_file():
    with open("books/frankenstein.txt") as f:
      return f.read()
def count_characters():
   text = read_file()
   text = text.lower()
   dic = {}
   for char in text:
      if char in dic:
        dic[char] += 1
      else:
         dic[char] = 1
   del dic[" "]
   print("--- Begin report of books/frankenstein.txt ---")
   print(f"{len(text)} words found in the document \n")
   dic = dict(sorted(dic.items(), key = lambda x : x[1], reverse=True))
   for key in dic:
      print(f"The {key} character was found {dic.get(key)} times")
   print("--- End report ---")
def main():
   count_characters()
main()