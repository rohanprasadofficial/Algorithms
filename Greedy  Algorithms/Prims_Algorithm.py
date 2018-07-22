graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0],
           ]
"""graph = [
  [0, 9, 75, 0, 0],
  [9, 0, 95, 19, 42],
  [75, 95, 0, 51, 66],
  [0, 19, 51, 0, 31],
  [0, 42, 66, 31, 0]
]"""

selected=[0 for i in range(5)]
selected[0]=True
no_edge=0
INF=9999
while(no_edge<4):
        x=0
        min=INF
        y=0
        for i in range(5):

            if(selected[i]):

                for j in range(5):
                    if( not selected[j] and graph[i][j]):
                        if(graph[i][j]<min):
                            min=graph[i][j]
                            x=i
                            y=j
        print(" {}  : {} - {}".format(x,y,graph[x][y]))
        selected[y]=True
        no_edge=no_edge+1
