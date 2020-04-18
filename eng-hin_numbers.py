inp = input("Enter the number: ")

inp_len = len(inp)
ans = ""
hin_num = [u'\u0966',u'\u0967',u'\u0968',u'\u0969',u'\u096A',u'\u096B',u'\u096C',u'\u096D',u'\u096E',u'\u096F']

for i in range(inp_len):
	ans += hin_num[int(inp[i])]

print("The number in Hindi is " + ans)


