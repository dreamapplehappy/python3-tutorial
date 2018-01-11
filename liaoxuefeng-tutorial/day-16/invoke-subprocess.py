import subprocess
# print('invoke a subprocess')
# r = subprocess.call(['nslookup', 'open.weixin.qq.com'])
# r = subprocess.call(['touch', 'README.md'])
# print('exit code', r)

print('------\n')

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('exit code:', p.returncode)