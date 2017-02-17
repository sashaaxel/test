
import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
a = r.text

while a[0]+a[1] != 'We':
    p =requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+a)
    print(p.text)
    a = p.text
    l = 1

