#!pip install PyMultiDictionary
from PyMultiDictionary import MultiDictionary
import re
import pandas as pd

DICT_FILE = 'data/dictionary_ita.txt'
RES_PATH = 'data/res/res_'

dictionary = MultiDictionary()
word_dictionary = pd.DataFrame(columns = ['name', 'definition'])
data_len = 0;

with open(DICT_FILE, 'r') as file:
  for i, line in enumerate(file, 1):
    if i < 252287:
      continue

    line = line.strip()
    if len(line) <= 2:
      continue

    # pattern regex per estrarre la prima definizione
    pattern = rf"La(?:\s*prima)?\s*definizione\s*di\s*(.*?)\s*nel\s*dizionario\s*è\s*(.*?)(?:\s*Altra|\s\1|$)"

    try:
      match = re.search(pattern, dictionary.meaning('it', line)[1], re.IGNORECASE)
    except Exception as e:
      print(f"{i} - {line}: {e}")

    # Se c'è una corrispondenza, inserisce il testo in un dataset
    if match:
      definition = match.group(2).capitalize()
      row_to_add = pd.Series([line, definition], index=word_dictionary.columns)
      word_dictionary = pd.concat([word_dictionary, row_to_add.to_frame().T], ignore_index=True)

    # Backup dati analizzati ogni 10000
    if i%10000 == 0:
        data_len += len(word_dictionary)
        print(f"Added {len(word_dictionary)} entries, current len={data_len}")
        word_dictionary.to_json(RES_PATH + f"{i}.json", orient='records')
        word_dictionary = pd.DataFrame(columns = ['name', 'definition'])

print(len(word_dictionary))
word_dictionary.to_json(RES_PATH + 'end.json', orient='records')