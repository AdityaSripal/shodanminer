import logging
import requests
import bs4

LOG = logging.getLogger(__name__)
from . import basepoller

class ShodanMiner(basepoller.BasePollerFT):
    def configure(self):
        super(ShodanMiner, self).configure()
        self.polling_timeout = self.config.get('polling_timeout', 20)
        self.verify_cert = self.config.get('verify_cert', True)
        self.url = 'http://wiki.ipfire.org/en/configuration/firewall/blockshodan'

    def _build_iterator(self, now):
        r = requests.get(self.url)
        try:
            r.raise_for_status()
        except:
            LOG.debug('%s - exception in request: %s %s',
                      self.name, r.status_code, r.content)
        html_soup = bs4.BeautifulSoup(r.content, "lxml")
        result = html_soup.find_all('td', class_='col1')

        return result

    def _process_item(self, item):
        indicator = item.string.strip()
        value = {
            'type': 'IPv4',
            'confidence': 100
        }
        return [[indicator, value]]
