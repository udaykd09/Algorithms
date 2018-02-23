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

print(get_distinct_ips('patterns.log'))
print(get_phonenumbers('patterns.log'))
