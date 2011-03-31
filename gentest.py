import sys
from random import randint

def _point():
    print "%d %d %d" % (randint(0,1000), randint(0,1000), randint(0,1000))

def _bombs(T=50):
    print T
    for t in range(50):
        N = randint(1,200)
        print N
        for bomb in range(N):
            _point()


if __name__ == "__main__":
    _bombs(1)
