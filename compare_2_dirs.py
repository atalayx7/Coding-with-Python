import os
path = ''
path2 = ''


def fnk(path):
    files = []
    programs = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(file))
    for i in files:
        programs.append(i.split('\\')[-1])
    return programs


x = fnk(path)
y = fnk(path2)

for i in x:
    if not i in y:
        print(i)
