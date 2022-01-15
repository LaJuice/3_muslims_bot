from quran.verses import Verses

vrs = Verses()

def nav_verse(id):
  try:
    return (vrs.get_verse(id).get("verses")[0].get('text_imlaei'))
  except IndexError:
    return "invalid verse ID"
print(nav_verse("1:1"))