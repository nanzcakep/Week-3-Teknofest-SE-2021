"""
Input: ["js", "js", "golang", "ruby", "ruby", "js", "js"]
Output:
golang: 1
ruby: 2
js: 4


Input: ["danu", "danu", "alif", "indra", "indra", "kurniadi", "indra"]

Output:
alif: 1
kurniadi: 1
danu: 2
indra: 3
"""



def totalmuncul(data):
    res = []
    for i in data:
        x = data.count(i)
        if x not in res:
                res.append(x)
                print(i + " :",x)



data = ["danu", "danu", "alif", "indra", "indra", "kurniadi", "indra"]
totalmuncul(data)