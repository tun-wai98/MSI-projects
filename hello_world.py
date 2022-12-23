class Quee(object):
    def __init__(self):
            self.q = []
    def isempty(self):
            return len(self.q) == 0
    def get_len(self):
            return len(self.q)
    def enque(self,elem):
            self.q.insert(0,elem)
    def deque(self):
            return self.q.pop()
            
def game(ppl,num):
    qr = Quee()
    for i in ppl:
        qr.enque(i)
    while qr.get_len() !=0:
        i = 0
        try:
            while i != num:
                qr.enque(qr.deque())
                i+=1
            
        except ValueError:
	        print ("error")
        qr.deque()
        if qr.get_len() == 1:
            return qr.deque()
	



print (game(["Bill","David","Susan","Jane","Kent","Brad"],7))