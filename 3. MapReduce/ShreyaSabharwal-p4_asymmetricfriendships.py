import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    persona = record[0]  # record[0]: Person
    friend = record[1]  # record[1]: Friend
    mr.emit_intermediate((persona, friend), 1)
    mr.emit_intermediate((friend, persona), 0)


def reducer(key, list_of_values):
    # key: personb
    # value: list of persona
    total = 0
    print(key, list_of_values)
    for val in list_of_values:
        total = total+val

    if total == 0:
        mr.emit((key))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
