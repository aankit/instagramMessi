import networkx as nx
import pickle

g = nx.Graph()
dataFile = open('combined.pk1', 'rb')
data = pickle.load(dataFile)

def graph_add_node(n, identity):
    if g.has_node(n):
        g.node[n]['weight']+=1
    else:
        g.add_node(n)
        g.node[n]['weight']=1
        g.node[n]['label'] = n
        g.node[n]['identity'] = identity
            
def graph_add_edge(n1, n2):
    if g.has_edge(n1, n2):
        g[n1][n2]['weight']+=1
    else:
        g.add_edge(n1,n2)
        g[n1][n2]['weight']=1

for screenName, info in data.items():
    messiCounter = info['tags'].count('leomessi')
    cristianoCounter = info['tags'].count('cristiano')
    identity = ''
    if messiCounter>0 and cristianoCounter>0:
        identity='both'
    elif cristianoCounter==0 and messiCounter>0:
        identity='messi'
    elif messiCounter==0 and cristianoCounter>0:
        identity='cristiano' 
    graph_add_node(screenName, identity)

for screenName, info in data.items():
    for liker in info['likes']:
        graph_add_node(liker,'like')
        graph_add_edge(screenName,liker)

print g.number_of_nodes()
print g.number_of_edges()

nx.write_gexf(g, 'messi_ronaldo.gexf')
print 'messi_ronaldo.gexf'