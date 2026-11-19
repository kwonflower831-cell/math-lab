# -*- coding: utf-8 -*-
import subprocess, os

cwd = r'D:\사용자\math-lab'

def run(cmd):
    print('==> ' + cmd, flush=True)
    res = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, encoding='utf-8')
    if res.stdout:
        print(res.stdout.strip(), flush=True)
    if res.stderr:
        print('STDERR:', res.stderr.strip(), flush=True)
    return res.returncode

run('git init -b main')
run('git add .')
run('git commit -m "Initial commit: Intuitive Math Lab with 7 interactive visualizations"')
run('gh repo create kwonflower831-cell/math-lab --public --source=. --remote=origin --push')
