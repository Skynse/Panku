#!/usr/bin/env python3
"""
Panku: Easy Reddit Scraper designed for humans.

Example Code

python_sub = Reddit('Python')
python_sub.read()

"""

__version__ = 0.4
RED = '\u001b[31m'
import argparse
from urllib.request import Request,urlopen
import json


class Reddit:

    class COLORS:
        red = '\032[91m'
        end = '\033[0m'

    def __init__(self, subreddit, count=20, imgs=False):
        self.subreddit = subreddit
        self.count = count
        self.imgs = imgs

        """
        :param subreddit: Defines the reddit forum that the code will search through.
        """

    def read(self):
        # initialize a user agent so that Reddit, or any website we scrape doesn't think we're a bot
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/39.0.2171.95 Safari/537.36'}

        base_url = f'https://old.reddit.com/r/%s/.json?limit={self.count}' % self.subreddit

        print('Using Base URL: %s\n' % base_url)

        req = Request(base_url,headers=headers)
        data  = json.loads(urlopen(req).read())

        for post in data['data']['children']:
            title = RED + post['data']['title'] + '\033[0m'
            author = post['data']['author']
            link = post['data']['permalink']
            lines = f"{title}\nby {author} → https://reddit.com{link} \n"
            print(lines)

            if self.imgs:
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
        help='Post images [unstable]',
        type=bool
    )
    args = parser.parse_args()

    if args.counter:
        runtime_subreddit = Reddit(args.s, count=args.counter)
        if args.images:
            runtime_subreddit = Reddit(args.s, count=args.counter, imgs=args.images)
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
