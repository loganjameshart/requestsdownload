import requests

def download(url: str, name: str, filetype: str):
	with open(fr"{name}.{filetype}", "wb") as f:
		r = requests.get(url, stream=True)
		r.raise_for_status()
		f.write(r.content)
