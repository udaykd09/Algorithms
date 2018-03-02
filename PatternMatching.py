import re


def get_distinct_ips(myfile):
    list = []
    with open(myfile) as f:
        for line in f:
            l = re.findall(r"(?:\d{1,3}\.){3}\d{1,3}", line)
            if l:
                list += l
    f.close()
    return list

def get_phonenumbers(myfile):
    list = []
    pattern = r'(?:\d{3}-|\(\d{3}\) )\d{3}-\d{4}'
    with open(myfile) as f:
        for line in f:
            l = re.findall(pattern, line)
            if l:
                list += l
    return list


s = "proc: warning 349 com.service.Register_Users: unable to connect"
pattern = r'proc: warning [0-9]+ [a-zA-Z_\.]+:.+'
print re.findall(pattern, s)


def find_second_largest(path):
    import sys
    max_1 = max_2 = -sys.maxint
    with open(path) as f:
        for line in f:
            n = int(line)
            if n > max_2:
                if n >= max_1:
                    max_1, max_2 = n, max_1
                else:
                    max_2 = n
    return max_2

#print(get_distinct_ips('patterns.log'))
#print(get_phonenumbers('patterns.log'))
#print(find_second_largest('n.log'))