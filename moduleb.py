import init, functools
from birdseye import eye


@eye
def test_linkage():

    init.myVar += 5

    print(init.myVar)



test_linkage()

#print(type(test_linkage))

#L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']

#print(functools.reduce( (lambda x,y:x+y), L))

#print(5 % 0)