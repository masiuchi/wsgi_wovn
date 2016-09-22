import json
import urllib.request
import re

from wsgi_wovn.lang import Lang


class Store:

    def __init__(self):
        self.__settings = {
            'user_token':      '',
            'secret_key':      '',
            'url_pattern':     'path',
            'url_pattern_reg': '/(?P<lang>[^/.?]+)',
            'query':           [],
            'api_url':         'https://api.wovn.io/v0/values',
            'default_lang':    'en',
            'supported_langs': ['en'],
            'test_mode':       False,
            'test_url':        '',
        }
        self.__config_loaded = False

    def is_valid_settings(self):
        valid = True
        errors = []
        settings = self.settings()

        if 'user_token' not in settings \
                or len(settings['user_token']) < 5 \
                or len(settings['user_token']) > 6:
            valid = False
            errors.append('User token is %s not valid.' %
                          settings['user_token'])

        if 'secret_key' not in settings or not settings['secret_key']:
            valid = False
            errors.append('Secret key %s is not valid.' %
                          settings['secret_key'])

        if 'url_pattern' not in settings or not settings['url_pattern']:
            valid = False
            errors.append('Url pattern %s is not valid.' %
                          settings['url_pattern'])

        if 'query' not in settings or not isinstance(settings['query'], list):
            valid = False
            errors.append('query config %s is not valid.' % settings['query'])

        if 'api_url' not in settings or not settings['api_url']:
            valid = False
            errors.append('API URL is not configured.')

        if 'default_lang' not in settings or not settings['default_lang']:
            valid = False
            errors.append('Default lang %s is not valid.' %
                          settings['default_lang'])

        if 'supported_langs' not in settings \
                or not isinstance(settings['supported_langs'], list) \
                or len(settings['supported_langs']) < 1:
            valid = False
            errors.append('Supported langs configuration is not valid.')

        if len(errors) > 0:
            print(errors)

        return valid

    def settings(self, opts={}):
        if len(opts) > 0:
            dicts = [self.__settings, opts]
            self.__settings = {k: v for dic in dicts for k, v in dic.items()}

        if not self.__config_loaded:
            self.__settings['default_lang'] \
                = Lang.get_code(self.__settings.get('default_lang'))
            if 'supported_langs' not in self.__settings:
                self.__settings['supported_langs'] = [
                    self.__settings['default_lang']]

            if self.__settings.get('url_pattern') == 'path':
                self.__settings['url_pattern_reg'] = r'/(?P<lang>[^/.?]+)'
            elif self.__settings.get('url_pattern') == 'query':
                self.__settings['url_pattern_reg'] \
                    = r'((\?.*&)|\?)wovn=(?P<lang>[^&]+)(&|$)'
            elif self.__settings.get('url_pattern') == 'subdomain':
                self.__settings['url_pattern_reg'] = r'^(?P<lang>[^.]+)\.'

            if not self.__settings.get('test_mode') \
                    or not self.__setting.get('test_mode') == 'on':
                self.__settings['test_mode'] = False
            else:
                self.__settings['test_mode'] = True
            self.__config_loaded = True

        return self.__settings

    def get_values(self, url):
        url = re.sub(r'/+$', '', url)
        request_url = '%s?token=%s&url=%s' % (
            self.settings().get('api_url'),
            self.settings().get('user_token'),
            url
        )
        body = b''
        with urllib.request.urlopen(request_url) as page:
            for line in page.readlines():
                body = body + line
        vals = json.loads(body.decode('utf-8'))
        return vals
