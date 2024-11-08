
def getData():
    with open('C:\\Users\\oussama.anadani\\Desktop\\PythonOnlineProblems\\AOF\\AdventOfCode\\2023\\day5\\data.txt') as f:
        data = f.read()
        return data

def data_preProcessing(data):
    data = data.strip().split("\n\n")
    seeds = data[0].split(":")[1].split()
    all_maps = [data[idx].split("map:") for idx in range(1,len(data))]
    return seeds, all_maps

def create_mapList(dist,src,range_):
    src_list = []
    dist_list = []
    src_list.append(int(src))
    dist_list.append(int(dist))
    for _ in range(0,int(range_)-1):
        src = int(src) + 1
        dist = int(dist)+ 1
        src_list.append(src)
        dist_list.append(dist)      
    return src_list, dist_list

def split_maps(maps):
    for map in maps:
        map_name, map_values = map
        lines = map_values.strip().splitlines()
        for line in lines:
            dist, src, range_= line.split()
            src, dist = create_mapList(dist,src,range_)


def star1():
    data=getData()
    seeds,all_maps=data_preProcessing(data)
    maps= split_maps(all_maps)

if __name__ == "__main__":
    star1()