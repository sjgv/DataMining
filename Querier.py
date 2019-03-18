import json
import matplotlib.pyplot as plt

def liveCall(comparisonDic, matlabDic):
    while(True):
        num = input("Enter index:")
        print(comparisonDic[num])
        print()
        print(matlabDic[num])
        if(num == "-1"):
            break
def main():
    with open("path_filename.txt") as filehandle:
        path_filename = json.load(filehandle)
    with open("comparisonDict.json") as filehandle:
        comparisonDic = json.load(filehandle)
    with open("matlabDict.json") as filehandle:
        matlabDic = json.load(filehandle)
    
    #liveCall(comparisonDic, matlabDic)
    for k,v in comparisonDic.items():
        for y in v:
            plt.scatter(int(k), int(y[0]))
    plt.gray()
    plt.show()


if __name__=="__main__":
    main()