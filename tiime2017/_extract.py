import re
pattern = re.compile(r'Session (\d+)')
with open('index.md') as fd:
    for l in fd.readlines():
        s = pattern.search(l)
        if s is not None:
            slink = s.group(0).replace(' ', '').replace('S', 's')
            print('* [' + l.rstrip().replace('### ', '').replace(' <', ': ').replace('>', '') + '](' + slink + '.md)')
