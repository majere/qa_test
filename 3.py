import time
import os
from psutil import virtual_memory


class Case:
    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    @staticmethod
    def prep():
        print('prep')
        return True

    @staticmethod
    def run():
        print('run')
        return True

    @staticmethod
    def clean_up():
        print('clean_up')
        return True

    def execute(self):
        if self.prep():
            if self.run():
                if self.clean_up():
                    print('TEST OK')
                else:
                    print('clean_up return False')
            else:
                print('run return False')
        else:
            print('prep return False')


class Test1(Case):
    @staticmethod
    def prep():
        time_now = int(time.time())
        if time_now % 2 == 0:
            return True
        else:
            return False

    @staticmethod
    def run():
        home = os.path.expanduser("~")
        for el in os.listdir(home):
            print(el)
        return True


class Test2(Case):
    @staticmethod
    def prep():
        ram = virtual_memory()[0]
        gb = 1073741824
        if ram >= gb:
            return True
        else:
            return False

    @staticmethod
    def run():
        kb = 1048575
        with open('test', 'wb') as f:
            f.write(os.urandom(kb))
        return True

    @staticmethod
    def clean_up():
        os.remove("test")
        return True


t1 = Test1(1, 'test_1')
t1.execute()

t2 = Test2(2, 'test_2')
t2.execute()


