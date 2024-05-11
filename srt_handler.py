import pysrt as srt
import pandas as pd

# consider this threshold may fail in some test cases, we should test more than one and change code a little bit
THRESHOLD = 1

def less_than(t1, t2):
    if (t1 > t2):
        return False
    return (t2 - t1).seconds > THRESHOLD


def less_than_equal(t1, t2):
    if (t1 > t2):
        return (t1 - t2).seconds < THRESHOLD
    return True


subs_en = srt.open(
    './data/Forrest Gump 1994 BRrip 720p x264.srt')  # .slice(ends_before={'minutes': 10})
subs_fa = srt.open('./data/fa_srt.srt')  # .slice(ends_before={'minutes': 10})

# use below code to fit first match of srt binding, others going to be match automatic
# subs_fa.shift(seconds = -5)


en = subs_en
fa = subs_fa
men = []
mfa = []
ien = ifa = 0
while ien < len(en) and ifa < len(fa):
    if less_than(en[ien].start, fa[ifa].start):
        ien += 1
    elif less_than(fa[ifa].start, en[ien].start):
        ifa += 1
    else:
        if en[ien].duration > fa[ifa].duration:
            men.append([en[ien].text])
            temp = []
            while ifa < len(fa) and less_than_equal(fa[ifa].end, en[ien].end):
                temp.append(fa[ifa].text)
                ifa += 1
            ien += 1
            mfa.append(temp)
        else:
            mfa.append([fa[ifa].text])
            temp = []
            while ien < len(en) and less_than_equal(en[ien].end, fa[ifa].end):
                temp.append(en[ien].text)
                ien += 1
            ifa += 1
            men.append(temp)

for i in range(len(men)):
    men[i] = ' '.join(men[i])

for i in range(len(mfa)):
    mfa[i] = ' '.join(mfa[i])

df = pd.DataFrame({'en': men, 'fa': mfa})
df.to_csv('./out/forres_gump.csv', index = False)
