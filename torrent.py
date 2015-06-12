torrent="d3:bar4:spam3:fooi42ee"

tt="3:bar4:spam"
torrentdict={"bar": "spam", "foo": 42}

key={}

def decode_string(x):
    ss= x.index(':',0)
    num = int(x[0:ss])
    print x[ss+1:ss+1+num]



def decode_dict(x):
    print "x is %s" % x
    i =0
    b=""
    while x[i] != 'e':
        b+=x[i]
        i+=1
    print "dict %r" % b

decode_dict(torrent)
decode_string(tt)
