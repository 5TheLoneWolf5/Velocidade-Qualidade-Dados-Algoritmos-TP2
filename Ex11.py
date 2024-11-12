class FilaAtendimento:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.start = 0
        self.end = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def adicionar_cliente(self, nome):

        if self.is_full():
            print("Fila cheia.")
            return

        self.items[self.end] = nome
        self.end += 1
        self.size += 1

        if self.end == self.capacity:
            self.end = 0
        
    def atender_cliente(self):
        if self.is_empty():
            print("Fila vazia.")
            return

        item = self.items[self.start]
        self.items[self.start] = None
        self.start += 1
        self.size -= 1

        if self.start == self.capacity:
            self.start = 0

        print(item)
        return item

    def peek(self):
        if self.is_empty():
            print("Fila vazia")
            return None
        return self.items[self.start]
    
    def tamanho_file(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("Fila vazia.")
            return
        else:
            for i in range(self.size):
                index = (self.start + i) % self.capacity
                print(self.items[index], end=" ")
            print()


queue = FilaAtendimento(5)

queue.adicionar_cliente("Cliente 1")
queue.adicionar_cliente("Cliente 2")
queue.adicionar_cliente("Cliente 3")
queue.adicionar_cliente("Cliente 4")
queue.adicionar_cliente("Cliente 5")

print(queue.peek())

queue.atender_cliente()

queue.display()
