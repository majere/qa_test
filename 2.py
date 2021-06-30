import hashlib
import os
import sys

try:
    input_file = sys.argv[1]
    path_to_check = sys.argv[2]
except IndexError:
    print('Wrong param')
    exit()

error = False

with open(input_file, 'r') as f:
    text = f.read().splitlines()
for line in text:
    tmp = line.split(' ')
    try:
        file = tmp[0]
        mtd = tmp[1]
        hsh = tmp[2]
    except IndexError:
        if line != '':
            print(f'Error in line "{line}"')
            error = True

    full_path = os.path.join(path_to_check, file)

    if os.path.isfile(full_path):
        f = open(full_path, 'rb')
        content = f.read()

        if mtd == 'md5':
            md5 = hashlib.md5(content)
            file_hash = md5.hexdigest()
        elif mtd == 'sha1':
            sha1 = hashlib.sha1(content)
            file_hash = sha1.hexdigest()
        elif mtd == 'sha256':
            sha256 = hashlib.sha256(content)
            file_hash = sha256.hexdigest()
        else:
            print(f'{file} unknown hash type {hsh}')

        if file_hash == hsh:
            print(file, 'OK')
        else:
            print(file, 'FAIL')

    else:
        if line != '' and not error:
            print(file, 'NOT FOUND')
