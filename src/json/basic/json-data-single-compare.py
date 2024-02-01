# import libraries
import json

# json file paths
myjson1_json_file = "[filepath]/myjson1.json"

myjson2_json_file = "[filepath]/myjson2.json"


# file open for json_file 1
file = open(myjson1_json_file)

data = json.load(file)

file.close()

# file open for json_file 2
file = open(myjson2_json_file)

data2 = json.load(file)

file.close()


# url lists

url_list1_myjson1 = []

url_list2_myjson2 = []


# counter var (to count loop iterations in case of convenience)

count = 0

# print(data['images'])

for item in data['images']:

#    name = item['name']
#    uid = item['uid']
    uri = item['uri']
    uri = uri.split('?')
    uri = uri[0]
    url_list1_myjson1.append(uri)



for item2 in data2['relevantImages']:

#    name = item['name']
#    uid = item['uid']
    uri2 = item2['originalImageURL']
    uri2 = uri2.split('?')
    uri2 = uri2[0]
    url_list2_myjson2.append(uri2)



# final for loop to check and compare both values from list

# currently omitted

# shortcut method
    
print(sorted(url_list1_myjson1)==sorted(url_list2_myjson2))


# Repository Owner: https://github.com/dasabhijeet
# Date: 01 February 2024
