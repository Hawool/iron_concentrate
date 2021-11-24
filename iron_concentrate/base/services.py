import pandas as pd


def get_obj_list(file):
    """parsing excel, return list with dicts"""
    excel = pd.read_excel(file)
    excel.head()
    irons_list = []
    for i in range(len(excel)):
        d = {
            'name': excel.name[i],
            'iron': excel.iron[i],
            'silicon': excel.silicon[i],
            'aluminum': excel.aluminum[i],
            'calcium': excel.calcium[i],
            'sulfur': excel.sulfur[i],
            'month': excel.month[i],
        }
        irons_list.append(d)
    return irons_list
