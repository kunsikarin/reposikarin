import numpy as np
import pandas as pd
from pandas.io.parsers import read_csv

vertices = []
vertices_no = 0
graph = []

def add_vertex(v):
  global graph
  global vertices_no
  global vertices
  if v in vertices:
    print("Vertex ", v, " already exists")
  else:
    vertices_no = vertices_no + 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
    temp = []
    for i in range(vertices_no):
        temp.append(0)
    graph.append(temp)

def add_edge(v1, v2, e): 
    global graph
    global vertices_no
    global vertices
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

def print_graph():
  global graph
  global vertices_no
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] == 0:
          if i!=j:
            print(vertices[i], " -> ", vertices[j], \
        " edge weight: ", graph[i][j])

def cal(i):
  for j in range (x):
      u=i-1
      qi = np.array(q[u])  
      qj = np.array(q[j]) 
      out_arr = np.subtract(qj, qi)
      pi = np.array(p[u])
      out=np.multiply(pi, out_arr)
      outfinal=np.sum(out)
      add_edge(i,j+1,outfinal)

def check_cycle():
    global graph
    global vertices_no
    global vertices
    visited1=[]
    visited2=[]
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] == 0:
                if i!=j:
                    visited1.append(i+1)
                    visited2.append(j+1)
    for i in range (len(visited1)):
        for j in range (i,len(visited2)):
            if visited1[i]==visited2[j]: 
                return True     
            else:
                pass     
        return False

#Choose file
#df = read_csv('rand_true.csv')
df = read_csv('rand_false.csv')

p = df.iloc[0:,1:5].values
q = df.iloc[0:,5:9].values

x=len(q)

for i in range (x):
    add_vertex(i+1)
for i in range (x):
    cal(i+1)
print_graph()

print("Internal representation: ", graph)
check_cycle()
print("Is it cycle with weight 0:"+str(check_cycle()))