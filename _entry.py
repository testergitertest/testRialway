from detalib.handler import handle
from detalib.debugger import debug

try:
    import main  # noqa
except Exception:
    pass


@debug
def handler(event, context):
    import main  # noqa

    return handle(event, main)