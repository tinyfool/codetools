import requests

token = ""
apiHome = ""

langDict = {}

def checkOrg(org):

    print(org["login"])
    print("========================")
    apiOrgrepos = apiHome + "/orgs/" + org["login"] + "/repos"
    response = requests.get(apiOrgrepos,
                            headers={"Authorization": token})
    repos = response.json()
    for repo in repos:
        print(repo["full_name"])
        showlanguage(repo["languages_url"])

def showlanguage(languages_url):


    response = requests.get(languages_url,
                            headers={"Authorization": token})
    langs = response.json()
    print(langs)
    for lang in langs:
        langDict[lang] = langDict.get(lang,0) + langs[lang]

apiAllorgs = apiHome + "/user/orgs"
response = requests.get(apiAllorgs,
                        headers={"Authorization": token})
orgs = response.json()
for org in orgs:
    checkOrg(org)

print(langDict)
s=0
for lang in langDict:
    s = s + langDict[lang]
print (s)