import requests
import key

url="https://api.yelp.com/v3/businesses/search"
header={
    "Authorization":"Bearer " + key.api_key
}
params={
    "term":"barber",
    "location":"NYC"
}
response = requests.get(url,headers=header,params=params) 
# print(response.text)

businesses= response.json()["businesses"]
# # print(businesses)
# for business in businesses:
#     print(business['name'])
name = [business["name"]
        for  business in businesses if business["rating"] > 4.5]
print(name)