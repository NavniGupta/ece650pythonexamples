#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  27 13:37:27 2018

@author: navnigupta
"""

import sys
import re


main_list = dict()
#function for checking street name is in valid format or not
def check_street(streetName):
    if all(a.isalpha() or a.isspace() for a in streetName ):
        return True
    else:
        return False
#function for checking if street to be changesd exits or not
def can_change(streetName):

    
        if streetName in main_list:
            return True
        else:

            return False
#function for checking parenthesis in input
def check_parenthesis(GPSlocation):
    s = []
    equal = True
    index = 0
    while index < len(GPSlocation) and equal:
        token = GPSlocation[index]
        if token == "(":
            s.append(token)
        elif token == ")":
            if len(s) == 0:
                equal = False
            else:
                s.pop()

        index += 1

    return equal and len(s) == 0

#function for checking valid format of coordinates
def is_vertex_valid(GPSlocation):
    regex = r'\(-?\d+,-?\d+\)'
    preg = re.compile(regex)
    result= preg.match(GPSlocation)
    return result   
   
#function for spiliting coordinate to get value of 'x' and 'y'    
def split_pair(pair):
    v1=re.split('\(|\)',pair)
    v1,w1=re.split(',',str(v1[1]))
    return v1,w1

#function for adding a street
def add_street(GPSlocation,streetName):
    
    
        if(check_parenthesis(GPSlocation)):
            GPSlocation1=re.sub(' +','',GPSlocation)
            GPSlocation1=re.sub('\)\(',') ( ',GPSlocation1)
            GPSlocation1=re.sub('\( ','(',GPSlocation1)
            GPSlocation1=GPSlocation1.split(' ')
            if all(is_vertex_valid(i) for i in GPSlocation1):
                 main_list[streetName] = GPSlocation1
            else:
                print "enter vertices in a valid format."
        else:
             print "unbalanced parenthesis"
    
#function for changing a street        
def change_street(GPSlocation,streetName):

        if(check_parenthesis(GPSlocation)):
            GPSlocation1=re.sub(' +','',GPSlocation)
            GPSlocation1=re.sub('\)\(',') ( ',GPSlocation1)
            GPSlocation1=re.sub('\( ','(',GPSlocation1)
            GPSlocation1=GPSlocation1.split(' ')
            if all(is_vertex_valid(i) for i in GPSlocation1):
                 main_list[streetName] = GPSlocation1
            else:
                print "enter vertices in a valid format."
        else:
             print "unbalanced parenthesis"

 #function for removing a street          
def remove_street(streetName):
      try:
                del main_list[streetName]
      except KeyError:
                sys.stderr.write("Error: " + streetName + "Street does not exist")
            

 #function for finding intersection between lines and finding vertex cover           
def graph_formation():
   
    list_of_vertices=list(main_list.values())
    vertices=list()
    graph_points=list()
    graph_distinctVertices=set()
    graph_vertices=dict()
    dictionary_intersectionPoints=list()
    vertices_intersection=list()
    y=list()
    q=1
    r=1
    #last_element=list()
    streets_count=len(list_of_vertices)
    vertices=[None]*streets_count
    #last_element=[None]*streets_count
    for o in range (0,streets_count):
        y=[i.split(', ', 1)[0] for i in list_of_vertices[o]]
        vertices[o]=y
    for i in range(0,streets_count):
        #print "hi"
        for j in range (i+1,streets_count):
             k=len(vertices[i])
             #print "hi"
             l=len(vertices[j])
             while q<k:
                 while r<l:
                      
                      p1=vertices[i][q-1]
                      p2=vertices[i][q]
                      p3=vertices[j][r-1]
                      p4=vertices[j][r]
                      
                      x1,y1 = split_pair(p1)
                      x2,y2 = split_pair(p2)
                      x3,y3 = split_pair(p3)
                      x4,y4 = split_pair(p4)
                      x1=float(x1);x2=float(x2); x3=float(x3);x4=float(x4);
                      y1=float(y1);y2=float(y2);y3=float(y3);y4=float(y4);
                      p1="(" + str(x1) + "," +str(y1) + ")"
                      p2="(" + str(x2) + "," +str(y2) + ")"
                      p3="(" + str(x3) + "," +str(y3) + ")"
                      p4="(" + str(x4) + "," +str(y4) + ")"
                      thislist = list((p1,p2,p3,p4))
                      A = x2 - x1    
                      B = y2 - y1
                      C = x4 - x3
                      D = y4 - y3
                      determinant = (-C * B + A * D)

                      if abs(determinant) < 1e-20: 
                          pass
         
                      else:
                         s = (-B * (x1 - x3) + A * (y1 - y3)) / determinant
                         t = ( C * (y1 - y3) - D * (x1 - x3)) / determinant

                         if (bool(s >= 0) & bool(s <= 1) & bool(t >= 0) & bool(t <= 1)):
                             X=x1 + (t * A)
                             Y=y1 + (t * B)

                             X = float("{0:.2f}".format(X))
                             Y = float("{0:.2f}".format(Y))
                             new_vertex="(" + str(X) + "," +str(Y) + ")"                            
                             graph_points.extend(thislist)
                             dictionary_intersectionPoints.append(new_vertex)
                             vertices_intersection.append(thislist)
                             graph_points.append(new_vertex)
                             graph_distinctVertices=set(graph_points)
                             graph_points=list(graph_distinctVertices)
                             for z in range(0,len(graph_points)):
                                 graph_vertices[z+1]=graph_points[z]
                         else: 
                             pass
                         
                      r=r+1
                 q=q+1
                 r=1
             q=1
                                 
             
    print "Vertices = {"
    for x,y in graph_vertices.items():
        print x,": ",y 
    print "}"

    graph_GPSedges=list() 
    graph_GPSedgeset=set()
    repetitive_edges=list()
    for t in range(0, len(dictionary_intersectionPoints)):
        intersection_pt=dictionary_intersectionPoints[t]
        vertexlist=vertices_intersection[t]
        [p1, p2, p3, p4]=vertexlist
        for g in graph_vertices:
            
            if intersection_pt == graph_vertices[g]:
                edge_intersection=g
        for key,val in graph_vertices.items():
            if val==p1:
                edge_p1=key
                
        for key,val in graph_vertices.items():
            if val==p2:
                edge_p2=key
                
        for key,val in graph_vertices.items():
                 if val==p3:
                     edge_p3=key
                                                          
        for key,val in graph_vertices.items():
                if val==p4:
                    edge_p4=key
                   
                    edge1="<"+str(edge_intersection) + "," + str(edge_p1) + ">"
                    
                    edge2="<"+str(edge_intersection) + "," + str(edge_p2) + ">"
                   
                    edge3="<"+str(edge_intersection) + "," + str(edge_p3) + ">"
                    
                    edge4="<"+str(edge_intersection) + "," + str(edge_p4) + ">"
                    
                    edgelist = list((edge1,edge2,edge3,edge4))
                    graph_GPSedges.extend(edgelist)
                    graph_GPSedgeset=set(graph_GPSedges)
                    graph_GPSedges=list(graph_GPSedgeset)
                    distinct_x=list()
                    for n in range(0,len(graph_GPSedges)):
                        pair=graph_GPSedges[n]
                        pair=re.sub('<','(',pair)
                        pair=re.sub('>',')',pair)
                        y,z=split_pair(pair)
                        distinct_x.append(y)
                        distinct_set=set(distinct_x)
                        distinct_x=list(distinct_set)
                        for n1 in range(0, len(distinct_x)):
                            for n2 in range(n1+1,len(distinct_x)):
                                edge_betweeen = "<" + str(distinct_x[n1]) + "," + str(distinct_x[n2]) + ">"
                                graph_GPSedges.append(edge_betweeen)
                                graph_GPSedgeset = set(graph_GPSedges)
                                graph_GPSedges = list(graph_GPSedgeset)
    
    
    for b in range(0,len(graph_GPSedges)):
        edge = graph_GPSedges[b]
        edge = re.sub('<', '(', edge)
        edge = re.sub('>', ')', edge)
        pair1,pair2 = split_pair(edge)
        pair1,pair2=int(pair1),int(pair2)


        for c in graph_vertices:
            vertex1=graph_vertices[pair1]

            vertex2=graph_vertices[pair2]

            
            v_x1,v_y1=split_pair(vertex1)
            v_x2,v_y2=split_pair(vertex2)
            
            y,z=split_pair(pair)
            min_x1 = min(v_x1, v_x2)
            max_x1 = max(v_x1, v_x2)
            min_y1 = min(v_y1, v_y2)
            max_y1 = max(v_y1, v_y2)
            pair_check=graph_vertices[c]

            check_x,check_y=split_pair(pair_check)
            if((bool(check_x!=min_x1) & bool( check_x !=max_x1)) | ((bool(check_y!=min_y1) & bool(check_y!=max_y1)))):
                if(bool(check_x <= max_x1) & bool(check_x >= min_x1)):
                    if(bool(check_y <= max_y1) & bool(check_y >= min_y1)):
                        del_check="<" + str(pair1) + "," + str(pair2) + ">"

                        repetitive_edges.append(del_check)
                        repetitive_edges_set=set(repetitive_edges)
                        repetitive_edges=list(repetitive_edges_set)


    for d in range(0,len(repetitive_edges)):
        graph_GPSedges.remove(repetitive_edges[d])
    
    
    
    
    print "Edges ={"
    for u in graph_GPSedges:
        print u
    print "}"
       

def main():
    while True:
        coordinates=sys.stdin.readline()
        coordinates=coordinates.replace('\n','')
        #coordinates=raw_input()
        if(coordinates ==''):
            break
        elif(coordinates[0]=='r'):
            y=re.split(' +"|"|',coordinates)
        else:
            y=re.split('" +| +"',coordinates)
        if(len(y)==1):
            command=y[0]
        elif(len(y)==2):
            command=y[0]
            streetName=y[1]
            streetName=streetName.lower()   
        elif(len(y)==3):
            command=y[0]
            streetName=y[1]
            streetName=streetName.lower()
            GPSlocation=y[2]
        else:
            sys.stdout.write("Error: " + "Wrong selection of command")
            continue
        if command == 'a':
            check=check_street(streetName)
            if check==True:
                    add_street(GPSlocation,streetName)
            else:
                    print "Enter street in valid format."
            
        elif command == 'c':
            check_change=can_change(streetName)
            
            if check_change==True:
                
                    change_street(GPSlocation,streetName)
              
            else:
                 print"Street cannot be changed"
         
        elif command == 'r':
            remove_street(streetName)
            
        elif command == 'g':
            graph_formation()
          
        else:
            print 'Error: ' + 'Invalid command.Press a,g or r for valid commands.'

if __name__ == '__main__':
    main()