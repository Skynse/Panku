#!/usr/bin/env python3
"""
Panku: Easy Reddit Scraper designed for humans.

Example Code

>> python_sub = Reddit('Python')
>> python_sub.read()

DISCLAIMER FROM REDDITS END USER LICENSE AGREEMENT ON WEB SCRAPING

Access, query, or search the Services with any automated system, 
other than through our published interfaces and pursuant to their
applicable terms. However, we conditionally grant permission to crawl
the Services for the sole purpose of and solely to the extent necessary
for creating publicly available searchable indices of the materials subject
to the parameters set forth in our robots.txt file.
"""

__version__ = 0.7
import argparse
from urllib.request import Request, urlopen
import json


class COLORS:
    red = '\u001b[31m'
    green = '\u001b[32m'
    end = '\033[0m'


class Reddit:

    def __init__(self, subreddit: str, count=20, imgs: bool=False) -> None:
        """
        :param subreddit: Subreddit definition
        :param count: Post count
        :param imgs: Images
        """

        self.subreddit = subreddit
        self.count = count
        self.imgs = imgs

    def read(self) -> None:
        # initialize a user agent so that Reddit, or any website we scrape doesn't think we're a bot
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/39.0.2171.95 Safari/537.36'}

        base_url = f'https://old.reddit.com/r/%s/.json?limit={self.count}' % self.subreddit

        print('Using Base URL: %s\n' % base_url)
        if self.imgs:
            print('load image urls: True')
        else:
            print('load image urls: False')

        req = Request(base_url, headers=headers)
        data = json.loads(urlopen(req).read())

        for post in data['data']['children']:
            title = COLORS.red + post['data']['title'] + COLORS.end
            author = post['data']['author']
            link = post['data']['permalink']
            lines = f"{title}\nby {author} → {COLORS.green}https://reddit.com{link}{COLORS.end}  \n"
            print(lines)

            if self.imgs == 1:
                print(post['data']['url'])


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        usage='panku -s {subreddit_name} -c {post count}',
        description='Easy Reddit Scraper designed for humans'

    )

    parser.add_argument(
        "-s",
        help='define subreddit to scrape',
        type=str
    )

    parser.add_argument(
        '-d',
        '--debug',
        help='boolean for debug mode',
        type=str
    )

    parser.add_argument(
        '-c',
        '--count',
        dest='counter',
        help='Post count',
        type=int
    )

    parser.add_argument(

        '-i',
        '--image',
        dest='images',
        help='Show image urls',
        type=bool
    )
    args = parser.parse_args()

    if args.counter:
        runtime_subreddit = Reddit(args.s, count=args.counter)
        if args.images:
            runtime_subreddit = Reddit(args.s, count=args.counter, imgs=True)
        else:
            runtime_subreddit = Reddit(args.s, count=args.counter)

    else:
        runtime_subreddit = Reddit(args.s)
    runtime_subreddit.read()

    if args.debug:
        if 'True' in args.debug:
            print('Panku version %s' % __version__)
            print('debug: Used https://reddit.com/r/%s as runtime subreddit' % args.s)
            print(f'Post Count:{runtime_subreddit.count}')
