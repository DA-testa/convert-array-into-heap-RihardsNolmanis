def build_heap(data):
    length = len(data)
    swaps = []
    for i in range(length, -1, -1):
        j = i
        while True:
            tree = (j * 2) + 1
            if tree >= length:
                break
            if tree+1 < length and data[tree+1] < data[tree]:
                tree = tree + 1
            if data[j] > data[tree]:
                swaps.append((j, tree))
                data[j], data[tree] = data[tree], data[j]
                j = tree
            else:
                break
    return swaps


def main():
    inputs = input()
    if 'I' in inputs:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    elif 'F' in inputs:
        
        filename = input()
        with open("tests/" + filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
        return

if __name__ == "__main__":
    main()
