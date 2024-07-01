

import os
import datetime
import pandas as pd

def write_to_excel(results: list) -> None:

    scores = []
    urls   = []
    dates  = []

    for result in results:
        scan_result = ""

        if result.score < 4:
           
            scan_result += f"clean {result.score}/{result.all_score}"

            if (result.fortinet):
                scan_result += " fortinet"

            scores.append(scan_result)
            urls.append(result.scan_url)
            dates.append(result.date.__str__())

    df = pd.DataFrame(
        {
            "urls": urls,
            "dates": dates,
            "scores": scores
        }
    )
    print(df.head(3))
    df.to_excel(f"{os.getcwd()}\\report.xlsx", sheet_name="report")
