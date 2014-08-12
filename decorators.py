import logging
import endpoints


def oauth_required(endpoint_method):
    def wrapper(*args, **kwargs):
        self = args[0]
        self.current_user = endpoints.get_current_user()
        if not self.current_user:
            raise endpoints.UnauthorizedException
        logging.info(self.current_user.email())
        return endpoint_method(*args, **kwargs)
    return wrapper
