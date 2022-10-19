class Edge:
	
	def __init__(self):
		self.src = 0
		self.dest = 0
		self.weight = 0

class Graph:
	
	def __init__(self):
		
		self.V = 0
		self.E = 0

		self.edge = None

def createGraph(V, E):

	graph = Graph()
	graph.V = V;
	graph.E = E;
	graph.edge =[Edge() for i in range(graph.E)]
	return graph;

def isNegCycleBellmanFord(graph, src):

	V = graph.V;
	E = graph.E;
	dist = [1000000 for i in range(V)];
	dist[src] = 0;

	for i in range(1, V):
		for j in range(E):
		
			u = graph.edge[j].src;
			v = graph.edge[j].dest;
			weight = graph.edge[j].weight;
			if (dist[u] != 1000000 and dist[u] + weight < dist[v]):
				dist[v] = dist[u] + weight;

	for i in range(E):
	
		u = graph.edge[i].src;
		v = graph.edge[i].dest;
		weight = graph.edge[i].weight;
		if (dist[u] != 1000000 and dist[u] + weight < dist[v]):
			return True;

	return False;

if __name__=='__main__':
	
	V = 5; 
	E = 8; 
	graph = createGraph(V, E);

	graph.edge[0].src = 0;
	graph.edge[0].dest = 1;
	graph.edge[0].weight = -1;

	graph.edge[1].src = 0;
	graph.edge[1].dest = 2;
	graph.edge[1].weight = 4;

	graph.edge[2].src = 1;
	graph.edge[2].dest = 2;
	graph.edge[2].weight = 3;

	graph.edge[3].src = 1;
	graph.edge[3].dest = 3;
	graph.edge[3].weight = 2;

	graph.edge[4].src = 1;
	graph.edge[4].dest = 4;
	graph.edge[4].weight = 2;

	graph.edge[5].src = 3;
	graph.edge[5].dest = 2;
	graph.edge[5].weight = 5;

	graph.edge[6].src = 3;
	graph.edge[6].dest = 1;
	graph.edge[6].weight = 1;

	graph.edge[7].src = 4;
	graph.edge[7].dest = 3;
	graph.edge[7].weight = -3;

	if (isNegCycleBellmanFord(graph, 0)):
		print("Yes")
	else:
		print("No")
