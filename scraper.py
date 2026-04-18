import requests
from lxml import html
import json


def get_files(url, base_api="https://example.com/api"):
    """
    Extracts data parameters from a webpage and uses them
    to fetch structured data from an API endpoint.
    """

    try:
        response = requests.get(url)
        if not response.text:
            return []

        parsed_html = html.fromstring(response.text)

        # Generic: look for elements with data-params attribute
        params_list = parsed_html.xpath('//div[@data-params]/@data-params')

        if not params_list:
            return []

        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        results = []

        for params in params_list:
            if not params:
                continue

            api_url = f"{base_api}?{params}"

            try:
                api_response = requests.get(api_url, headers=headers)

                if not api_response.text:
                    continue

                payload = json.loads(api_response.text)
                data = payload.get("data")

                if data:
                    results.append(data)

            except Exception:
                continue

        return results

    except Exception:
        return []