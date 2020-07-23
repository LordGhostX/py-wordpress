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

    def get_pages(self, params=None):
        # get all blog page
        r = requests.get(self.api_url + "pages", params=params)
        return r.json()

    def get_page(self, page_id, params=None):
        # get a particular blog page
        r = requests.get(
            self.api_url + "pages/{}".format(page_id), params=params)
        return r.json()

    def get_comments(self, post_id=None, params=None):
        # get all comments
        if post_id:
            r = requests.get(
                self.api_url + "comments/{}".format(post_id), params=params)
        else:
            r = requests.get(self.api_url + "comments", params=params)
        return r.json()


wp = WP("https://blog.cleanpick.green")
# print(wp.get_posts())
# print(wp.get_post(1))
# print(wp.get_categories())
# print(wp.get_tags())
# print(wp.get_pages())
# print(wp.get_page(1))
print(wp.get_comments())
print(wp.get_comments(1))
