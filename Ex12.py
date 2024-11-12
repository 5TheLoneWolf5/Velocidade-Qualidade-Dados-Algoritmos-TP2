class TabelaHash:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0

    def hash(self, key):
        print(hash(key))
        print(hash(key) % self.capacity)
        return hash(key) % self.capacity

    def inserir(self, chave, valor):
        idx = self.hash(chave)

        for pair in self.table[idx]:
            if pair[0] == chave:
                pair[1] = valor
                return

        self.table[idx].append([chave, valor])
        self.size += 1

    def buscar(self, chave):
        idx = self.hash(chave)

        for pair in self.table[idx]:
            if pair[0] == chave:
                return pair[1]

        return None
        
    def remover(self, chave):
        idx = self.hash(chave)

        for i, pair in enumerate(self.table[idx]):
            if pair[0] == chave:
                del self.table[idx][i]
                self.size -= 1
                return True

        return False
    
    def __str__(self):
        result = []

        for listTable in self.table:
            for pair in listTable:
                result.append(f"{pair[0]}: {pair[1]}")
        return "{ " + ", ".join(result) + " }"


hashTable = TabelaHash()
hashTable.inserir("key1", "value1")
hashTable.inserir("key2", "value2")
hashTable.inserir("key3", "value3")

print(hashTable.buscar("key2"))

hashTable.remover("key2")

print(hashTable)
