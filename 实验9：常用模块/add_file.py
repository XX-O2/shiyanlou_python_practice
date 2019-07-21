import os

os.mkdir('/home/shiyanlou/syl')
filename_A = '/home/shiyanlou/syl/A'
filename_B = '/home/shiyanlou/syl/B'
filename_C = '/home/shiyanlou/syl/C'
filename_other = '__init__.py'
filename_D = os.path.join('/home/shiyanlou/syl',filename_other)
A_file = os.path.join(filename_A,filename_other)
B_file = os.path.join(filename_B,filename_other)
C_file = os.path.join(filename_C,filename_other)
os.mkdir(filename_A)
os.mkdir(filename_B)
os.mkdir(filename_C)
os.mkdir(filename_D)
os.mkdir(A_file)
os.mkdir(B_file)
os.mkdir(C_file)
