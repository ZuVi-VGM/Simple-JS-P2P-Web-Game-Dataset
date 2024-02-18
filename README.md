
# Simple-JS-P2P-Web-Game-Dataset

This repository contains the dataset for the [ZuVi-VGM/Simple-JS-P2P-Web-Game](https://github.com/ZuVi-VGM/Simple-JS-P2P-Web-Game) original project,  the python scripts used to generate it and the initial dataset, taken from [scalaWords](https://github.com/pazqo/scalaWords).

<p>
<img src="https://img.shields.io/badge/Status-Released-blue" /> <a href="https://opensource.org/license/gpl-3-0/" target="_blank"><img src="https://img.shields.io/badge/License-GPL%20v3-yellow.svg" /></a>
<a href="https://creativecommons.org/licenses/by/4.0/" target="_blank"><img src="https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg" /></a>
</p>

## Tech Stack

Python, Pandas, JSON.

## Roadmap

I started by searching a list of Italian words, which I easily found on the [scalaWords](https://github.com/pazqo/scalaWords) Git repository. 

At this point, I found a Python library called [PyMultiDictionary](https://github.com/ppizarror/PyMultiDictionary) that allows multilingual retrieval of word definitions from various dictionaries. <br>Since I was interested in having a single concise definition, I thought of a way to extract the first definition provided using a regex, noticing the specific pattern usage in the response generation. 

At this point, I generated my dictionaries using a backup system, as execution times proved quite long, and I needed to establish checkpoints.

The last step was merging the results and generating a unique dataset without possible duplicates. I also generated a shuffled version because it can be useful for my purposes.

## Appendix

The resulting datasets are located in the directory *"[data/merged](https://github.com/ZuVi-VGM/Simple-JS-P2P-Web-Game-Dataset/tree/main/data/merged)"* and are as follows:
- [res_merged.json](https://github.com/ZuVi-VGM/Simple-JS-P2P-Web-Game-Dataset/blob/main/data/merged/res_merged.json) - dataset in alphabetical order.
- [res_shuffled.json](https://github.com/ZuVi-VGM/Simple-JS-P2P-Web-Game-Dataset/blob/main/data/merged/res_shuffled.json) - dataset in random order.

The initial dictionary is contained in the file:
- [data/dictionary_ita](https://github.com/ZuVi-VGM/Simple-JS-P2P-Web-Game-Dataset/blob/main/data/dictionary_ita.txt)

The scripts in the main folder are used, respectively:
- [create_dictionary.py](https://github.com/ZuVi-VGM/Simple-JS-P2P-Web-Game-Dataset/blob/main/create_dictionary.py) - create the dictionary with words and definitions.
- [merge.py](https://github.com/ZuVi-VGM/Simple-JS-P2P-Web-Game-Dataset/blob/main/merge.py) - merge the results into a unique json file and generate a shuffled copy.

The compressed intermediate results are contained in the directory *[data/result](https://github.com/ZuVi-VGM/Simple-JS-P2P-Web-Game-Dataset/tree/main/data/result)*
## Greetings

- [@pazqo](https://github.com/pazqo) for the original [scalaWords](https://github.com/pazqo/scalaWords) list.
- [@pazqo](https://github.com/pazqo) for the [PyMultiDictionary](https://github.com/ppizarror/PyMultiDictionary) libary.

## License
The result dataset of this project is licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/) and all the scripts used to generate this dataset are licensed under the [GPL v3](https://opensource.org/license/gpl-3-0/) license.

## Authors

- [@ZuVi-VGM](https://www.github.com/ZuVi-VGM)


