import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    seq_id = record[0]  # record[0]: SeqId
    nucleotide = record[1]  # record[1]: Nucleotide
    mr.emit_intermediate(nucleotide[:-10], seq_id)


def reducer(key, list_of_values):
    # key: sequence id
    # value: list of nucleotides
    mr.emit((key))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
