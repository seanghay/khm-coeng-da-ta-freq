import os
import regex as re
import csv
from khnormal import khnormal
from khmernormalizer import normalize

_coeng_da_pattern = re.compile(r"([\u1780-\u17a2])\u17d2ដ")
_coeng_ta_pattern = re.compile(r"([\u1780-\u17a2])\u17d2ត")

_coeng_da_words = {}
_coeng_ta_words = {}

with open("khmerdictionary.csv") as infile:
  reader = csv.DictReader(infile)
  for item in reader:
    text = item["word"].replace("\u200b", "")

    coeng_da_result = [m[1] for m in _coeng_da_pattern.finditer(text)]
    if len(coeng_da_result) > 0:
      for ch in coeng_da_result:
        if ch in _coeng_da_words:
          _coeng_da_words[ch].append(text)
        else:
          _coeng_da_words[ch] = [text]

    coeng_ta_result = [m[1] for m in _coeng_ta_pattern.finditer(text)]
    if len(coeng_ta_result) > 0:
      for ch in coeng_ta_result:
        if ch in _coeng_ta_words:
          _coeng_ta_words[ch].append(text)
        else:
          _coeng_ta_words[ch] = [text]

os.makedirs("result", exist_ok=True)

for k, v in _coeng_da_words.items():
  filename = f"KHDICT2022_COENG_DA_{k}.tsv"
  with open(os.path.join("result", filename), "w") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerows([[w, "・".join(w)] for w in v])

for k, v in _coeng_ta_words.items():
  filename = f"KHDICT2022_COENG_TA_{k}.tsv"
  with open(os.path.join("result", filename), "w") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerows([[w, "・".join(w)] for w in v])


# ---
_coeng_da_words = {}
_coeng_ta_words = {}

with open("khmerlbdict.tsv") as infile:
  reader = csv.reader(infile)
  words = list(set([item[0].strip() for item in reader if len(item) > 0]))

  for text in words:
    coeng_da_result = [m[1] for m in _coeng_da_pattern.finditer(text)]
    if len(coeng_da_result) > 0:
      for ch in coeng_da_result:
        if ch in _coeng_da_words:
          _coeng_da_words[ch].append(text)
        else:
          _coeng_da_words[ch] = [text]

    coeng_ta_result = [m[1] for m in _coeng_ta_pattern.finditer(text)]
    if len(coeng_ta_result) > 0:
      for ch in coeng_ta_result:
        if ch in _coeng_ta_words:
          _coeng_ta_words[ch].append(text)
        else:
          _coeng_ta_words[ch] = [text]

os.makedirs("result", exist_ok=True)

for k, v in _coeng_da_words.items():
  filename = f"KHLBDICT_COENG_DA_{k}.tsv"
  with open(os.path.join("result", filename), "w") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerows([[w, "・".join(w)] for w in v])

for k, v in _coeng_ta_words.items():
  filename = f"KHLBDICT_COENG_TA_{k}.tsv"
  with open(os.path.join("result", filename), "w") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerows([[w, "・".join(w)] for w in v])
