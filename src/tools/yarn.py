
import os
import sys


def yarn_shell(code_path):

    os.chdir(code_path)
    os.system('yarn')
    os.system('npm run build')
    r = os.popen('npm run build')  # 执行该命令
    info = r.readlines()  # 读取命令行的输出到一个list
    for line in info:  # 按行遍历
        line = line.strip('\r\n')
        print(line)


if __name__ == "__main__":
    print(sys.argv)
    code_path = str(sys.argv[1])
    yarn_shell(code_path)