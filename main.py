#!/usr/bin/env python

# 3rd-Party Libraries
import praw
import time

# 1st-Party Libraries
import service
import helper

# Initialize Logging
logger = helper.log_factory()

# Login to Reddit
reddit_session = helper.get_praw()

# Main Loop
running = True
comments_evaluated = 0
while running:
    try:
        for comment in praw.helpers.comment_stream(reddit_session, 'all'):
            if service.evaluate(comment.body):
                logger.info('Found a matching comment!')
                while True:
                        try:
                            comment.reply(service.get_reply())
                            break
                        except reddit_session.errors.RateLimitExceeded as rateLimitEx:
                            logger.error('\tRate Limited Exceeded! Sleeping for {0} seconds'.format(rateLimitEx.sleep_time))
                            time.sleep(rateLimitEx.sleep_time)
                        except Exception as ex:
                            logger.error(ex)
                        finally:
                            break
            comments_evaluated += 1
    except KeyboardInterrupt:
        logger.info('\tKeyboard Interrupt! Stopping after {0} Comments.'.format(comments_evaluated))
        running = False
    except SystemExit:
        logger.info('\tSystem Exit! Stopping after {0} Comments.'.format(comments_evaluated))
        running = False
    except:
        logger.error('\tUnhandled Exception! Sleeping for 5 minutes.')
        time.sleep(300)