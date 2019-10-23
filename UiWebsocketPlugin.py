from Plugin import PluginManager

@PluginManager.registerTo("UiWebsocket")
class UiWebsocketPlugin(object):

    # Create a new action that can be called using zeroframe api
    def actionSudo(self, to):
        self.response(to, { 'message': 'With great power comes great responsibility!' })
