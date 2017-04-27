import argparse, random, json, requests 

parser = argparse.ArgumentParser()

parser.add_argument("--gh", help="Random access the Github API", nargs=1)
parser.add_argument("--ghl", help="Access the Github API", nargs=1)
parser.add_argument("-l", help="Access the Gitlab API", nargs=1)
args = parser.parse_args()


def github():

    userRepos = args.gh[0] + '/repos?'
    url = 'https://api.github.com/users/' + userRepos
    response = requests.get(url)

    response.raise_for_status()
    repoData = json.loads(response.text)

    d = repoData

    repoList = []

    for item in d:
        repoList.append(item["name"])

    print(random.choice(repoList))

def listGithub():

    userRepos = args.ghl[0] + '/repos?'
    url = 'https://api.github.com/users/' + userRepos
    response = requests.get(url)

    response.raise_for_status()
    repoData = json.loads(response.text)

    d = repoData

    repoList = []

    for item in d:
        repoList.append(item["name"])

    for item in repoList:
        print(item)

        
def gitlab():
    return


def menuInit():
    if args.gh:
        github()

    elif args.l:
        gitlab()

    elif args.ghl:
        listGithub()

    else:
        print("Oooops")

menuInit()

