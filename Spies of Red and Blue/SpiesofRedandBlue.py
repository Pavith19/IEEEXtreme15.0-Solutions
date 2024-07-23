"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not (start in graph):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def whatsNext(int2R1, int2B1):
    if int2R1 is not None and int2B1 is not None:
        i2R = len(int2R1)-1
        i2B = len(int2B1)-1
        if i2B == i2R:
            print("TIE ", i2R)
        elif i2B < i2R:
            print("BLUE ",i2B)
        else:
            print("RED ", i2R)
    elif int2R1 is not None and int2B1 is None:
        print("RED ", len(int2R1)-1)
    elif int2R1 is None and int2B1 is not None:
        print("BLUE ",len(int2B1)-1)
    else:
        print("NONE")

T = int(input())
for i in range(T):
    NR, NB, E = [int(x) for x in input().split()]
    Red = {"R"+str(i):[] for i in range(1,NR+1)}
    Blue = {"B"+str(i):[] for i in range(1,NB+1)}
    RedSeniors  = input().split()
    BlueSeniors = input().split()
    for i, rsenior in enumerate(RedSeniors):
        Red[rsenior].append("R"+str(i+2))
    for j, bsenior in enumerate(BlueSeniors):
        Blue[bsenior].append("B"+str(j+2))
    # complete graph: two disjoint graphs at the beginning
    graph = Red
    graph.update(Blue)
    print(len(graph.keys()))
    for event in range(E):
        e, x, y = input().split()
        if e == 'c': # spi crossover
            # remove previous bond
            for key in graph.keys():
                if x in graph[key]:
                    graph[key].remove(x)
            # assign new
            graph[y].append(x)
            
        else: # battle?

            # function call to traverse the graph
            
            reachable = {}
            # information flow to R1
            R1ToX = find_shortest_path(graph,"R1", x,path =[])
            # print("X To R1", R1ToX)
            R1ToY = find_shortest_path(graph,"R1", y,path =[])
            # print("Y To R1", R1ToY)

            # information flow to B1
            B1ToX = find_shortest_path(graph,"B1", x,path =[])
            # print("X To B1", B1ToX)
            B1ToY = find_shortest_path(graph,"B1", y,path =[])
            # print("Y To B1", B1ToY)
            
            if (R1ToX==None):
                if(R1ToY==None):
                    if(B1ToX==None):
                        if(B1ToY==None):
                            print("NONE")
                        else:
                            print("BLUE",len(B1ToY)-1)
                    else:
                        if(B1ToY==None):
                            print("BLUE",len(B1ToX)-1)
                        else:
                            print("BLUE",min(len(B1ToX)-1, len(B1ToY)-1))
                else:# R1ToY exists
                    if(B1ToX==None):
                        if(B1ToY==None):
                            print("RED", len(R1ToY)-1)
                        else:# B1ToY exits
                            r1toy = len(R1ToY)
                            b1toy = len(B1ToY)
                            if r1toy < b1toy:
                                print("RED", r1toy-1)
                            elif r1toy > b1toy:
                                print("BLUE", b1toy-1)
                            else:
                                print("TIE", r1toy-1)
                  
                    else:#B1ToX EXISTS
                        if(B1ToY==None):
                            r1toy = len(R1ToY)
                            b1tox = len(B1ToX)
                            if r1toy < b1tox:
                                print("RED", r1toy-1)
                            elif r1toy > b1tox:
                                print("BLUE", b1tox-1)
                            else:
                                print("TIE", r1toy-1)
                        else:#B1ToY Exists
                            r1toy = len(R1ToY)
                            b1tox = len(B1ToX)
                            if (r1toy < min(b1tox,b1toy)):
                                print("RED", r1toy-1)
                            elif (r1toy > min(b1tox,b1toy)):
                                print("BLUE",min(b1tox,b1toy)-1)
                            else:
                                print("TIE", r1toy-1)
                            # else:
                            #     if(b1tox < b1toy):
                            #         print("BLUE", b1tox-1)
                            #     else:
                            #         print("BLUE", b1toy-1)
# main else of r1tox exists                                    
            else:#R1ToX exists
                if(R1ToY==None):
                    if(B1ToX==None):
                        if(B1ToY==None):
                            print("RED", len(R1ToX)-1)
                        else:#B1ToY exists
                            b1toy = len(B1ToY)
                            r1tox = len(R1ToX)
                            if (r1tox < b1toy):
                                print("RED", r1tox-1)
                            elif(r1tox > b1toy):
                                print("BLUE", b1toy-1)
                            else:
                                print("TIE", b1toy-1)

                    else:#B1ToX exists
                        if(B1ToY==None):
                            b1tox = len(B1ToX)
                            r1tox = len(R1ToX)
                            if(b1tox < r1tox):
                                print("BLUE", b1tox-1)
                            elif(b1tox > r1tox):
                                print("RED", r1tox-1)
                            else:
                                print("TIE", b1tox-1)
                        else:#B1ToY exists
                            b1tox = len(B1ToX)
                            b1toy = len(B1ToY)
                            r1tox = len(R1ToX)
                            if(r1tox < min(b1tox, b1toy)):
                                print("RED", r1tox-1)
                            elif(r1tox > min(b1tox, b1toy)):
                                print("BLUE", min(b1tox,b1toy)-1)
                            else:
                                print("TIE", r1tox-1)

                else:# R1ToY, R1ToX exists
                    if(B1ToX==None):
                        if(B1ToY==None):
                            print("RED", min( len(R1ToX) , len(R1ToY) )-1)
                        else:# B1ToY exits
                            r1tox = len(R1ToX)
                            r1toy = len(R1ToY)
                            b1toy = len(B1ToY)
                            if(b1toy < min(r1tox, r1toy)):
                                print("BLUE", b1toy-1)
                            elif(b1toy > min(r1tox, r1toy)):
                                print("RED", min(r1tox, r1toy)-1)
                            else:
                                print("TIE",b1toy-1)
                  
                    else:#B1ToX EXISTS
                        if(B1ToY==None):
                            r1toy = len(R1ToY)
                            r1tox = len(R1ToX)
                            b1tox = len(B1ToX)
                            if(b1tox < min(r1toy, r1tox)):
                                print("BLUE", b1tox-1)
                            elif(b1tox > min(r1toy, r1tox)):
                                print("RED", min(r1tox, r1toy)-1)
                            else:
                                print("TIE",b1tox-1)
                            
                        else:#B1ToY Exists
                            r1toy = len(R1ToY)
                            r1tox = len(R1ToX)

                            b1toy = len(B1ToY)
                            b1tox = len(B1ToX)
                            if(min(r1tox,r1toy) < min(b1tox, b1toy)):
                                print("RED", min(r1tox,r1toy)-1)
                            elif(min(r1tox,r1toy) > min(b1tox, b1toy)):
                                print("BLUE", min(b1tox, b1toy)-1)
                            else:
                                print("TIE", min(r1tox,r1toy)-1 )
                
                            
                
                            

            
