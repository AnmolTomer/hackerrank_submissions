"""t = int(input())
list_words = []
odd_list = []
even_list = []
if (t < 0 or t > 10):
    exit()
else:
    for i in range(t):
        s1 = input()
        list_words.append(s1)
#print(list_words) #Got Hacker Rank list printed.
for i in range(len(list_words)):
    for j in range(len(list_words[i])):
        if j%2 != 0:
            odd_list.append(list_words[i][j])
        elif j%2 == 0:
            even_list.append(list_words[i][j])
    a = ''.join(odd_list)
    b = ''.join(even_list)
    c = print(a,b)
    even_list.clear()
    odd_list.clear()
"""

for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])
