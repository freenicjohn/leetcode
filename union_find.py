class UF:
    def __init__(self, members):
        self.parent = {member:member for member in members}

    def find(self, i):
        if self.parent[i] == i:
            return i
        else:
            return self.find(self.parent[i])
        
    def union(self, i, j):
        i_parent = self.find(i)
        j_parent = self.find(j)

        self.parent[i_parent] = j_parent

    
if __name__ == "__main__":
    uf = UF([1, 2, 3, 4, 5, 6, 7])
    
    print(uf.find(6))  # 6

    uf.union(6, 2)
    uf.union(7, 2)

    print(uf.parent)

    print(uf.find(7))
    print(uf.find(6))
    print(uf.find(2))

    uf.union(1,7)
    print(uf.parent)
    print(uf.find(1))
