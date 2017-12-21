import xml.etree.ElementTree as ET
import urllib.request as ur
import pandas as pd


def get_all_info(url):
    """

    :param url: url of xml
    :return: dataframe  of all info
    """

    xml_page = ur.urlopen(url)

    root = ET.fromstring(xml_page.read())

    result = []

    for child_l1 in root.getchildren():
        # level 1: indicators
        for child_l2 in child_l1:
            # level 2: indicator
            tmp = {}
            tmp = child_l2.attrib
            for child_l3 in child_l2.getchildren():
                # level 3 (last level)
                tmp[child_l3.tag.split('}')[1]] = child_l3.text
            result.append(tmp)

    data_frame_result = pd.DataFrame(result)

    return data_frame_result


if __name__ == '__main__':
    info = get_all_info('http://wits.worldbank.org/API/V1/wits/datasource/tradestats-trade/indicator/ALL?format=JSON')

    print(info)

# For the country data availability http://wits.worldbank.org/API/V1/wits/datasource/tradestats-trade/dataavailability/

aval_country = get_all_info('http://wits.worldbank.org/API/V1/wits/datasource/tradestats-trade/dataavailability/')['iso3Code']

list_country = set(aval_country)
'USA' in list_country