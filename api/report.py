

import datetime

class report:

    def __init__(self, responce: dict) -> None:
        
        # meta
        self.scan_url = responce['meta']['url_info']['url']

        # data
        data = responce['data']

        attributes = data['attributes']

        # results
        results = attributes['results']
        self.results = []
        self.fortinet = False

        for res in results.keys():
            if res == "Fortinet" and results[res]['result'] not in ["clean", "unrated"]:
                self.fortinet = True
            self.results.append(results[res])

        # stats
        stats = attributes['stats']
        
        self.score = stats['malicious'] + stats['suspicious']
        self.all_score = stats['harmless']

        self.date = datetime.datetime.fromtimestamp(attributes['date'])
        
    def __str__(self) -> str:

        scan_result = f"url: {self.scan_url} date: {self.date} "

        if self.score > 4:
            scan_result += f"malicious {self.score}/{self.all_score}"
        else:
            scan_result += f"clean {self.score}/{self.all_score}"

        if self.fortinet:
            scan_result += " fortinet"
        
        return scan_result