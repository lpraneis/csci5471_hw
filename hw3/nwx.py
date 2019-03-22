from hashlib import sha256
import networkx as nx

def hash16(x):
    m = sha256()
    m.update(b"prane001")
    # m.update(bytes(x, 'utf-8'))
    m.update(x)
    return m.digest()[-2:]


DG = nx.DiGraph()

inp = input('Enter beginning string, x: ')
inp_bytes = bytes(inp, 'utf-8')
DG.add_edges_from([(inp_bytes, hash16(inp_bytes))])

for i in range(0, 2**16):
    bts = (i).to_bytes(2, byteorder="little")
    DG.add_edges_from([(bts, hash16(bts))])
term_list = []
for node in DG.nodes():
    if DG.in_degree(node) == 0:
        term_list.append(node)

cyc_list =list(nx.simple_cycles(DG))
cyc_len_list = [len(i) for i in cyc_list]
max_cycle = max(cyc_len_list)
min_cycle = min(cyc_len_list)
avg_cycle = sum(cyc_len_list) / len(cyc_len_list)

print("max cycleLength: " , max_cycle)
print("avg cycleLength: " , avg_cycle )
print("min cycleLength: ", min_cycle)

flattened_cycles = []
for i in range(len(cyc_list)):
    for k in range(len(cyc_list[i])):
        flattened_cycles.append(cyc_list[i][k])
cyc_item_list = [i[0] for i in cyc_list]
terminal_paths = []
for node in term_list:
    for target in cyc_item_list:
        if nx.has_path(DG, node, target):
            tl = nx.shortest_simple_paths(DG, node, target)
            terminal_paths.append(list(tl))


tail_length_list = []
for i in terminal_paths:
    count = 0
    for val in i[0]:
        if val not in flattened_cycles:
            count+=1
    tail_length_list.append(count)
       
max_tail = max(tail_length_list)
avg_tail = sum(tail_length_list) / len(tail_length_list)

print("max tailLength: " , max_tail)
print("avg tailLength: " , avg_tail) 
print("components: ", len(cyc_list))
