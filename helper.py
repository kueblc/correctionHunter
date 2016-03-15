# 3rd-Party Libraries
import praw
import logging

# Returns a logged in Reddit object, exits if login attempts limit is exceeded
def get_praw():
    logger = logging.getLogger('correction_hunter')
    login_attempts = 0
    while login_attempts <= 3:
        try:
            UA = 'a script by /u/scubar that replies to grammar fanatics'
            r = praw.Reddit(UA)
            r.login()
            logger.info('Logged In.')
            return r
        except praw.errors.InvalidUserPass:
            login_attempts += 1
            logger.error('Wrong Password!')
        except praw.errors.InvalidUser:
            login_attempts += 1
            logger.error('Wrong User!')
        finally:
            if login_attempts >= 3:
                logger.error('Max login attempts exceeded.')
                exit()

# Returns an initialized and configured logger
def log_factory():
    # Create Logger
    logger = logging.getLogger('correction_hunter')
    logger.setLevel(logging.DEBUG)

    # Setup formatting
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create File Handler
    fh = logging.FileHandler('ch.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    # Create Console Handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    # Add the Handlers to the Logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    # Return the Logger
    return logger
