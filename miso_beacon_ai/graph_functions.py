"""This functions provides tools for working with graphs"""

import heapq
import functools


def getadjacencymatrix(vertices):
    """This function returns the adjacency matrix of a graph given its vertices and edges"""
    # Initialize matrix
    matrix = []
    for i in range(len(vertices)):
        rowlist = []
        for j in range(len(vertices)):
            rowlist.append(0)
        matrix.append(rowlist)

    # Each Vertex object has a list of Edges object, which are the ones connected to it,
    # and every of those Edge object has a list of connected Vertex.

    # For every vertex in the graph...
    for i, graphvertex in enumerate(vertices):
        # ...check in its edges...
        for edge in graphvertex.geteges():
            # ...the set of vertices of every of those edges...
            for edgevertex in edge.getvertices():
                # ...and check if every vertex is equal to this edge's vertex.
                for j, graphvertex2 in enumerate(vertices):
                    if graphvertex == graphvertex2:
                        matrix[i][j] += 1

    return matrix


def convexhullgrahamscan(vertices):
    """This function returns the set of vertices which are the convex hull of a given set"""
    # Get the vertex with the lowest value of y coordinate and, if more than one is found, the lowest x valued
    vertex_p = None
    for vertex in vertices:
        if vertex_p is None:
            vertex_p = vertex
        else:
            if vertex.getposition().gety() == vertex_p.getposition().gety():
                if vertex.getposition().getx() < vertex_p.getposition().getx():
                    vertex_p = vertex
            elif vertex.getposition().gety() < vertex_p.getposition().gety():
                vertex_p = vertex

    # Vertex are ordered by the angle between vertex_p and x axis segment and vertex_p and each vertex segment
    # As the vertex are confined in the first quadrant, instead of the angle can be calculated any monotonic function
    # on [0, PI], like cos or the segments slope
    x_p = vertex_p.getposition().getx()
    y_p = vertex_p.getposition().gety()
    verticesslopes = []
    for vertex in vertices:
        slope = vertex.getposition().gety() - y_p / vertex.getposition().getx() - x_p
        verticesslopes.append((slope, vertex))

    # Heapsort ordering method is used
    # Make list into a heap
    heapq.heapify(verticesslopes)
    # Elements come off the heap in ascending order
    verticesslopesordered = []
    for i in range(len(verticesslopes)):
        verticesslopesordered.append(heapq.heappop(verticesslopes))
    # Python's "sorted" could be used instead

    # Then, using the sorted set of points, is verified that the last two points evaluated are a "turn right" or
    # "clock-wise" turn, and if it happens the middle point is popped out of the set; if so, the new pair of last points
    # are evaluated again. The process continues with every new point until the vertex_p is reached.
    # The turn is evaluated using the z component of cross product (x2 − x1)(y3 − y1) − (y2 − y1)(x3 − x1) <? 0r >? 1 .
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)
    def compare(a, b):
        return (a > b) - (a < b)

    def evaluateturn(v1, v2, v3):
        return compare((v2[1].getposition().getx() - v1[1].getposition().getx()) *
                       (v3[1].getposition().gety() - v1[1].getposition().gety()) -
                       (v2[1].getposition().gety() - v1[1].getposition().gety()) *
                       (v3[1].getposition().getx() - v1[1].getposition().getx()), 0)

    def keep_left(hull, r):
        while len(hull) > 1 and evaluateturn(hull[-2], hull[-1], r) == TURN_RIGHT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    l = functools.reduce(keep_left, verticesslopesordered, [])
    u = functools.reduce(keep_left, reversed(verticesslopesordered), [])

    # Vertex objects are saved
    convexhulltuples = l.extend(u[i] for i in range(1, len(u) - 1)) or l
    convexhull = []
    for tup in convexhulltuples:
        convexhull.append(tup[1])

    # And comparing both set, the hull vertex are popped out and so discarded ones are saved
    discardedvertices = list(vertices)
    for hullvertex in convexhull:
        hv_x = hullvertex.getposition().getx()
        hv_y = hullvertex.getposition().gety()
        for vertex in vertices:
            v_x = vertex.getposition().getx()
            v_y = vertex.getposition().gety()
            if v_x == hv_x and v_y == hv_y:
                discardedvertices.remove(vertex)

    return convexhull, vertices, discardedvertices
