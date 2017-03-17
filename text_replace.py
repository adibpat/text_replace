import sys
import getFileName

def text_replace(path, pattern_from, pattern_to):

    getFileName.pattern_match_files(path,pattern_from)

    file_name = './pattern_match.txt'

    with open(file_name,'r') as fp:
        lines = fp.readlines()
        for line in lines:
            line = line[:-1]
            with open(line,'r') as file:
                old_data = file.read()
                file.close()
            new_data = old_data.replace(pattern_from,pattern_to)
            with open(line,'w') as file:
                file.write(new_data)
                file.close()
        fp.close()

    getFileName.delete_match_file()


if (__name__ == '__main__'):
    count = len(sys.argv)
    if count < 4:
        print "Insufficient number of arguments"
    else:
        path = sys.argv[1]
        pattern_from = sys.argv[2]
        pattern_to = sys.argv[3]
        text_replace(path,pattern_from,pattern_to)