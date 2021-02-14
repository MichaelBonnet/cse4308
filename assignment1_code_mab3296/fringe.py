import sys
import readinputfile as readInputFiles
import heuristic as heu
import operator

#Node Structure
class nodestructure:
    def __init__(self, prnt, state, g, d, f, Uninformed):
        self.prnt = prnt
        self.state = state
        self.g = g
        self.d = d
        self.f = f
        self.Uninformed = Uninformed


    def __str__(self):
        if self.Uninformed:
            return self.state+": g(n)= "+str(self.g) + ",d= "+str(self.d)+",Parent ->{"+str(self.prnt)+"}"
        else:
            return self.state+": g(n)="+str(self.g)+",d= "+str(self.d)+", f(n) = "+str(self.f)+", Parent ->{"+str(self.prnt)+"}"

 # uses map and heuristic   to generate successors
def expandNode(node, map, h,SearchType):
    actions = map[node.state]
    successor = []
    for i in actions:
        costtotal = node.g + i[1]
        if node.Uninformed:
            successor.append(nodestructure(node, i[0], costtotal, node.d + 1, 0, node.Uninformed))
        else:
            successor.append(nodestructure(node, i[0], costtotal, node.d + 1, costtotal + h[i[0]], node.Uninformed))
    return successor

def getkey(item,n):
    return item[n]

# reconstruct the path from node
def reconstruct(node, map,SearchType):
    s = []
    distance = node.g
    while node is not None:
        parent = node.prnt
        if parent is not None:
            act = (a for a in map[parent.state] if
                   a[0] == node.state)
            a=next(act)
            s.append(parent.state+" to "+node.state+ ", "+str(a[1])+" kms")
        node = parent
    s.reverse()
    print("distance : " + str(distance))
    print("route :")
    for i in s:
        print(i)
