from time import sleep
import emoji


print('O show de fogos de artificio começa em:')

for c in range(10, -1, -1):
    print(c)
    sleep(1)
for f in range(0, 15):
    print(emoji.emojize('\033[46m' + ':fireworks:' + '\033[m', language='alias'), end=' ')
    sleep(0.3)
