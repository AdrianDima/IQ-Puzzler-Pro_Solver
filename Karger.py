#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 01:17:16 2021

@author: adrian
"""
import random
import copy

grapf_text_file = open("kargerMinCut.txt", "r")
GreadFromFile = []
for line in grapf_text_file.readlines():
    tmp = []
    for element in line[0:-1].split():
        tmp.append (int(element))
    GreadFromFile.append(tmp)
grapf_text_file.close()

# build the Grapf list of lists:
Goriginal = []
for item in GreadFromFile:
    adjacentNodes = []
    for i in range(1, len(item)):
        tmp = [item[i], 1]
        adjacentNodes.append(tmp)
    Goriginal.append(adjacentNodes)

    
def printG(G):
    for item in G:
        print(item)
    print()
    

def GrapfLength(G):# count the NOT isolated vertices
    count = 0
    for v in G:
        if v:
            count += 1
    return count


def countingPaarNodes(G):
    m = 0
    for v in G:
        m += len(v)
    return m


def nodesPaar(rand, G):
    currentSublist = 0
    NodesPairs = 0 # the number of nodes in the sublists traversed
    for i in range(len(G)):
        NodesPairs += len(G[i])
        if NodesPairs >= rand:
            currentSublist = i
            break
    
    aaa = 0
    for i in range(currentSublist):
        aaa += len(G[i])

    return (currentSublist + 1, G[currentSublist][rand - aaa - 1][0])


def adjacentNodesList(nod, G):
    adjacentNodesList = []
    for node in G[nod - 1]:
        adjacentNodesList.append(node[0])
    return adjacentNodesList


def Karger(G):
    while GrapfLength(G) > 2:
#        printG(G)
        m = countingPaarNodes(G)
#        print("m = " + str(m))
        r = random.randint(1, m)
        print("r = " + str(r))
        a, b = nodesPaar(r, G)
        u = min(a, b)
        v = max(a, b) # vertex v will be removed

        UadjacentNodes = adjacentNodesList(u, G)
        print("u = " + str(u) + " -> " + str(UadjacentNodes))
        VadjacentNodes = adjacentNodesList(v, G)
        print("v = " + str(v) + " -> " + str(VadjacentNodes))
        
        VadjacentNodes.remove(u) # remove u from v's adjacent nodes list
        
        for adjacent in VadjacentNodes:
            tmpV = []
            for node in G[v - 1]:
                if node[0] == adjacent:
                    tmpV = node[:]
                    break
            
            if adjacent not in UadjacentNodes:
                G[u - 1].append(tmpV)
                G[adjacent - 1].append([u, tmpV[1]])
            else:
                tmpU = []
                for node in G[u - 1]:
                    if node[0] == adjacent:
                        node[1] += tmpV[1]
                        break
                for node in G[adjacent - 1]:
                    if node[0] == u:
                        node[1] += tmpV[1]
                        break
                    
        # remove all edges to v from grapf:
        for item in G:
            for adjacent in item:
                if adjacent[0] == v:
                    item.remove(adjacent)
        
        # make the vertex v isolate
        G[v - 1] = []


G = copy.deepcopy(Goriginal)
printG(G)
Karger(G)
printG(G)

"""
def minCut(G):
    for v in G:
        if v:
            return v[0][1]
    return 0


res = []
for i in range(100):
    G = copy.deepcopy(Goriginal)
    Karger(G)
    res.append(minCut(G))
print(min(res))
"""
