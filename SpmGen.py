import sys


def open_csv_file(file_path):
    spm_dicts = []
    for line in open(file_path):
        cells = line.split(",")
        if len(cells) > 4:
            spm_dicts.append(cells)
    return spm_dicts


def output_nodes(spm_dicts, index):
    nodes = []
    for cells in spm_dicts:
        if not nodes.__contains__(cells[index]):
            nodes.append(cells[index])
    return nodes


args = sys.argv
if len(args) > 1:
    print "open file " + args[1]
    dicts = open_csv_file(args[1])
    if len(dicts) > 0:
        node_b = output_nodes(dicts, 1)
        print node_b
    else:
        print "no spm information, please check you file"
else:
    print "please input a file"
