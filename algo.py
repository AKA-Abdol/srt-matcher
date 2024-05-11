en = [[4, 5], [8, 14], [16, 17], [17, 19]]
fa = [[1, 5], [4, 6], [8, 10], [10, 12], [12, 14], [16, 19]]
men = []
mfa = []
ien = ifa = 0
while ien < len(en) and ifa < len(fa):
    if en[ien][0] < fa[ifa][0]:
        ien += 1
    elif en[ien][0] > fa[ifa][0]:
        ifa += 1
    else:
        if en[ien][1] - en[ien][0] > fa[ifa][1] - fa[ifa][0]:
            men.append([ien])
            temp = []
            while ifa < len(fa) and fa[ifa][1] <= en[ien][1]:
                temp.append(ifa)
                ifa += 1
            mfa.append(temp)
        else:
            mfa.append([ifa])
            temp = []
            while ien < len(en) and fa[ifa][1] >= en[ien][1]:
                temp.append(ien)
                ien += 1
            men.append(temp)
print(men, mfa)