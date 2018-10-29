import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # record[0]: Person
    # record[1]: Friend
    mr.emit_intermediate(record[0], 1)


def reducer(key, list_of_values):
    # key: person
    # value: list of occurrence of friends
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
