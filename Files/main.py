import os
from datetime import datetime


def pushToRepo(branch, directory, message):
    os.chdir(directory)
    os.system('git branch -M ' + branch)
    os.system('git add .')
    os.system('git commit -m "' + message + '"')
    os.system('git push -u origin ' + branch)


leetcode = "C:\\Users\\Aditya\\Leet Code Solutions"
codeforces = "C:\\Users\\Aditya\\Code Forces Solutions"
codechef = "C:\\Users\\Aditya\\Code Chef Solutions"
cses = "C:\\Users\\Aditya\\CSES Solutionss"

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

today = datetime.now()
day = today.day
month = months[today.month - 1]
year = today.year
time = today.strftime("%H:%M:%S")
message = f'{day} {month} {year} - {time}'

pushToRepo("main", leetcode, message)
pushToRepo("main", codeforces, message)
pushToRepo("main", cses, message)
pushToRepo("main", codechef, message)
