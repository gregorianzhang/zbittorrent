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
        dict1 = {}
        n=1
	print "data[%s] is value %s" % (n,data)
	while data[n] != 'e':
	    print "dict1 %r" % dict1
	    print "data[%s] is value %s" % (n,data[n])
	    #key
	    if data[n].isdigit():
	        (z,i) = self.ben_string(data[n:])
		print z,i
	    else:
	    	if data[n] == 'i':
	            (z,i) = self.ben_num(data[n:])
	    print "z %r i %r" % (z,i)    
	    print "1" *40
	    n += i
	    #value
	    print "data[%s] is value %s" % (n,data[n])
	    if data[n].isdigit():
		(v,t) = self.ben_string(data[n:])
	    else:
	    	if data[n] == 'i':
		    (v,t) = self.ben_num(data[n:])
	    n += t
	
	    print "z %s,v %s" % (z,v)	
	    dict1[z]=v

	    #if n > num:
#		return dict1
		
	return dict1
	

if __name__ == "__main__":
    a = ben()
    x="2:aa2:ab2:ac13:qazxswedcvf5r"
    c="i233334ei32e"
    d="i-32e"
    tt="d2:aa2:abe"
    td="d4:aaaai333e2:445:abcde4:xyzzi4356ee"
    #a.decode(x)
    print a.ben_string(x)
    print a.ben_num(c)
    print a.ben_num(d)
    print "*" * 30
    print a.ben_dict(tt)
    print a.ben_dict(td)
