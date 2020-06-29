import config
import requests

apiHome = config.apiHome
token = "token " + config.token

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
    print()
    print()


def showlanguage(languages_url):
    response = requests.get(languages_url,
                            headers={"Authorization": token})
    langs = response.json()
    print(langs)
    for lang in langs:
        langDict[lang] = langDict.get(lang, 0) + langs[lang]


if __name__ == "__main__":
    if (apiHome == ""):
        print("Please set api home at config.py")
        exit()

    if (token == ""):
        print("Please set access token at config.py")
        exit()

    if config.serverType == "github":
        apiAllorgs = apiHome + "/user/orgs"
    else:
        apiAllorgs = apiHome + "/organizations"

    response = requests.get(apiAllorgs,
                            headers={"Authorization": token})
    orgs = response.json()
    for org in orgs:
        checkOrg(org)

    print(langDict)
    s = 0
    for lang in langDict:
        s = s + langDict[lang]
    print(s)
