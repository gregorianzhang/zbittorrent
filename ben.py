#-*- coding:utf-8 -*-

class ben(object):
    def __init__(self):
        print "aaa"

    def encode(self, data):
        print data

    def decode(self, data):
        print data

    def run(self):
        pass

    def ben_string(self,data):
        n = data.find(":")
        num = int(data[:n])
        return (data[n+1:n+num+1],n+num+1)

    def ben_num(self,data):
        num = ""
        for x in data[1:]:
            if x != 'e':
                num += x
            else:
                return(num,len(num)+2)

    def ben_dict(self,data):
        dic = {}
        

if __name__ == "__main__":
    a = ben()
    x="2:aa2:ab2:ac13:qazxswedcvf5r"
    c="i233334ei32e"
    d="i-32e"
    #a.decode(x)
    print a.ben_string(x)
    print a.ben_num(c)
    print a.ben_num(d)
