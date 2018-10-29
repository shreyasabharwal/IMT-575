import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]  # FileName
    value = record[1]  # Text
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)


def reducer(key, fileNames):
    # key: word
    # value: File Name
    list_fnames = []
    for file in fileNames:
        if file not in list_fnames:
            list_fnames.append(file)
    mr.emit((key, list_fnames))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
