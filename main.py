

from excel import *
from api import *

# virustotal test site's
urls = excel_reader()

# urls = ["https://utorrent.softybased.ru/", "https://ya.ru/"]

results = []

for u in urls:
    scan_url = url_scan(u)
    report_url = get_url_report(scaned_url=scan_url)

    # print("scan_url: ")
    # print(f"    {scan_url}")
    # print("report: ")
    # print(f"    {report_url}")
    # print("___________________________")

    results.append(report_url)

# make report
write_to_excel(results=results)
