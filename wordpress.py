import requests


class WP:
    def __init__(self, blog_url, api_base="/wp-json/wp/v2/"):
        self.blog_url = blog_url
        self.api_url = blog_url + api_base

    def get_posts(self, params=None):
        # get all blog posts
        r = requests.get(self.api_url + "posts", params=params)
        return r.json()

    def get_post(self, post_id, params=None):
        # get a particular blog post
        r = requests.get(
            self.api_url + "posts/{}".format(post_id), params=params)
        return r.json()

    def get_categories(self, params=None):
        # get blog categories
        r = requests.get(
            self.api_url + "categories", params=params)
        return r.json()

    def get_tags(self, params=None):
        # get blog tags
        r = requests.get(
            self.api_url + "tags", params=params)
        return r.json()


wp = WP("https://blog.cleanpick.green")
# print(wp.get_posts())
# print(wp.get_post(1))
# print(wp.get_categories())
print(wp.get_tags())
