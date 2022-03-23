from waypy.list import list

class search(object):

    def amplitude(self, begin, end, nodes, graph):

        # manipulate the queue for the seach
        l1 = list()

        # copy to present the way (insertion only)
        l2 = list()

        # insert start point as root node of tree
        l1.insertLast(begin,0,None)
        l2.insertLast(begin,0,None)

        # control of visited nodes
        visited = []
        line = []
        line.append(begin)
        line.append(0)
        visited.append(line)

        while l1.empty() == False:
            # remove the first from queue
            current = l1.deleteFirst()
            if current is None: break

            ind = nodes.index(current.value1)

            # scan all connections within the graph starting from current
            for i in range(len(graph[ind])):

                new = graph[ind][i]
                # assuming not visited
                flag = True

                # repeat node control
                for j in range(len(visited)):
                    if visited[j][0]==new:
                        if visited[j][1]<=(current.value2+1):
                            flag = False
                        else:
                            visited[j][1]=current.value2+1
                        break
                
                # if not visited, include it in the queue
                if flag:
                    l1.insertLast(new, current.value2 + 1, current)
                    l2.insertLast(new, current.value2 + 1, current)

                    # marks as visited
                    line = []
                    line.append(new)
                    line.append(current.value2+1)
                    visited.append(line)

                    # check if it's the goal
                    if new == end:
                        way = []
                        way += l2.showway()
                        #print("Fila:\n",l1.showlist())
                        #print("\nÁrvore de busca:\n",l2.showlist())
                        return way

        return "way not found"


    def depth(self, begin, end, nodes, graph):
        
        way = []

        # manipulate the QUEUE for the search
        l1 = list()

        # copy to present the way (insertion only)
        l2 = list()

        # insert start point as root node of tree
        l1.insertLast(begin,0,None)
        l2.insertLast(begin,0,None)

        # control of visited nodes
        visited = []
        line = []
        line.append(begin)
        line.append(0)
        visited.append(line)


        while l1.empty() == False:
            # remove the first from queue
            current = l1.deleteLast()
            if current is None: break

            ind = nodes.index(current.value1)

            # scan all connections within the graph starting from current
            for i in range(len(graph[ind])-1,-1,-1):

                new = graph[ind][i]
                #print("\tFilho de current: ",new)
                flag = True  # assuming not visited

                # for each connection checks if it has already been visited
                for j in range(len(visited)):
                    if visited[j][0]==new:
                        if visited[j][1]<=(current.value2+1):
                            flag = False
                        else:
                            visited[j][1]=current.value2+1
                        break
                    
                
                # if not visited, include it in the queue
                if flag:
                    l1.insertLast(new, current.value2 + 1, current)
                    l2.insertLast(new, current.value2 + 1, current)

                    # marks as visited
                    line = []
                    line.append(new)
                    line.append(current.value2+1)
                    visited.append(line)

                    # check if it's the goal
                    if new == end:
                        way += l2.showway()
                        #print("Árvore de busca:\n",l2.showlist())
                        return way

        return "way não encontrado"


    def limitaded_depth(self, begin, end, limit, nodes, graph):
        
        way = []

        # manipulate the queue for the search
        l1 = list()

        # copy to present the way (insertion only)
        l2 = list()

        # insert start point as root node of tree
        l1.insertLast(begin,0,None)
        l2.insertLast(begin,0,None)

        # control of visited nodes
        visited = []
        line = []
        line.append(begin)
        line.append(0)
        visited.append(line)


        while l1.empty() == False:
            # remove the first from queue
            current = l1.deleteLast()
            if current is None: break

            if current.value2 < limit:
                ind = nodes.index(current.value1)
    
                # scan all connections within the graph starting from current
                for i in range(len(graph[ind])-1,-1,-1):
    
                    new = graph[ind][i]
                    #print("\tFilho de current: ",new)
                    flag = True  # assuming not visited
    
                    # for each connection checks if it has already been visited
                    for j in range(len(visited)):
                        if visited[j][0]==new:
                            if visited[j][1]<=(current.value2+1):
                                flag = False
                            else:
                                visited[j][1]=current.value2+1
                            break
                        
                    
                    # if not visited, include it in the queue
                    if flag:
                        l1.insertLast(new, current.value2 + 1, current)
                        l2.insertLast(new, current.value2 + 1, current)
    
                        # marks as visited
                        line = []
                        line.append(new)
                        line.append(current.value2+1)
                        visited.append(line)
    
                        # check if it's the goal
                        if new == end:
                            way += l2.showway()
                            #print("Árvore de busca:\n",l2.showlist())
                            return way

        return "way not found"


    def iterative_deepening(self, begin, end, nodes, graph):
        
        for limit in range(len(nodes)):
            way = []
    
            # manipulate the queue for the search
            l1 = list()
    
            # copy to present the way (insertion only)
            l2 = list()
    
            # insert start point as root node of tree
            l1.insertLast(begin,0,None)
            l2.insertLast(begin,0,None)
    
            # control of visited nodes
            visited = []
            line = []
            line.append(begin)
            line.append(0)
            visited.append(line)
    
    
            while l1.empty() is not None:
                # remove the first from queue
                current = l1.deleteLast()
                if current is None: break
    
                if (current.value2) < limit:
                    ind = nodes.index(current.value1)
        
                    # scan all connections within the graph starting from current
                    for i in range(len(graph[ind])-1,-1,-1):
        
                        new = graph[ind][i]
                        #print("\tFilho de current: ",new)
                        flag = True  # assuming not visited
        
                        # for each connection checks if it has already been visited
                        for j in range(len(visited)):
                            if visited[j][0]==new:
                                if visited[j][1]<=(current.value2+1):
                                    flag = False
                                else:
                                    visited[j][1]=current.value2+1
                                break
                            
                        
                        # if not visited, include it in the queue
                        if flag:
                            l1.insertLast(new, current.value2 + 1, current)
                            l2.insertLast(new, current.value2 + 1, current)
        
                            # marks as visited
                            line = []
                            line.append(new)
                            line.append(current.value2+1)
                            visited.append(line)
        
                            # check if it's the goal
                            if new == end:
                                way += l2.showway()
                                #print("Árvore de busca:\n",l2.showlist())
                                return way

        return "way not found"

    def bidirecional(self, begin, end, nodes, graph):

        # lists for searching from source - search 1
        l1 = list()      # queue search
        l2 = list()      # full tree copy

        # lists for searching from destination - search 2
        l3 = list()      # queue search
        l4 = list()      # full tree copy

        # creates structure to control visited nodes
        visited = []

        l1.insertLast(begin,0,None)
        l2.insertLast(begin,0,None)
        line = []
        line.append(begin)
        line.append(1)
        visited.append(line)
        
        l3.insertLast(end,0,None)
        l4.insertLast(end,0,None)
        line = []
        line.append(end)
        line.append(2)
        visited.append(line)
        
        while True:
            
            # EXECUTION OF THE FIRST AMPLITUDE - SEARCH 1
            flag1 = True
            while flag1:
                current = l1.deleteFirst()
                ind = nodes.index(current.value1)
                for i in range(len(graph[ind])):
                    new = graph[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visited)):
                        if visited[j][0]==new:
                            if visited[j][1] == 1:    # visited in the same tree
                                flag2 = False
                            else:                      # visited in the other tree
                                flag3 = True
                            break
                    # for j
                        
                    if flag2:
                        l1.insertLast(new, current.value2 + 1 , current)
                        l2.insertLast(new, current.value2 + 1, current)
                        
                        if flag3:
                            way = []
                            way = l2.showway()
                            #way = way[::-1]
                            way += l4.showway1(new)
                            return way
                        else:
                            line = []
                            line.append(new)
                            line.append(1)
                            visited.append(line)
                        # if flag3
                    # if flag2
                # for i
                
                
                if(l1.empty()!=True):
                    aux = l1.first()
                    if aux.value2 == current.value2:
                        flag1 = True
                    else:
                        flag1 = False                

            # EXECUTION OF THE SECOND RANGE - SEARCH 2
            flag1 = True
            while flag1:
                current = l3.deleteFirst()
                if current==None:
                    break
                ind = nodes.index(current.value1)
                for i in range(len(graph[ind])):
                    new = graph[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visited)):
                        if visited[j][0]==new:
                            if visited[j][1] == 2:
                                flag2 = False
                            else:
                                flag3 = True
                            break
                        
                    if flag2:
                        l3.insertLast(new, current.value2 + 1 , current)
                        l4.insertLast(new, current.value2 + 1, current)
                        
                        if flag3:
                            way = []
                            way = l4.showArvore()
                            way = way[::-1]
                            way += l2.showArvore1(new)
                            return way
                        else:
                            line = []
                            line.append(new)
                            line.append(2)
                            visited.append(line)
                        
                if(l3.empty() != True):
                    aux = l3.first()
                    if(current.value2 == aux.value2):
                        flag1 = True
                    else:
                        flag1 = False