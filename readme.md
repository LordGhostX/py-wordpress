# WordPress REST API Wrapper

Python API Wrapper for WordPress

Getting Started
```python
from wordpress import WP

blog = WP("https://example-wordpress.com")
```

Get Blog Posts
```python
# Getting all posts from the blog
print(wp.get_posts())

# Get a single post with a specified ID
post_id = 474
print(wp.get_posts(post_id))
```

Get Blog Categories
```python
# Getting all post categories from the blog
print(wp.get_categories())
```

Get Blog Tags
```python
# Getting all post tags from the blog
print(wp.get_tags())
```

Get Blog Pages
```python
# Getting all pages from the blog
print(wp.get_pages())

# Get a single page with a specified ID
page_id = 10
print(wp.get_pages(page_id))
```

Get & Post Blog Comments
```python
# Getting all comments from the blog
print(wp.get_comments())

# Get a single comment with a specified ID
comment_id = 1
print(wp.get_comments(comment_id))

print(wp.post_comment())
```

Get Blog Taxonomies
```python
# Getting all taxonomies from the blog
print(wp.get_taxonomies())

# Get a single taxonomy with a specified ID
taxonomy_id = 1
print(wp.get_taxonomies(taxonomy_id))
```

Get Blog Media
```python
# Getting all media from the blog
print(wp.get_media())

# Get a single media with a specified ID
media_id = 10
print(wp.get_media(media_id))
```

Get Blog Users
```python
# Getting all users from the blog
print(wp.get_users())

# Get a single user with a specified ID
user_id = 10
print(wp.get_users(user_id))
```

Search Blog
```python
# Search blog for a string
search_item = "hello world"
print(wp.get_string(search_item))
```
