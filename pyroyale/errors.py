class ClashRoyaleAPIError(Exception):
    """Catch-all for all generic errors involved with accessing the
    ClashRoyale API"""
    pass

class ClashRoyaleAPIMissingFieldsError(Exception):
    """One of the required fields is empty, thus we're bailing early,
    knowing we're going to fail. The reason for this error is that the
    two fields that the end user NEEDS to provide are clan tag and API
    key, so we can't rely on defaults. We want to give nice error
    messages in this state to aid in troubleshooting."""
    field_name = None

    def __init__(self, field_name):
        Exception.__init__(self, "'{}' not provided".format(field_name))
        self.field_name = field_name


class ClashRoyaleAPIAuthenticationError(Exception):
    """Failed to authenticate with the API. Key is likely bad."""
    pass

class ClashRoyaleAPIClanNotFound(Exception):
    """clan_id is likely incorrect or invalid."""
    def __init__(self, clan_tag):
        Exception.__init__(self, 'Clan with tag "{}" not found'.format(clan_tag))
        self.clan_tag = clan_tag
