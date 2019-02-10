'''
Day - 8
Link : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/

'''

#  Accepted Solution

entry = int(input())

phone_book = {}
for _ in range(entry):
    name, number = input().split()
    phone_book[name] = number

query_name = input()
while query_name:
    if query_name in phone_book:
        print(query_name, phone_book[query_name], sep='=')
    else:
        print("Not found")
    query_name = input()