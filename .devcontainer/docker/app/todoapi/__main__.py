from todoapi import app
import gunicorn.app.base
import ptvsd
import os


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


# リモートデバッグする場合の設定
if os.getenv("TODOAPI_REMOTE_DEBUG") == "on":
    ptvsd.enable_attach(address=("0.0.0.0", 3000))
    ptvsd.wait_for_attach()
    ptvsd.break_into_debugger()

if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('0.0.0.0', '5000'),
        'workers': 1,
    }
    StandaloneApplication(app, options).run()
