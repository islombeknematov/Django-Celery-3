from __future__ import unicode_literals, absolute_import

# This will make sure that app is always imported when
# django starts so that shared_task will use this app.
from .celeryy import app as celery_app

__all__ = ('celery_app',)

