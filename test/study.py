import re

content = ''


class MyWith(object):
    def __enter__(self):
        print("Enter with")
        return self  # 返回对象给as后的变量

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # 关闭资源等
        if exc_traceback is None:
            print("Exited without Exception")
            return True
        else:
            print("Exited with Exception")
            return False


def test_with():
    with MyWith() as my_with:
        print("running my_with")
    print("------分割线-----")
    with MyWith() as my_with:
        print("running before Exception")
        raise Exception
        print("running after Exception")


if __name__ == '__main__':
    test_with()
