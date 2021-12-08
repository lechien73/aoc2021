fishies = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

def init():

    content = list(map(int, open("day6.txt").read().split(",")))

    for k in fishies.keys():
        fishies[k] = 0

    for c in content:
        fishies[c] += 1

def run_cycle(count):

    for i in range(count):
        new8 = fishies[0]
        fishies[0] = 0
        
        for k,v in fishies.items():
            if k > 0:
                fishies[k - 1] = fishies[k]
                
        fishies[8] = new8
        fishies[6] += new8
    
    return(sum(fishies.values()))


init()
print(f"Solution to part 1: {run_cycle(80)}")
init()
print(f"Solution to part 2: {run_cycle(256)}")
