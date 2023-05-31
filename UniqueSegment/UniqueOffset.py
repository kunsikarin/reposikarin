import os

file = input('Enter File Name Either in Realative Path or Absolute Path: ')

def checkfname(fname, ext):
    if os.path.exists(fname + ext):
        count=1
        while os.path.exists(fname + str(count) + ext):
            count+=1
        return fname + str(count) + ext
    else:
        return fname + ext
    
with open(file, 'r') as logfile:
    seglst = []
    for log in logfile:
        loglst = log.split(' ')
        if loglst[0] == 'Caused':
            loglst[-1] = loglst[-1].strip()
            seglst.append(loglst[3:])
            
    uniqseglst = []
    con = []
    for seg in seglst:
        if seg not in con:
            con.append(seg)
            seg = ' '.join(seg)
            uniqseglst.append(seg)
    
    fname = checkfname('IllegalOffset', '.txt')
    
    i=1
    with open(fname, 'a+') as wfile:
        wfile.write('Unique IllegalOffsetException as follows.\n')
        wfile.write('\n')
        for ln in uniqseglst:
            ln = str(i)+'. '+ln+'\n'
            wfile.write(ln)
            i=+1

print('\n')
with open(fname, 'r') as rfile: print(rfile.read())    
print('File Generated: '+fname)