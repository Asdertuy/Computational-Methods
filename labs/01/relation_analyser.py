import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X, is a loop for each Vertex
    2. Symmetric: aRb implies bRa for all a,b in X The arrows 
    joining a pair of different vertices allways appear in a pair with opposite arrow directions
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X, 
    If A is related to B and B is related to C then A is related to C
    """

    Reflexive = False
    Symmetric = False
    Transitive = False

    #The idea is that all will return true if there is a loop at each vertex then it will return true#
    Reflexive = all((a, a) in val for a in set(x[0] for x in val))  # Check if (a, a) is present for all 'a'

    #This one makes sure 
    Symmetric = all((b, a) in val for (a, b) in val) and all((a, b) in val for (b, a) in val)
    # Check if for every (a, b), (b, a) exists as well
    
    Transitive = all((a, c) in val for (a, b) in val for (x, c) in val if x == b)
    # Check if for every (a, b) and (b, c), (a, c) exists

    return Reflexive,Symmetric,Transitive

def plot(val):
    g = graphviz.Digraph('G', filename='relation_graph.gv')

    # Add edges based on the provided relations in 'val'
    for relation in val:
        g.edge(str(relation[0]), str(relation[1]))

    g.attr('node', shape='circle')  # Set node shape (optional)
    g.attr('edge', arrowhead='vee')  # Set arrowhead style (optional)

    g.render(view=True) 

def main():
    print("Hello World analyzing input!")
    val = R = [(0, 0), (0, 1), (0, 3), (1, 0), (1, 1), (2, 2), (3, 0), (3, 3)]
    print(val)
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot()

if __name__ == "__main__":
    main()
