#!/usr/bin/env python

import sys
import random
import fbconsole as fb

#GID = '504896499520960' # pan group
GID = '102305819969381' # myfrog

def post_msg(fb, path, msg):
    fb.post(path, {"message": msg})

def get_msgs(fb, path):
    return fb.get(path)

def get_rand_msg(fn):
    return random.sample(open(fn).readlines(), 1)[0].strip()

def get_weekday():
    import datetime
    return datetime.datetime.today().weekday()

def main():
    if len(sys.argv) < 2:
        print "usage: %s <message_file>"
        sys.exit()
    fn = sys.argv[1]
    fb.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'user_groups']
    fb.authenticate()
    msg = get_rand_msg(fn)
    if get_weekday() == 5:
        path = '/%s/feed' % GID
    else:
        msgs = get_msgs(fb, '/%s/feed' % GID )
        mid = msgs['data'][0]['id']
        path = '/%s/comments' % mid 
    post_msg(fb, path , msg)

if __name__ == '__main__':
    main()

