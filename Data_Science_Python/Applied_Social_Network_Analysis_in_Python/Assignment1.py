'''Assignment 1 - Creating and Manipulating Graphs
Eight employees at a small company were asked to choose 3 movies that they would most enjoy watching for the 
upcoming company movie night. These choices are stored in the file Employee_Movie_Choices.txt.

A second file, Employee_Relationships.txt, has data on the relationships between different coworkers.

The relationship score has value of -100 (Enemies) to +100 (Best Friends). A value of zero means the two 
employees haven't interacted or are indifferent.'''

import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite

# This is the set of employees
employees = set(['Pablo',
                 'Lee',
                 'Georgia',
                 'Vincent',
                 'Andy',
                 'Frida',
                 'Joan',
                 'Claude'])

# This is the set of movies
movies = set(['The Shawshank Redemption',
              'Forrest Gump',
              'The Matrix',
              'Anaconda',
              'The Social Network',
              'The Godfather',
              'Monty Python and the Holy Grail',
              'Snakes on a Plane',
              'Kung Fu Panda',
              'The Dark Knight',
              'Mean Girls'])

# you can use the following function to plot graphs
# make sure to comment it out before submitting to the autograder
def plot_graph(G, weight_name=None):
    '''
    G: a networkx G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    '''
    #%matplotlib notebook
    import matplotlib.pyplot as plt
    
    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    weights = None
    
    if weight_name:
        weights = [int(G[u][v][weight_name]) for u,v in edges]
        labels = nx.get_edge_attributes(G,weight_name)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw_networkx(G, pos, edges=edges, width=weights);
    else:
        nx.draw_networkx(G, pos, edges=edges);
    
    return

#-----------------------------------------------------------------------
'''Question 1
Using NetworkX, load in the bipartite graph from Employee_Movie_Choices.txt and return that graph.
This function should return a networkx graph with 19 nodes and 24 edges'''

#---------- ANSWER CODE ----------
def answer_one():

    return nx.read_edgelist('Employee_Movie_Choices.txt', delimiter="\t")

answer_one()

#plot_graph(answer_one(), weight_name=None)

#---------- ANSWER ----------
<networkx.classes.graph.Graph at 0x7f62dc72a700>

#-----------------------------------------------------------------------
'''Question 2
Using the graph from the previous question, add nodes attributes named 'type' where movies have the value 
'movie' and employees have the value 'employee' and return that graph.
This function should return a networkx graph with node attributes {'type': 'movie'} or {'type': 'employee'}'''

#---------- ANSWER CODE ----------
def answer_two():
    
    # Your Code Here
    G = answer_one()
    for node in G.nodes():
        if node in employees:
            G.add_node(node, type="employee")
        elif node in movies:
            G.add_node(node, type="movie")
    return G

answer_two()

#plot_graph(answer_two(), weight_name=None)

#---------- ANSWER ----------
<networkx.classes.graph.Graph at 0x7f62b9736760>

#-----------------------------------------------------------------------
'''Question 3
Find a weighted projection of the graph from answer_two which tells us how many movies different pairs of 
employees have in common.

This function should return a weighted projected graph.'''

#---------- ANSWER CODE ----------
def answer_three():
        
    B = answer_two()
    weighted_projection = bipartite.weighted_projected_graph(B, employees)
    
    return weighted_projection

answer_three()

#plot_graph(answer_three(), weight_name=None)

#---------- ANSWER ----------
<networkx.classes.graph.Graph at 0x7f62b974fb20>

#-----------------------------------------------------------------------
'''Question 4
Suppose you'd like to find out if people that have a high relationship score also like the same types of 
movies.
Find the Pearson correlation ( using DataFrame.corr() ) between employee relationship scores and the number 
of movies they have in common. If two employees have no movies in common it should be treated as a 0, not a 
missing value, and should be included in the correlation calculation.
This function should return a float.'''

#---------- ANSWER CODE ----------
def answer_four():
        
    Rel = nx.read_edgelist('Employee_Relationships.txt', data=[('relationship_score', int)])
    Rel_df = pd.DataFrame(Rel.edges(data=True), columns=['From', 'To', 'relationship_score'])
#     print (Rel_df)
    G = answer_three()
    G_df = pd.DataFrame(G.edges(data=True), columns=['From', 'To', 'movies_score'])
#     print (G_df)
    G_copy_df = G_df.copy()
#     change the edge direction and get a double direction graph
    G_copy_df.rename(columns={"From":"From_", "To":"From"}, inplace=True)
    G_copy_df.rename(columns={"From_":"To"}, inplace=True)
#     print (G_copy_df)
    G_final_df = pd.concat([G_df, G_copy_df])
#     print (G_final_df)
    final_df = pd.merge(G_final_df, Rel_df, on = ['From', 'To'], how='right')
    final_df['movies_score'] = final_df['movies_score'].map(lambda x: x['weight'] if type(x)==dict else None)
    final_df['relationship_score'] = final_df['relationship_score'].map(lambda x: x['relationship_score'])
    final_df['movies_score'].fillna(value=0, inplace=True)
#     print (final_df)

    return final_df['movies_score'].corr(final_df['relationship_score'])

answer_four()

#---------- ANSWER ----------
0.788396222173347

#-----------------------------------------------------------------------
import networkx as nx

G = nx.MultiGraph()
G.add_node('A',role='manager')
G.add_edge('A','B',relation = 'friend')
G.add_edge('A','C', relation = 'business partner')
G.add_edge('A','B', relation = 'classmate')
#G.node['A']['role'] = 'team member'
#G.node['B']['role'] = 'engineer'
G

plot_graph(G, weight_name=None)
#---------- ANSWER CODE ----------
<networkx.classes.multigraph.MultiGraph at 0x7f62b96e6760>

#-----------------------------------------------------------------------
B=nx.Graph()
B.add_edges_from([('A',1),('A',2),('A',3),('A',4),('A',5),('B',2),('C',3),('C',4),('C',5),('D',4),('E',5)])
X = set(['A','B','C','D','E'])
P = bipartite.projected_graph(B,X)
plot_graph(B, weight_name=None)

B=nx.Graph()
B.add_edges_from([('A',1),('A',2),('A',3),('A',4),('A',5),('B',2),('C',3),('C',4),('C',5),('D',4),('E',5)])
X=set(['A','B','C','D','E'])
P=bipartite.projected_graph(B,X)
plot_graph(P, weight_name=None)

B=nx.Graph()
B.add_edges_from([('A',1),('A',2),('A',3),('A',4),('A',5),('B',2),('C',3),('C',4),('C',5),('D',4),('E',5)])
X=set([1,2,3,4,5])
P=bipartite.projected_graph(B,X)
plot_graph(B, weight_name=None)

B=nx.Graph()
B.add_edges_from([('A',1),('A',2),('A',3),('A',4),('A',5),('B',2),('C',3),('C',4),('C',5),('D',4),('E',5)])
X=set([1,2,3,4,5])
P=bipartite.projected_graph(B,X)
plot_graph(P, weight_name=None)
#-----------------------------------------------------------------------