from collections import defaultdict
power_rate = 1
eps = []
gamma_rate = []

zeros = 0
ones = 0
bit_dict = defaultdict(list)

with open("data3.txt") as f:
    lines = f.readlines()
    for line in lines:
        for i in range(0,len(line)):
            if line[i] != "\n":
                bit_dict[i].append(line[i])

    for i in bit_dict.keys():
        zeros = 0
        ones = 0
        for bit in bit_dict[i]:   
            if bit == '1':
                ones =ones + 1
            else:
                zeros = zeros + 1
        if ones > zeros:
            gamma_rate.append('1')
        else:
            gamma_rate.append('0')
    
    gr = ''.join(gamma_rate)
    eps = ''.join(['1' if i == '0' else '0' for i in gr])
    gr = int(gr,2)
    eps = int(eps,2)
    power_rate = eps * gr
    print(power_rate)
    f.close()