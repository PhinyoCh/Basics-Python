def count_char(word):
  lword = ''.join(e for e in word.lower() if e.isalnum())
  d={}
  for c in lword:
    d[c] = d.get(c,0) + 1 
  return d
