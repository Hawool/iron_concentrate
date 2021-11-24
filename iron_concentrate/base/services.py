import pandas as pd


def get_obj_list(file):
    excel = pd.read_excel(file)
    excel.head()
    l = []
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
        l.append(d)
    return l
