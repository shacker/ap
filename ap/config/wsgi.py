import logging
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iris.config.settings.local')
log = logging.getLogger(__name__)

application = get_wsgi_application()
if 'NEW_RELIC_LICENSE_KEY' in os.environ or 'NEW_RELIC_CONFIG_FILE' in os.environ:
    os.environ.setdefault('NEW_RELIC_ENABLED', 'true')
    try:
        import newrelic.agent
        newrelic.agent.initialize()
    except ImportError:
        log.warning("Could not import Newrelic agent")
