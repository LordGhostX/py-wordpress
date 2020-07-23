import requests


class WP:
    def __init__(self, blog_url, api_base="/wp-json/wp/v2/"):
        self.blog_url = blog_url
        self.api_url = blog_url + api_base

    def get_posts(self, post_id=None, params=None):
        # get all blog posts
        if post_id:
            r = requests.get(
                self.api_url + "posts/{}".format(post_id), data=params)
        else:
            r = requests.get(self.api_url + "posts", data=params)
        return r.json()

    def get_categories(self, params=None):
        # get blog categories
        r = requests.get(
            self.api_url + "categories", data=params)
        return r.json()

    def get_tags(self, params=None):
        # get blog tags
        r = requests.get(
            self.api_url + "tags", data=params)
        return r.json()

    def get_pages(self, page_id=None, params=None):
        # get blog pages
        if page_id:
            r = requests.get(
                self.api_url + "pages/{}".format(page_id), data=params)
        else:
            r = requests.get(self.api_url + "pages", data=params)
        return r.json()

    def get_comments(self, post_id=None, params=None):
        # get all comments
        if post_id:
            r = requests.get(
                self.api_url + "comments/{}".format(post_id), data=params)
        else:
            r = requests.get(self.api_url + "comments", data=params)
        return r.json()

    def post_comment(self, params=None):
        # post a comment to the blog
        r = requests.post(self.api_url + "comments", data=params)
        return r.json()

    def get_taxonomies(self, taxonomy=None, params=None):
        # get all taxonomies
        if taxonomy:
            r = requests.get(
                self.api_url + "taxonomies/{}".format(taxonomy), data=params)
        else:
            r = requests.get(self.api_url + "taxonomies", data=params)
        return r.json()

    def get_media(self, media_id=None, params=None):
        # get all blog media
        if media_id:
            r = requests.get(
                self.api_url + "media/{}".format(media_id), data=params)
        else:
            r = requests.get(self.api_url + "media", data=params)
        return r.json()

    def get_users(self, user_id=None, params=None):
        # get all blog users
        if user_id:
            r = requests.get(
                self.api_url + "users/{}".format(user_id), data=params)
        else:
            r = requests.get(self.api_url + "users", data=params)
        return r.json()

    def search(self, search_item=None, params=None):
        # get all search results
        if search_item:
            if params == None:
                params = {}
            params["search"] = search_item
        r = requests.get(self.api_url + "users", data=params)
        return r.json()


if __name__ == "__main__":
    wp = WP("https://blog.cleanpick.green")
    # print(wp.get_posts())
    # print(wp.get_posts(1))
    # print(wp.get_categories())
    # print(wp.get_tags())
    # print(wp.get_pages())
    # print(wp.get_pages(1))
    # print(wp.get_comments())
    # print(wp.get_comments(1))
    # print(wp.post_comment())
    # print(wp.get_taxonomies())
    # print(wp.get_taxonomies(1))
    # print(wp.get_media())
    # print(wp.get_media(1))
    # print(wp.get_users())
    # print(wp.get_users(1))
    print(wp.search("hello"))
