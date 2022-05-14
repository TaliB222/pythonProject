aLsit = [100, 200, 300, 400, 500]
aLsit=aLsit[::-1]

#aLsit = sorted(aLsit, reverse=True)
print(aLsit)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
resList = list(filter(None, list1))
#list1.remove("")
#print(list1)
print(resList)

#Add item 7000 after 6000 in the following Python List:

list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list2[2][2].append(7000)
print(list2)

list_1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list_2 = ["h", "i", "j"]
list_1[2][1][2].extend(list_2)
print (list_1)

LIst = [5, 10, 15, 20, 25, 50, 20]
index= LIst.index(20)
LIst.insert(LIst.index(20), 200)
#LIst[index]=200
print(LIst)


#Exercise 1: Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
sampleDict = dict(zip(keys, values))
print(sampleDict)
#Exercise 2: Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)


#Exercise 3: Access the value of key ‘history’ from the below dict
sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}
print(sampleDict['class']['student']['marks']['history'])

#Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

resDict = dict.fromkeys(employees, defaults)
print(resDict)
print(resDict["Kelly"])
#Exercise 5: Create a new dictionary by extracting the following keys from a below dictionary
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)

#Exercise 6: Delete set of keys from a dictionary
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]
sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}

print(sampleDict)

#Exercise 7: Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(200 in sampleDict.values())
#Exercise 8: Rename key city to location in the following dictionary
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sampleDict['location'] = sampleDict.pop('city')
print(sampleDict)

#Exercise 9: Get the key of a minimum value from the following dictionary
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sampleDict, key=sampleDict.get))

#Exercise 10: Change Brad’s salary to 8500 from a given Python dictionary
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict['emp3']['salary'] = 8500
print(sampleDict)

l=[2,4,6]
m=l*3
print(m)