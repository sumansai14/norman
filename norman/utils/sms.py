from django.conf import settings
import logging
import requests

logger = logging.getLogger(__name__)


def send_sms(body, to, from_=None):
    options = getattr(settings, 'SMS_SETTINGS', None)
    if not options:
        raise RuntimeError('SMS Settings not configured.')
    account = options.get('exotel')
    url = 'https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=account.get('sid'))
    rv = requests.post(url, auth=(account.get('sid'), account.get('token')), data={
        'From': account.get('number'),
        'To': to,
        'Body': body
    })
    if not rv.ok:
        logging.exception('Failed to send text message to %s: (%s) %s', to,
                          rv.status_code, rv.content)
        return False
    return True
