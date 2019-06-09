import os
from sub_module1.sub1 import sub_fun1
import sub_module2.sub2
if __name__ == '__main__':
    sub_fun1()
    sub_module2.sub2.sub_fun2()
    print ('finished')
    print (os.path)
    print (os.path.dirname)
    print (os.getcwd())
