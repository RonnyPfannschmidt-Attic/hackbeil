#!/usr/bin/python

import subprocess
import py

config_file = py.path.local(__file__).dirpath().join('example.ini')
config = py.iniconfig.IniConfig(config_file)
config_dir = config_file.dirpath()

bin = config_dir.dirpath().join('bin')

svnrepo = config['workload']['repo']
replay = str(config_dir.join(config['workload']['replay']))
converts = str(config_dir.join(config['workload']['converts']))
target = str(config_dir.join(config['workload']['target']))
authormap = str(config_dir.join(config['workload']['authormap']))


def call(cmd, *args):
    cmd = str(bin/cmd)
    subprocess.check_call(['python', cmd] + list(args))



import sys
args = sys.argv[1:]
if 'replay' in args:
    pass

if 'convert' in args:
    call('convert-via-replay.py', replay, svnrepo ,converts, authormap)
if 'combine' in args:
    call('replay-hg-history.py', replay, converts, target)