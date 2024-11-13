def getData():
    with open('C:\\Users\\oussama.anadani\\Desktop\\PythonOnlineProblems\\AOF\\AdventOfCode\\2023\\day5\\data.txt') as f:
        data = f.read()
        return data

def data_preProcessing(data):
    data = data.strip().split("\n\n")
    seeds = data[0].split(":")[1].split()
    categories = [data[idx].split("map:") for idx in range(1,len(data))]
    return seeds, categories

def check_for_src_in_range(seed, category_lines):
    for line in category_lines: 
        dist, src, length= line.split()
        src, dist, length = int(src),int(dist),int(length)
        if seed >= src and seed <= (src+length):
            return dist, src, length


def ceate_conversion_map(current_src, category_lines):
    src_dist_map={}
    result = check_for_src_in_range(current_src, category_lines)         
    if result is not None:
        dist, src, length = result
        for _ in range(length):
            src_dist_map[src]=dist
            src +=1
            dist +=1
    return src_dist_map

def search_in_map(seed, src_dist_map):
    return src_dist_map.get(seed,seed)

def get_min_location(seed, categories):
    current_src = seed
    for ctgry_name, category_lines in categories:    
        category_lines = category_lines.strip().splitlines()
        src_dist_map = ceate_conversion_map(current_src, category_lines)
        if src_dist_map:
            distination=search_in_map(current_src, src_dist_map)
            current_src=distination
    return current_src


def star1():    
    data=getData()
    seeds, categories=data_preProcessing(data)
    all_locaions=[get_min_location(int(seed), categories) for seed in seeds]    
    print(min(all_locaions))

if __name__ == "__main__":
    star1()