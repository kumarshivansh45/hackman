import networkx as nx
import osmnx as ox
from IPython.display import IFrame
import sys

ox.config(log_console=True, use_cache=True)

G = ox.graph_from_place('karnataka, India', network_type='drive')

# use networkx to calculate the shortest path between two nodes
origin_node = list(G.nodes())[0]
destination_node = list(G.nodes())[-1]
route = nx.shortest_path(G, [12.906525577185116, 77.5653220601236], [12.955230325317402, 77.57406378296383])
print(route)
# plot the route with folium
# route_map = ox.plot_route_folium(G, route)

# # save as html file then display map as an iframe
# filepath = './route.html'
# route_map.save(filepath)
# IFrame(filepath, width=600, height=500)
