import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


columns = ["red",'green',"blue"]

path = "/Users/chenyuanyu/Desktop/water_mix_new/"

std_list = np.ndarray([])
# mean_list = np.ndarray([])

for i in range(1,87):
    data = pd.read_csv(path + "%d.csv"%i)
    data = data.iloc[:,1:4]
    data.columns = columns
    data["red_ratio"] = data["red"] / ((data["green"] + data["blue"])/2)
    std_list = np.append(std_list,data["red_ratio"].std())
    # mean_list = np.append(mean_list,data["red_ratio"].mean())
    color = ["r","g","b"]
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    for j in range(3):
        ax1.plot(data.iloc[:,j],color=color[j],label="%s_channel"%color[j])
    else:
        ax1.set_ylim([0,255])
        ax1.set_xlabel("distance(pixel)")
        ax1.legend()
    ax2 = fig.add_subplot(212)
    ax2.plot(data.iloc[:,3],color="k",label="red_ratio->R/[(G+B)/2]")
    ax2.set_ylim([0.8,3.5])
    ax2.set_xlabel("distance(pixel)")
    ax2.legend()
    plt.savefig("/Users/chenyuanyu/Desktop/test/%d.png"%i)
    plt.show()

else:
    outputData = pd.DataFrame(std_list,columns=["red_ratio_std"])
    outputData = outputData.drop(index=0)
    print(outputData)
    outputData.to_csv("./water_mix_newest.csv")





