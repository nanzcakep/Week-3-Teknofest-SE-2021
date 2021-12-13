"""
Test Case:
Input: “76523752”
Output: [6, 3]
Input: “1122”
Output: []

"""

def onlyone(number):
        pecah = []
        for i in number:
            x = number.count(i)
            if x <= 1:
                pecah.append(int(i))
        if pecah >= pecah:
              print(pecah)


print('Masukan nomor kamu:')
nomer = input()

onlyone(nomer)