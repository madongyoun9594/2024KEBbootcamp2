# Open closed principle
def test(f):
    """
    데코레이터 함수, 함수 시작하면 start 출력,, 함수 끝나면 end 출력
    :param f: function
    :return: closure function
    """
    def test_inner(*args, **kwargs):
        print('start')
        # result = f(*args, **kwargs)
        f()
        print('end')
        # return result
    return test_inner
@test
def greeting():
    print('hello')

greeting()


