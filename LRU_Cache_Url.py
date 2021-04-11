

class LRU:
    def __init__(self, cache):  # result
        self.cache = []
        self.cache.append(cache)

    def Set(self, URL):
        if(len(self.cache) == 2):
            print('Cache is full, Clearing LRU (Least recent used)')
            self.cache.pop(0)
            self.cache.append(URL)
            return("Added : {URL}").format()

    def get(self):
        if (len(self.cache) == 0):
            print("cache is empty ")
        else:
            return self.cache.pop(0)

    def display(self):
        return self.cache


def main():
    from LRU_Test import LRUTest

    print("enter an input of URL for LRU")
    v = str(input())
    result = LRUTest(v)
    a = True

    print("press 1 for testing set method")
    print("press 2 for testing get method")
    print("enter your choice")

    y = int(input())

    while(a):
        if(y == 1):
            result.testSet()

        elif(y == 2):
            result.testGet()

        else:
            print("invalid input")
            a = False


if __name__ == "__main__":
    main()
