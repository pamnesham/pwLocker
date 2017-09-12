#! python3
# An insecure password locker program
passwords = {'school': 'abc123',
            'blog': 'cat45',
            'luggage': '67576'}
import sys
import pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]   # first command line arg is the acct name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

# Create a batch file to run from 'run' window:
'''@py.exe C:\path_to_this_file\pw.py %*
@pause'''
