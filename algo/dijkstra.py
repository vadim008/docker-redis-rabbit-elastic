
# import re
#
# cli_ouput = "0020 | 2018-05-07 19:23:01 | SMI Timeout | POST Error | POST Error code = 0x146: PCI out of resources error | Asserted \n \
# 023c | 2018-10-31 17:47:57 | Power Unit Redundancy | Memory Error | ECC Correctable Error on node 1 channel 2 dimm 1 reserved 0 rank 1 | Asserted \n \
# 0247 | 2018-12-06 02:58:59 | SMI Timeout | POST Error | POST Error code = 0x8533: DIMM_G2 failed test/initialization | Asserted \n \
# 0248 | 2018-12-06 02:58:59 | SMI Timeout | POST Error | POST Error code = 0x8553: DIMM_G2 disabled | Asserted"
#
#
#
# faulty_dimm_list = []
# faulty_dimm_chan_list = []
# dimms_names_channels_population = {"DIMM_C":[0,2],"DIMM_D":[0,3],"DIMM_B":[0,1],"DIMM_A":[0,0],"DIMM_G":[1,2],"DIMM_H":[1,3],"DIMM_F":[1,1],"DIMM_E":[1,0]}   #[Node,Channel]
#
# cli_ouput = cli_ouput.splitlines()
# for line in cli_ouput:
#     line = line.replace("-", "")
#     words = line.split(" ")
#
#     if "disabled" in line:
#         continue
#
#     if 'DIMM_' in line:
#         for dimm_name in words:
#             if 'DIMM_' in dimm_name:
#                 dimm_channel = dimm_name[:-1]
#                 dimm_info = dimms_names_channels_population[dimm_channel]
#                 if dimm_info not in faulty_dimm_chan_list:
#                     faulty_dimm_chan_list.append(dimm_info)
#                 break
#     else:
#      #   if "node " in line:
#         val = line[line.find('node '):]
#
#         dimm_info = re.findall(r'\d+', val)
#         dimm_info = dimm_info[:3]  # Need the CPU , channel and DIMM
#
#         if dimm_info not in faulty_dimm_list:
#             faulty_dimm_list.append(dimm_info)
#
# if len(faulty_dimm_list) or len(faulty_dimm_chan_list):
#     if len(faulty_dimm_list) > 1 or len(faulty_dimm_chan_list) > 1:
#         print ("Error more than one")
#     elif len(faulty_dimm_list) == 1:
#         if len(faulty_dimm_chan_list):
#             # if same chan , allow it
#             temp_dimm_info = [(int)(faulty_dimm_list[0][0]), (int)(faulty_dimm_list[0][1])]
#             if temp_dimm_info not in faulty_dimm_chan_list:
#                 print("Error more than one")


from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def addEdge(self, x, y, weigth):
        d = self.graph[x] if x in self.graph else {}
        d[y] = weigth
        self.graph[x] = d


    def run_dijkstra(self, start, end):
        infinity = 999999
        path = []
        unseenodes = self.graph
        predesesors = {}
        shortest_distance = {}

        for node in unseenodes:
            shortest_distance[node] = infinity

        shortest_distance[start] = 0


        # now start teh real algorithm
        while unseenodes:

            # find the node with min weigth
            #{'A': 0, 'B': 10, 'C': 14, 'D': 12, 'E': 999999}
            min_node = None
            for node in unseenodes:
                if min_node == None:
                    min_node = node
                elif shortest_distance[min_node] > shortest_distance[node]:
                    min_node = node


            # Run on all its childred and update chidlred in parent_calculated_distance + child < child_calculated_distance
            for child_node, child_weigth in self.graph[min_node].items():
                if child_weigth + shortest_distance[min_node] < shortest_distance[child_node]:
                    shortest_distance[child_node] = child_weigth + shortest_distance[min_node]
                    predesesors[child_node] = min_node



            unseenodes.pop(min_node)

        print(str(self.graph))
        print(shortest_distance)
        print(predesesors)

        current_node = end;
        while current_node != start:
            try:
                path.insert(0, current_node)
                current_node = predesesors[current_node]
            except KeyError:
                print ("Path not reacheble")
                break

        path.insert(0, start)

        if shortest_distance[end] != infinity:
            print("Shortest distance is: " + str(shortest_distance[end]))
            print ("Path: "  + str(path))


        return path



if __name__ == '__main__':



    g = Graph()
    g.addEdge("A", "B", 10)
    g.addEdge("A", "C", 3)
    g.addEdge("B", "C", 4)
    g.addEdge("C", "B", 4)
    g.addEdge("B", "D", 2)
    g.addEdge("C", "D", 8)
    g.addEdge("C", "E", 2)
    g.addEdge("D", "E", 9)
    g.addEdge("E", "D", 9)

    print ("Following is dijkstra's  Shortest Path"
           " (starting from vertex A to E)")


    path = g.run_dijkstra("A", "E")
    print (path, end = " !!!!!! ")

