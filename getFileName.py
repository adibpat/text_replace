import os
import sys

def pattern_match_files(path,pattern_from):
    match_file = "./" + "pattern_match.txt"
    os.chdir(path)
    command = "egrep -rl " + pattern_from + " *>" + match_file
    os.system(command)

def delete_match_file():
    os.system('rm ./pattern_match.txt')


if __name__ == '__main__':
    if (len(sys.argv)!=3):
        print "Insufficient Arguments"
    else:
        path = sys.argv[1]
        pattern_from = sys.argc[2]
        pattern_match_files(path,pattern_from)

