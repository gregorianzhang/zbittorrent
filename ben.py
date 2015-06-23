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
        print "ben_string %s" % data
        return (data[n+1:n+num+1],n+num+1)

    def ben_num(self,data):
        num = ""
        for x in data[1:]:
            if x != 'e':
                num += x
            else:
                print "ben_num %s" % data
                return(num,len(num)+2)

    def ben_dict(self,data):
        dict1 = {}
        n=1
	print "data[%s] is value %s" % (n,data)
	while data[n] != 'e':

            print "dict1 %r" % dict1
            print "data[%s] is value %s" % (n,data[n])
            print "*"*40
            #key
            if data[n].isdigit():
                (z,i) = self.ben_string(data[n:])
		print z,i
            else:
                if data[n] == 'd':
                   (z,i) = self.ben_dict(data[n:])
                if data[n] == 'i':
                   (z,i) = self.ben_num(data[n:])

                if data[n] == 'l':
                    (z,i) = self.ben_list(data[n:])

            print "z %r i %r" % (z,i)    
            print "=" *40
            n += i
            #value
            print "data[%s] is value %s" % (n,data[n])
            if data[n].isdigit():
		(v,t) = self.ben_string(data[n:])
            else:
                if data[n] == 'd':
                    (v,t) = self.ben_dict(data[n:])
                if data[n] == 'i':
                    (v,t) = self.ben_num(data[n:])

                if data[n] == 'l':
                    (v,t) = self.ben_list(data[n:])
            n += t

            print "z %s,v %s" % (z,v)
            print "+" *40
            dict1[z]=v


        print "ben_dict %s" % data
        return (dict1,n+1)

    def ben_list(self,data):
        list1 = []
        n=1
	print "data[%s] is value %s" % (n,data)
	while data[n] != 'e':
            print "list1 %r" % list1
            print "data[%s] is value %s" % (n,data[n])
            #key
            if data[n].isdigit():
                (z,i) = self.ben_string(data[n:])
		print z,i
            else:
                if data[n] == 'i':
                   (z,i) = self.ben_num(data[n:])
                if data[n] == 'd':
                   (z,i) = self.ben_dict(data[n:])
                if data[n] == 'l':
                   (z,i) = self.ben_list(data[n:])
            print "z %r i %r" % (z,i)
            print "1" *40
            n += i
            list1.append(z)

        print "ben_list %s" % data
	return (list1,n+1)


if __name__ == "__main__":
    a = ben()
    x="2:aa2:ab2:ac13:qazxswedcvf5r"
    c="i233334ei32e"
    d="i-32e"
    tt="d2:aa2:abe"
    #td="d4:aaaai333e2:445:abcde4:xyzzi4356ee"
    td="d2:ee2:ee3:eeell3:abc3:xyz3:ttte2:332:442:44ee"
    tl="d2:aa2:xy3:qwel2:bb6:bbb.coee"

    with open('b.torrent') as ft:
        data=ft.read()
        print a.ben_dict(data)
    #with open('c.torrent') as ft:
    #    data=ft.read()
    #    print a.ben_dict(data)

    #a.decode(x)
#    print a.ben_string(x)
#    print a.ben_num(c)
#    print a.ben_num(d)
#    print "*" * 30
#    print a.ben_dict(tt)
    #print a.ben_dict(td)
    #print a.ben_dict(tl)
