from oauth2client.client import OAuth2WebServerFlow
class Oauth(object):

    def __init__(self, config):
        if not config['clientId'] and not config['clientSecret'] and not config['scope'] and not config['redirectUri']:
            raise StandardError('clientId, clientSecret, scope or redirectUri has not been set')
        self.clientId = config['clientId']
        self.clientSecret = config['clientSecret']
        self.scope = config['scope']
        self.redirectUri = config['redirectUri']
        self.flow = None

    def createFlow(self):
        self.flow = OAuth2WebServerFlow(client_id=self.clientId, client_secret=self.clientSecret,
                                        scope=self.scope, redirect_uri=self.redirectUri)

    def getAuthUrl(self):
        if not self.flow:
            raise StandardError('flow object has not been defined')

        return self.flow.step1_get_authorize_url()

    def getCredentials(self, code):
        if not self.flow:
            raise StandardError('flow object has not been defined')

        return self.flow.step2_exchange(code)


