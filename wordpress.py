import requests


class WP:
    def __init__(self, blog_url, api_base="/wp-json/wp/v2/"):
        self.blog_url = blog_url
        self.api_url = blog_url + api_base

    def get_posts(self, params=None):
        # get all blog posts
        r = requests.get(self.api_url + "posts", params=params)
        return r.json()


wp = WP("https://blog.cleanpick.green")
print(wp.get_posts())
