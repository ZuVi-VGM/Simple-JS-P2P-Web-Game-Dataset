import pandas as pd
import os

DICT_PATH = '/data/result'
RES_PATH = 'data/merged/res_merged.json'
RES_SHUFFLED = 'data/merged/res_shuffled.json'

word_dictionary = pd.DataFrame(columns = ['name', 'definition'])

for file in os.listdir(DICT_PATH):
  file_path = os.path.join(DICT_PATH, file)
  print(file_path)
  if os.path.isdir(file_path):
    continue

  data = pd.read_json(file_path)
  word_dictionary = pd.concat([word_dictionary, data], ignore_index = True)
  print(f'DONE {file_path}')

word_dictionary.drop_duplicates(subset=['name'], keep='first', inplace=True)
word_dictionary.sort_values(by='name', inplace=True)
word_dictionary.to_json(RES_PATH, orient='records')
print(len(word_dictionary))
word_dictionary_shuffled = word_dictionary.sample(frac=1).reset_index(drop=True)
word_dictionary_shuffled.to_json(RES_SHUFFLED, orient='records')
print(len(word_dictionary))
