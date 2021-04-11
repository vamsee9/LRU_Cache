from LRU_Cache_Url import LRU

class LRUTest(LRU):

    def __init__(self, URL):
        self.URL=URL
        
    def testSet(self):
        
        k=f"Added : {self.URL}"
        d=LRU("www.google.com")
        assert k == d.Set("www.Facebook.com"),"Testing Successful for SET method"

    def testGet(self):
        j=self.URL
        a=LRU(j)
        i=a.get()
        assert j != i,"Testing Successful for GET method"