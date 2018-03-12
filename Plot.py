
import plotly.plotly as py
from plotly.graph_objs import *
# import plotly
import csv
import networkx as nx
import matplotlib.pyplot as plt

# plotly.tools.set_credentials_file(username='44576947', api_key='GXt7SSTLJTpqpMA3Exrc')


# namelist=['stokley-c','schwieger-j','delainey-d']

class Plot():

    # def getRandomCo(self,namelist):


    def draw(self,dictionary):


        G = nx.Graph()
        threshold = 5
        for (n1,n2) in dictionary.keys():
            if dictionary[(n1,n2)] >= threshold and n1 != n2:
                G.add_edge(n1,n2)
        nx.draw(G)
        plt.draw()
        plt.savefig('foo.png')
        print("Network density:", G.number_of_nodes())
        self.printDegreeCentralityTable(nx.degree_centrality(G))
        self.printBetweenCentralityTable(nx.betweenness_centrality(G))
        self.printClosenessCentralityTable(nx.closeness_centrality(G))
        self.printEigenCentralityTable(nx.eigenvector_centrality(G))
        # print(nx.degree_centrality(G))

        return G.to_undirected()

    def addNode(self,node,G):
        if node in G.nodes:
            return
        else:
            G.add_node(node)


    def printDegreeCentralityTable(self,degree_centrality):
        with open('degree_centrality.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in degree_centrality.items():
                writer.writerow([key, value])

    def printBetweenCentralityTable(self, between_centrality):
        with open('between_centrality.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in between_centrality.items():
                writer.writerow([key, value])

    def printClosenessCentralityTable(self, closeness_centrality):
        with open('closeness_centrality.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in closeness_centrality.items():
                writer.writerow([key, value])

    def printEigenCentralityTable(self, eigen_centrality):
        with open('eigen_centrality.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in eigen_centrality.items():
                writer.writerow([key, value])
#
#     def getNodePostion(self):
#         # G = self.injectData()
#         G = nx.random_geometric_graph(200,0.015)
#         pos = nx.get_node_attributes(G, 'pos')
#
#         print(pos)
#
#         dmin = 1
#         ncenter = 0
#         for n in pos:
#             x, y = pos[n]
#             d = (x - 0.5) ** 2 + (y - 0.5) ** 2
#             if d < dmin:
#                 ncenter = n
#                 dmin = d
#
#         p = nx.single_source_shortest_path_length(G, ncenter)
#         edge_trace = Scatter(
#             x=[],
#             y=[],
#             line=Line(width=0.5, color='#888'),
#             hoverinfo='none',
#             mode='lines')
#
#         for edge in G.edges():
#             x0, y0 = G.node[edge[0]]['pos']
#             x1, y1 = G.node[edge[1]]['pos']
#             edge_trace['x'] += [x0, x1, None]
#             edge_trace['y'] += [y0, y1, None]
#
#         node_trace = Scatter(
#             x=[],
#             y=[],
#             text=[],
#             mode='markers',
#             hoverinfo='text',
#             marker=Marker(
#                 showscale=True,
#                 # colorscale options
#                 # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
#                 # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
#                 colorscale='YIGnBu',
#                 reversescale=True,
#                 color=[],
#                 size=10,
#                 colorbar=dict(
#                     thickness=15,
#                     title='Node Connections',
#                     xanchor='left',
#                     titleside='right'
#                 ),
#                 line=dict(width=2)))
#
#         for node in G.nodes():
#             x, y = G.node[node]['pos']
#             node_trace['x'].append(x)
#             node_trace['y'].append(y)
#
#         for node, adjacencies in enumerate(G.adjacency_list()):
#             node_trace['marker']['color'].append(len(adjacencies))
#             node_info = '# of connections: ' + str(len(adjacencies))
#             node_trace['text'].append(node_info)
#
#         fig = Figure(data=Data([edge_trace, node_trace]),
#                      layout=Layout(
#                          title='<br>Network graph made with Python',
#                          titlefont=dict(size=16),
#                          showlegend=False,
#                          hovermode='closest',
#                          margin=dict(b=20, l=5, r=5, t=40),
#                          annotations=[dict(
#                              text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
#                              showarrow=False,
#                              xref="paper", yref="paper",
#                              x=0.005, y=-0.002)],
#                          xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
#                          yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))
#
#         py.image.save_as(fig, filename="new.png")
#
#
# # plot.getNodePostion()