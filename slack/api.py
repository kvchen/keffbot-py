import urllib


class SlackEndpoints(object):
    base = 'https://slack.com/api/'

    def url(self, *args):
        """Returns the URL corresponding the API endpoint specified by the
        arguments.
        """
        endpoint = '.'.join(args)
        return urllib.parse.urljoin(self.base, endpoint)


endpoints = SlackEndpoints()


