#!/usr/bin/python

import random
import matplotlib.pyplot as plt

p = .5
cluster_num = 0

class Node:

    def __init__(self, parent = None, children = None, num=0, cluster = None):
        self.parent = parent
        self.children = children
        self.num = num
        rand_num = random.uniform(0,1)
        self.link = (rand_num < p) # link to parent
        self.cluster = cluster
    def added(self, adder):
        self.family.append(adder)

class Cluster:
    def __init__(self, num = None):
        self.num = num
        self.nodes = []
    def add_node(self, node):
        self.nodes.append(node)

index = 0
node_list = []
cluster_list = []
reserves = []
init_child = [Node(), Node()]
reserves.extend(init_child)
head = Node(None, init_child, index, cluster_num)
head_cluster = Cluster(cluster_num)
head_cluster.add_node(head)
cluster_list.append(head_cluster)
cluster_num =+ 1
node_list.append(head)
index += 1
for child in head.children:
    node_list.append(child)
    child.parent = head
    child.num = index
    if not child.link:
        new_cluster = Cluster(cluster_num)
        new_cluster.add_node(child)
        cluster_list.append(new_cluster)
        child.cluster = cluster_num
        cluster_num =+ 1
    else:
        child.cluster = child.parent.cluster
        cluster_list[child.cluster].add_node(child)
    index += 1

gens = 0
while gens < 15:
    new_reserves = []
    for node in reserves:
        new_child = [Node(), Node()]
        node.children = new_child
        for child in node.children:
            node_list.append(child)
            child.parent = node
            child.num = index
            index += 1
            if not child.link:
                new_cluster = Cluster(cluster_num)
                new_cluster.add_node(child)
                cluster_list.append(new_cluster)
                child.cluster = cluster_num
                cluster_num += 1
            else:
                child.cluster = child.parent.cluster
                cluster_list[child.cluster].add_node(child)

        new_reserves.extend(new_child)
    reserves = new_reserves
    gens += 1

tallies = {}
for cluster in cluster_list:
    if len(cluster.nodes) in tallies:
        tallies[len(cluster.nodes)] += 1
    else:
        tallies[len(cluster.nodes)] = 1

print(tallies)

x_vals = [i for i in range(1, max(t for t in tallies))]
y_vals = [0] * len(x_vals)

for x in x_vals:
    if x in tallies:
        y_vals[x-1] = tallies[x]

print(x_vals, y_vals)

plt.plot(x_vals, y_vals)
plt.show()
