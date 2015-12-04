import networkx as nx


def generate_graph(words):
    from string import ascii_lowercase as lowercase
    G = nx.Graph(name="words")
    lookup = dict((c,lowercase.index(c)) for c in lowercase)
    from itertools import permutations
    def reorder_word(word):
        perms = [''.join(p) for p in permutations(word)]
        for i in range(len(perms)):
            yield perms[i]
    def edit_distance_one(word):
        for i in range(len(word)):
            left, c, right = word[0:i], word[i], word[i+1:]
            j = lookup[c] # lowercase.index(c)
            for cc in lowercase[j+1:]:
                yield left + cc + right
    candgen = ((word, cand) for word in sorted(words) 
               for reorder in reorder_word(word)
               for cand in edit_distance_one(reorder) if cand in words)
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G

g5 = nx.Graph()
fh = open("words_dat.txt", 'r')
words=set()
for line in fh.readlines():
    line = line.decode()
    if line.startswith('*'):
        continue
    w=str(line[0:5])
    words.add(w)
g5 = generate_graph(words)

for (source,target) in [('chaos','order'),
                        ('nodes','graph'),
                        ('moron','smart'),
                        ('pound','marks')]:
    print("Shortest path between %s and %s is"%(source,target))
    try:
        sp=nx.shortest_path(g5, source, target)
        for n in sp:
            print(n)
    except nx.NetworkXNoPath:
        print("None")
g4 = nx.Graph()
fh = open("words4.dat", 'r')
words=set()
for line in fh.readlines():
    line = line.decode()
    if line.startswith('*'):
        continue
    w=str(line[0:4])
    words.add(w)
g4 = generate_graph(words)

for (source,target) in [('cold','warm'),
                        ('love','hate'),]:
    print("Shortest path between %s and %s is"%(source,target))
    try:
        sp=nx.shortest_path(g4, source, target)
        for n in sp:
            print(n)
    except nx.NetworkXNoPath:
        print("None")