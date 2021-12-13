"""
Test Case:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Penjelasan:Angkanya ada di index 1 and 3 yang mana jika dijumlahkan sesuai dengan target => 2 + 4 = 6
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Penjelasan: Angkanya ada di index 0 and 2 yang mana jika dijumlahkan sesuai dengan target => 2 + 9 = 11
"""
def penjumlahan(nomer,target):
    pecah = []
    for i in nomer:
        for j in nomer:
            if j + i == target and j / i != 1:
                test = nomer.index(i)
                pecah.append(test)
                if test == max(pecah)!=min(pecah):
                    print(pecah)




nomor = [2, 5, 9, 11] #target 11 , [0, 2]
target = 11 #2 + 9

penjumlahan(nomor,target)
            



    


