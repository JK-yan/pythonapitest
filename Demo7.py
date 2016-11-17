import nose


def setup():
    print('function setup')


def Testfunction1():
    print('testfybction1')
    assert True


def Testfunction2():
    print('testfybction2')
    assert True


def tearDown():
    print('function tearDown')


if __name__ == '__main__':
    nose.runmodule()
