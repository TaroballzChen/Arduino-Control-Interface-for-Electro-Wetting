import pandas as pd


columns = ["red_mean","red_stdev","green_mean","green_stdev","blue_mean","blue_stdev"]

outputData = pd.DataFrame(columns=columns)


for i in range(1,81):
    data = pd.read_csv("/Users/chenyuanyu/Desktop/water_merge_new/%d.csv"%i,index_col=0)
    insertRow = pd.DataFrame([[data["mean"][1],data["std.dev."][1],data["mean"][2],data["std.dev."][2],data["mean"][3],data["std.dev."][3]]],columns=columns)
    outputData = outputData.append(insertRow,ignore_index=True)
else:
    print(outputData)
    outputData.to_csv("./water_merge_new.csv")





