import os
import sys
import getopt
import urllib.request
import json


BAIL = False

url = "https://api.github.com/repos/sigil-ebook/{}/releases/latest"

repos = {'sigil'                : 'sigil_ver',
         'sigil-user-guide'     : 'sigil_guide_ver', 
         'pageedit'             : 'pageedit_ver',
         'pageedit-user-guide'  : 'pageedit_guide_ver',
         'iconthemes'           : 'iconthemes_ver'
}

line_data = '{{% assign {} = "{}" %}}'


def get_remote_vers():
    global BAIL
    lines = []
    for r, v in repos.items():
        try: 
            j = json.loads(urllib.request.urlopen(url.format(r)).read())
            t = j['tag_name']
        except Exception:
            BAIL = True
            break
        lines.append(line_data.format(v,t))
    return lines

def get_local_ver(p):
    global BAIL
    c = ''
    if os.path.exists(p) and os.path.isfile(p):
        print(p)
        with open(p) as f:
            c = f.readlines()
            c = [x.strip() for x in c]
    else:
        BAIL = True
    return c

def main(argv):
    global BAIL
    path = ''
    try:
        opts, args = getopt.getopt(argv,"hp:",["path="])
    except getopt.GetoptError:
        print ('vers_update.py -p <path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('vers_update.py -p <path>')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
    remote = get_remote_vers()
    if BAIL:
        sys.exit(2)
    p = os.path.join(path, '_includes', 'remote_versions.html')
    local = get_local_ver(p)
    if BAIL:
        sys.exit(2)
    if not (remote == local):
        try:
            with open(p, 'w') as f:
                f.write('\n'.join(remote))
                f.write('\n')
        except Exception:
            sys.exit(2)
        print('Updates from remote versions')
    sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])