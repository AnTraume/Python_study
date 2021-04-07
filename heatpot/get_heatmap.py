import numpy as np
import matplotlib.pyplot as plt
import sys

vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

#sys.stdin = open("/home/antraume/costmap/build/costmap_data.txt", "r")
sys.stdin = open("./gridmap1.txt","r")
#ksys.stdin = open("/home/antraume/Python_study/heatpot/gridmap1.txt","r")
#sys.stdin = open("/home/antraume/Python_study/heatpot/dwa_test.txt","r")
# for i in range(972):
i = 0
flag = False
while True:
    fig, ax = plt.subplots()
    data = []
    while True:
        t = input().split()
        if len(t) > 9:
            data.append(list(map(int, t)))
        else:
            if flag:
                break
            else:
                flag = True
    im = ax.imshow(np.array(data))
    plt.savefig("./map_show/{0}.jpg".format(i))
    #plt.show()
    plt.close()
    i += 1
