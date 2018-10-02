# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 13:35:41 2018

@author: Kunal Taneja
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:24:18 2018
e

@author: Kunal Taneja
"""
import sys
import re
import ast

from decimal import Decimal

class_list = dict()

            
def vertex_collection():
    k=1
    m=1
    l=list(class_list.values())
    vertices=list()
    graph_vertices=list()
    graph_edges=list()
    graph_edgeset=set()
    graph_set=set()
    vertex_list=dict()
    dict_vertex=list()
    vertices_intersection=list()
    y=list()
    #last_element=list()
    no_streets=len(l)
    vertices=[None]*no_streets
    #last_element=[None]*no_streets
    for o in range (0,no_streets):
        y=[i.split(', ', 1)[0] for i in l[o]]
        vertices[o]=y
    for i in range(0,no_streets):
        #print "hi"
        for j in range (i+1,no_streets):
             w=len(vertices[i])
             #print "hi"
             v=len(vertices[j])
             while k<w:
                 while m<v:
                      pair1=vertices[i][k-1]
                      pair2=vertices[i][k]
                      pair3=vertices[j][m-1]
                      pair4=vertices[j][m]
                      x1,y1 = ast.literal_eval(pair1)
                      x2,y2 = ast.literal_eval(pair2)
                      x3,y3 = ast.literal_eval(pair3)
                      x4,y4 = ast.literal_eval(pair4)
                      x1=float(x1)
                      x2=float(x2)
                      x3=float(x3)
                      x4=float(x4)
                      y1=float(y1)
                      y2=float(y2)
                      y3=float(y3)
                      y4=float(y4)
                      A1 = y2-y1
                      B1 = x1-x2
                      C1 = A1*(x1) + B1*(y1) 
                      
                      A2 = y4-y3
                      B2 = x3-x4
                      C2 = A2*(x3)+ B2*(y3) 
                      determinant = A1*B2 - A2*B1
                      min_x1=min(x1,x2)
                      min_x2=min(x3,x4)
                      max_x1=max(x1,x2)
                      max_x2=max(x3,x4)
                      min_y1=min(y1,y2)
                      min_y2=min(y3,y4)
                      max_y1=max(y1,y2)
                      max_y2=max(y3,y4)
                      flag1=False
                      flag2=False
                      
                      pair1="(" + str(x1) + "," +str(y1) + ")"
                      pair2="(" + str(x2) + "," +str(y2) + ")"
                      pair3="(" + str(x3) + "," +str(y3) + ")"
                      pair4="(" + str(x4) + "," +str(y4) + ")"
                      thislist = list((pair1,pair2,pair3,pair4))
                     # print thislist
                       
                      
                      if (determinant != 0): 
                           X = Decimal((B2*C1 - B1*C2)/determinant)
                           X = round(X,2)
                           Y = Decimal((A1*C2 - A2*C1)/determinant)
                           Y = round(Y,2)
                          # print "X= " + str(X)
                           #print "Y= " + str(Y)
                           #print "min_x1= " + str(min_x1)
                           #print "max_x1= " + str(max_x1)
                           #print "min_y1= " + str(min_y1)
                          # print "max_y1= " + str(max_y1)
                          # print "min_x2= " + str(min_x2)
                           #print "max_x2= " + str(max_x2)
                           #print "min_y2= " + str(min_y2)
                           #print "max_y2= " + str(max_y2)
                           if (bool(X<=max_x1) & bool(X>=min_x1)):
                               #print ("im true for x1")
                               if (bool(Y<=max_y1) & bool(Y>=min_y1)):
                                     #print ("hi im true for both x1,y1")
                                     flag1=True
                               if (bool(X<=max_x2) & bool(X>=min_x2)):
                                     #print ("im true for x2")
                                     if (bool(Y<=max_y2) & bool(Y>=min_y2)):
                                    # print ("hi im true for both x2,y2")
                                        flag2=True
                           if(flag1==True & flag2==True):
                                   #print "you got me right"
                                   new_vertex="(" + str(X) + "," +str(Y) + ")"
                                   graph_vertices.extend(thislist)
                                   dict_vertex.append(new_vertex)
                                   vertices_intersection.append(thislist)
                                   intersection_points=new_vertex
                                   graph_vertices.append(new_vertex)
                                   graph_set=set(graph_vertices)
                                   graph_vertices1=list(graph_set)
                                   for z in range(0,len(graph_vertices1)):
                                       vertex_list[z+1]=graph_vertices1[z]
                                
                                  
                                   
                           else:
                                   pass
      
                     
                     
                     
                      m=m+1
                 k=k+1
                 m=1
             k=1
     
    print "V = {"
    for x,y in vertex_list.items():
        print x,": ",y 
    print "}"

    
    for t in range(0, len(dict_vertex)):
        intersection_pt=dict_vertex[t]
        vertexlist=vertices_intersection[t]
        [pair1, pair2, pair3, pair4]=vertexlist
        for g in vertex_list:
            
            if intersection_pt == vertex_list[g]:
                edge_intersection=g
        for s,e in vertex_list.items():
            if e==pair1:
                edge_pair1=s
                #print "comparing pair 1" + e
                #print s
        for s,e in vertex_list.items():
            if e==pair2:
                edge_pair2=s
                #print s
                #print "comparing pair 2" + e
        for s,e in vertex_list.items():
                 if e==pair3:
                     edge_pair3=s
                 #    print s
                  #   print "comparing pair 3" +e                                            
        for s,e in vertex_list.items():
                if e==pair4:
                    edge_pair4=s
                   # print "comparing pair 4" + e
                    #print s
                    #print edge_intersection
                   # print intersection_points
                    edge1="<"+str(edge_intersection) + "," + str(edge_pair1) + ">"
                    #print edge1
                    edge2="<"+str(edge_intersection) + "," + str(edge_pair2) + ">"
                    #print edge2
                    edge3="<"+str(edge_intersection) + "," + str(edge_pair3) + ">"
                    #print edge3
                    edge4="<"+str(edge_intersection) + "," + str(edge_pair4) + ">"
                    #print edge4
                                
                                
                    edgelist = list((edge1,edge2,edge3,edge4))
                    graph_edges.extend(edgelist)
                    graph_edgeset=set(graph_edges)
                    graph_edges=list(graph_edgeset)
                    distinct=list()
                    for n in range(0,len(graph_edges)):
                        pair=graph_edges[n]
                        pair=re.sub('<','(',pair)
                        pair=re.sub('>',')',pair)
                        v1,w1 = ast.literal_eval(pair)
                        distinct.append(v1)
                        distinct_set=set(distinct)
                        distinct=list(distinct_set)
                    for n1 in range(1,len(distinct)):
                        edge_betweeen="<"+str(distinct[n1-1]) + "," + str(distinct[n1]) + ">"
                        graph_edges.append(edge_betweeen)
                        graph_set=set(graph_edges)
                        graph_edges=list(graph_set)                        
                    
    print "E ={"
    for u in graph_edges:
        print u
    print "}"
        
    
   


    
    
    
    

    
def main():
    while True:
        command=raw_input()
        if(command ==''):
            break
        elif(command[0]=='r'):
            y=re.split(' +"|"|',command)
        else:
            y=re.split('" +| +"',command)
        if(len(y)==1):
            choice=y[0]
        elif(len(y)==2):
            choice=y[0]
            street=y[1]
            street=street.lower()   
        elif(len(y)==3):
            choice=y[0]
            street=y[1]
            street=street.lower()
            location=y[2]
        else:
            sys.stdout.write("Error: " + "Wrong selection of command")
            continue
        if choice == 'a':
            location=re.sub(' +','',location)
            location=re.sub('\)\(',') ( ',location)
            location=re.sub('\( ','(',location)
            location=location.split(' ')
            class_list[street] = location
            #database()
        elif choice == 'c':
           location=re.sub(' +','',location)
           location=re.sub('\)\(',') ( ',location)
           location=re.sub('\( ','(',location)
           location=location.split(' ')        
           class_list[street] = location
            #database()
        elif choice == 'r':
            try:
                del class_list[street]
            except KeyError:
                sys.stderr.write("Error: " + street + " not available to delete")
            #database()
        elif choice == 'g':
            vertex_collection()
          
        else:
            print 'Error: ' + 'Wrong choice try again'

if __name__ == '__main__':
    main()