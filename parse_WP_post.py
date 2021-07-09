import requests
import json

response = requests.get('http://54.193.156.214/blog/wp-json/wp/v2/posts/5')

if response.status_code == 200:
    res = (json.loads(response.text))
    title = (res['title']['rendered'])
    blog_post = (res['content']['rendered'])
    print(blog_post)

