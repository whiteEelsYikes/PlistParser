import tkinter as tk
from tkinter import ttk

from PlistParser.Plist import PlistItem
from PlistParser.PlistParser import PlistParser


def populate_tree(tree, parent, dic):
    for key in dic:
        uid = tree.insert(parent, 'end', text=key)
        if isinstance(dic[key], dict):
            populate_tree(tree, uid, dic[key])
        else:
            tree.insert(uid, 'end', text=dic[key])


def display_json(json_data):
    app = tk.Tk()
    tree = ttk.Treeview(app)
    tree.pack()
    populate_tree(tree, '', json_data)
    app.mainloop()


def raed_plist(path, map_dict, name_map_dict):
    pp = PlistParser()
    pp.parser_dict(path)
    plist = PlistItem((), None)
    plist.load_parse_dict(pp.plist_dict, map_dict)
    plist_dict = -plist
    plist_map_dict = plist.attribute_mapping_dict()
    plist_dict = plist.dict_key_replacement(plist_dict, plist_map_dict, True)
    plist_dict = plist.dict_key_replacement(plist_dict, name_map_dict, True)
    return plist_dict


def write_plist(py, plist_dict, map_dict, name_map_dict):
    plist = PlistItem((), None)
    name_map_dict = plist.attribute_mapping_dict_reverse(name_map_dict)
    plist_dict = plist.dict_key_replacement(plist_dict, name_map_dict, True)
    map_dict_ = plist.attribute_mapping_dict_reverse(map_dict)
    plist_dict = plist.dict_key_replacement(plist_dict, map_dict_, True)
    plist = type(f'Plist', (PlistItem,), {})
    plist = plist((), None)
    plist.load_parse_dict(plist_dict, map_dict)
    plist * py


attribute_mapping_dict_iPhone14_Pro_Max = {
    'CacheUUID': 'CacheUUID',
    'CacheData': 'CacheData',
    'CacheVersion': 'CacheVersion',
    'CacheExtra': {
        'CacheExtra': 'CacheExtra',
        'oBbtJ8x+s1q0OkaiocPuog': 'item1',
        '96GRvvjuBKkU4HzNsYcHPA': 'item2',
        'wYMBabAO8VguyDDVgCsPdg': 'item3',
        'TZ/0j62wM3D0CuRt+Nc/Lw': 'item4',
        'VuGdqp8UBpi9vPWHlPluVQ': 'device_category',
        'xUHcyT2/HE8oi/4LaOI+Sw': 'GUID_partition_scheme',
        'NaA/zJV7myg2w4YNmSe4yQ': 'item5',
        'DViRIxZ/ZwO007CLcEYvZw': 'item6',
        'QbQzuIbef01P4JeoL9EmKg': 'item7',
        'gBw7IWiBnLHaA+lBrZBgWw': 'item8',
        'pB5sZVvnp+QjZQtt2KfQvA': 'item9',
        'qwXfFvH5jPXPxrny0XuGtQ': 'item10',
        'zHeENZu+wbg7PUprwNwBWg': 'device_issuance',
        'LeSRsiLoJCMhjn6nd6GWbQ': 'item11',
        '9MZ5AdH43csAUajl/dU+IQ': 'itemx',
        'JhEU414EIaDvAz8ki5DSqw': 'item12',
        '+3Uf0Pm5F8Xy7Onyvko0vA': 'item13',
        'Z/dqyWS6OZTRy10UcmUAhw': 'device_model',
        'Nzu4E/VsXjEIa83CkRdZrQ': 'item14',
        '91LyMcx4z1w3SGVeqteMnA': 'item15',
        'JUWcn+5Ss0nvr5w/jk4WEg': 'item16',
        'rkqlwPcRHwixY4gapPjanw': 'item17',
        'IMLaTlxS7ITtwfbRfPYWuA': 'item18',
        '4qfpxrvLtWillIHpIsVgMA': 'item19',
        'h63QSdBCiT/z0WU6rdQv6Q': 'item20',
        'qNNddlUK+B/YlooNoymwgA': 'item21',
        'k7QIBwZJJOVw+Sej/8h8VA': 'item22',
        'mZfUC7qo4pURNhyMHZ62RQ': 'item23',
        'ivIu8YTDnBSrYv/SN4G8Ag': 'device_system',
        '4W7X4OWHjri5PGaAGsCWxw': 'item24',
        'emXA9B552rnSoI7xXE91DA': 'item25',
        'NUYAz1eq3Flzt7ZQxXC/ng': 'item26',
        '97JDvERpVwO+GHtthIh7hA': 'item27',
        'oPeik/9e8lQWMszEjbPzng': {
            'oPeik/9e8lQWMszEjbPzng': 'item28',
            'ArtworkDeviceIdiom': 'item1',
            'ArtworkDeviceSubType': 'item2',
            'GraphicsFeatureSetFallbacks': 'item3',
            'CompatibleDeviceFallback': 'item4',
            'ArtworkDisplayGamut': 'item5',
            'ArtworkDeviceProductDescription': 'item6',
            'ArtworkDynamicDisplayMode': 'item7',
            'GraphicsFeatureSetClass': 'item8',
            'ArtworkDeviceScaleFactor': 'item9',
            'DevicePerformanceMemoryClass': 'item10'
        },
        'ybGkijAwLTwevankfVzsDQ': 'item29',
        '9s45ldrCC1WF+7b6C4H2BA': 'item30',
        'LTI8wHvEYKy8zR1IXBW1uQ': 'item31',
        'AoKnINTLPoKML3ctoP0AZg': {
            'AoKnINTLPoKML3ctoP0AZg': 'item32',
            'media-compression': 'item1',
            'universal-lossy-buffer-compression': 'item2',
            'buffer-compression': 'item3',
            'universal-buffer-compression': 'item4'
        },
        'bbtR9jQx50Fv5Af/affNtA': 'item33',
        'nSo8opze5rFk+EdBoR6tBw': 'item34',
        'HXTqT3UXOKuTEklxz+wMAA': 'item35',
        '5pYKlGnYYBzGvAlIU8RjEQ': 'item36',
        'h9jDsbgj7xIVeIQ8S3/X3Q': 'item37',
        'mumHZHMLEfAuTkkd28fHlQ': 'item38',
        'k+KTni1jrwErpcDMEnn3aw': 'item39',
        '/YYygAofPDbhrwToVsXdeA': 'item40',
        'c7fCSBIbX1mFaRoKT5zTIw': 'item41'
    },
}
name_map_dict = {'CacheUUID': 'CacheUUID', 'CacheData': 'CacheData', 'CacheVersion': 'CacheVersion',
                 'CacheExtra': {'CacheExtra': 'CacheExtra', 'device_category': '设备类别',
                                'device_issuance': '设备发行', 'device_model': '设备型号', 'device_system': '设备系统'}}


if __name__ == '__main__':
    plist_dict = raed_plist('../TEST/example.plist',
                            attribute_mapping_dict_iPhone14_Pro_Max, name_map_dict)
    display_json(plist_dict)

    write_plist('Plist.py', plist_dict, attribute_mapping_dict_iPhone14_Pro_Max, name_map_dict)
