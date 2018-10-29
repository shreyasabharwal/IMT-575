import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    matrix = record[0]  # record[0]: matrix name
    i = record[1]  # record[1]: row
    j = record[2]  # record[2]: column
    nrows, ncols = 5, 5
    if matrix == 'a':
        for col in range(ncols):
            c_coord = (i, col)
            mr.emit_intermediate((c_coord), record)
    else:
        for row in range(nrows):
            c_coord = (row, j)
            mr.emit_intermediate((c_coord), record)


def reducer(key, list_of_values):
    # key: coordinates of result(c) matrix
    # value: list of values of rows/columns
    # print(key, list_of_values)
    dict_a, dict_b = {}, {}

    for record in list_of_values:
        i = record[1]
        j = record[2]
        val = record[3]

        if record[0] == 'a':
            if key[0] == i and j not in dict_a:
                dict_a[j] = val
        else:
            if key[1] == j and i not in dict_b:
                dict_b[i] = val

    sum = 0
    for r, rval in dict_a.items():
        for c, cval in dict_b.items():
            if r == c:
                sum = sum + (rval*cval)
    mr.emit((key[0], key[1], sum))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
