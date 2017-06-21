
class Minions:
    def __init__(self):
        self.round = 0
	self.storage = []

    def next_round(self):
        self.round += 1
        for x in self.storage:
            x.new_round()

    def spawn_minion(self):
        self.storage.append(Page())
        return len(self.storage)
 
    def assign(self, n, x):
        self.storage[n].assign(x)
    
    def get(self, n):
        return self.storage[n].get()

    def current_round(self):
        return self.round

    def size_of_horde(self):
        return len(self.storage)


class Page: 

    def __init__(self):
        self.values = range(2)
        self.is_set = False
        self.is_read = True # the data is initialized to have been read already so that in order to read, you must call next_round
       
    def assign(self, x):
        if self.is_set:
            raise Exception("FullHeadedMinionError: You have already assigned a value to this minion.")
            return
        self.value = x
        self.is_set = True
        self.is_read = True

    def get(self):
        if not self.is_set:
            raise Exception("EmptyHeadedMinionError: You haven't assigned a value to this minion.")
            return
        if self.is_read:
            raise Exception("ExhaustedMinionError: You already asked this minion for his value or assigned one to him this round.")
            return
        self.is_read = True
        return self.value

    def new_round(self):
        self.is_read = False







