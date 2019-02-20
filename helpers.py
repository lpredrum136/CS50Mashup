import feedparser
import urllib.parse

def lookup(geo):
    """Looks up articles for geo."""

    # check cache for geo
    """ if geo in lookup.cache:
        return lookup.cache[geo]. This snippet is old/unknown version.
 """

    try:
        if geo in lookup.cache:
            return lookup.cache[geo]
    except AttributeError:
        lookup.cache = {}

    # Replace special characters
    escaped = urllib.parse.quote(geo, safe="")

    # Get feed from Google
    feed = feedparser.parse(f"https://news.google.com/news/rss/local/section/geo/{escaped}")

    # if no items in feed, get feed from news.com.au
    # this for loop and if is not optimal because the feed has only one item and its title is "This feed is not available."
    # So actually the for loop is redundant. But we don't know how to jump exactly at the title above
    # For example, "if feed["items"][0]["title"] doesn't work at all.
    for item in feed["items"]:
        if item["title"] == "This feed is not available.":
            feed = feedparser.parse("https://www.news.com.au/content-feeds/latest-news-national/")

    # cache results
    lookup.cache[geo] = [{"link": item["link"], "title": item["title"]} for item in feed["items"]]

    # return results
    return lookup.cache[geo]

# initialize cache
# lookup.cache = {}. This snippet is old/unknown version.
