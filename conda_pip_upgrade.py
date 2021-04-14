from subprocess import call

call('pip install --upgrade pip',shell=True)
call('pip freeze — local | grep -v ‘^\-e’ | cut -d = -f 1 | xargs -n1 pip install -U',shell=True)

call('pip3 install --upgrade pip',shell=True)
call('pip3 freeze — local | grep -v ‘^\-e’ | cut -d = -f 1 | xargs -n1 pip install -U',shell=True)

call('conda update --all',shell=True)
