import pyarabic.araby as arabic
import random
from ayat import *
 

def chapter_len(id):
  return vrs.get_chapter(id).get("verses")[-1].get("verse_key").split(":")[1]

def chapter_test(id):
  verse_id = random.randrange(1,int(chapter_len(id)) + 1)
  verse = nav_verse(f"{id}:{verse_id}")
  arabic.strip_diacritics(verse)
  verse = verse.split(" ")
  empty = random.randrange(len(verse))
  verse[empty] = ".." * len(verse[empty])
  return " ".join(verse), verse_id

name = "2:2"
print(name.split(":")[1])

