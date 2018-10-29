import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # key: table name
    # value: document contents
    predicate = record[1]  # OrderId
    mr.emit_intermediate(predicate, record[:])


def reducer(key, list_of_values):
    # key: OrderId
    # value: List Of Attributes
    order, lineItem = [], []
    for record in list_of_values:
        if record[0] == 'order':
            order.append(record[:])
        elif record[0] == 'line_item':
            lineItem.append(record[:])

    for o in order:
        for l in lineItem:
            mr.emit((o, l))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
