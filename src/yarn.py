
import os
import sys


def yarn_shell(code_path):
    os.system('rm -f ' + '/home/data/code/fabric/src/logs/front.log')
    os.chdir(code_path)
    yarn_line = os.popen('yarn')  # 执行该命令
    info = yarn_line.readlines()  # 读取命令行的输出到一个list
    for line in info:  # 按行遍历
        line = line.strip('\r\n')
        with open("/home/data/code/fabric/src/logs/front.log", "a") as f:
            line = '[yarn]->' + line
            f.write(line + '\n')
    npm_line = os.popen('npm run build')
    info = npm_line.readlines()  # 读取命令行的输出到一个list
    for line in info:  # 按行遍历
        line = line.strip('\r\n')
        with open("/home/data/code/fabric/src/logs/front.log", "a") as f:
            line = '[npm]->' + line
            f.write(line + '\n')


if __name__ == "__main__":
    print(sys.argv)
    code_path = str(sys.argv[1])
    yarn_shell(code_path)