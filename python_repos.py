import requests

url = "http://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"{r.status_code}")

response_dict = r.json()
print(f"符合条件的个数{response_dict['total_count']}")
print(f"是否完成{not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"{len(repo_dicts)}")

for repo_dict in repo_dicts:
    print(f"{repo_dict['name']}")

