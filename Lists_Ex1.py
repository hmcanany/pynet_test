ip = raw_input('What is your IP Address?  ')
#ip = '10.2.1.1'
ip_Add = ip.split('.')
ip_Add[3] = 0

ip_binary = []
ip_binary.append(bin(int(ip_Add[0])))
ip_binary.append(bin(int(ip_Add[1])))
ip_binary.append(bin(int(ip_Add[2])))
ip_binary.append(bin(int(ip_Add[3])))

print "{:<12}{:<12}{:<12}{:<12}".format(*ip_Add)
print "{:<12}{:<12}{:<12}{:<12}".format(*ip_binary)
