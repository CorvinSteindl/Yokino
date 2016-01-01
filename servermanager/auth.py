from Yokino.exceptions import Unauthorized


def is_owner_or_forbidden(server, user):
    if server.owner != user:
        raise Unauthorized()
