import csv
from datetime import datetime
from pathlib import Path

from itemadapter import ItemAdapter

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.__statuses = {}

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter_status = adapter.get('status')
        if adapter_status:
            pep_status = adapter['status']
            self.__statuses[pep_status] = (
                self.__statuses.get(pep_status, 0) + 1
            )
            return item

    def close_spider(self, spider):
        time = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        filename = BASE_DIR / f'results/status_summary_{time}.csv'
        with open(filename, mode='w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows(
                (
                    ("Статус", "Количество"),
                    *self.__statuses.items(),
                    ("Total", sum(self.__statuses.values()))
                )
            )
