#! python3
# An insecure password locker program
passwords = {'school': 'abc123',
            'blog': 'cat45'
            'luggage': '67576'}

 import sys
 if len(sys.argv) < 2:
     print('Usage: python pw.py [account] - copy account password')
     sys.exit()
account = sys.argv[1]   # first command line arg is the acct name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
