#!/usr/bin/env python

import praw
import time
import service
import traceback

UA = 'a script by /u/scubar that replies to grammar fanatics'

while True:
    try:
        r = praw.Reddit(UA)
        r.login()
        break
    except praw.errors.InvalidUser:
        print('Wrong User!')
    except praw.errors.InvalidUserPass:
        print('Wrong Password!')

print('Logged In.')

while True:
    try:
        for comment in praw.helpers.comment_stream(r, 'all'):
            if service.evaluate(comment.body):
                print('Got a match!')
                while True:
                        try:
                            comment.reply(service.get_reply())
                            break
                        except praw.errors.RateLimitExceeded as error:
                            print('\tSleeping for {0} seconds'.format(error.sleep_time))
                            time.sleep(error.sleep_time)
                        except:
                            traceback.print_exc()
                        finally:
                            break
    except:
        traceback.print_exc()
        print('\tSleeping for five minutes')
        time.sleep(300)