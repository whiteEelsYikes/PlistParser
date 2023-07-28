"""
 .Plist Data
 本程序为Plist的py版本
 略...
"""
from PlistParser.Plist import PlistItem


class CacheExtraItem(PlistItem,):
    pass

class item28Item(PlistItem,):
    pass

class item28(PlistItem,):
    def __init__(self, item_index_tuple=None, item=None, data=None, item_index_head=''):
        item_index_tuple = () if item_index_tuple == None else item_index_tuple
        super().__init__(item_index_tuple, item, item_index_head=item_index_head)
        
        self.item_index_tuple = ('CacheExtra', 'oPeik/9e8lQWMszEjbPzng')
        self.item = 'oPeik/9e8lQWMszEjbPzng'
        self.item_index_head = ''
        self.data = None
        self.dict = {'CacheExtra': {'oPeik/9e8lQWMszEjbPzng': {'oPeik/9e8lQWMszEjbPzng': {}}}}
        self.dict_index = '["CacheExtra"]["oPeik/9e8lQWMszEjbPzng"]["oPeik/9e8lQWMszEjbPzng"]'
        self.path = 'CacheExtra.oPeik/9e8lQWMszEjbPzng.oPeik/9e8lQWMszEjbPzng'
        self.path_tuple = ('CacheExtra', 'oPeik/9e8lQWMszEjbPzng', 'oPeik/9e8lQWMszEjbPzng')
        self.item1 = item28Item(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'ArtworkDeviceIdiom', None, '')
        self.item2 = item28Item(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'ArtworkDeviceSubType', None, '')
        self.item3 = item28Item(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'GraphicsFeatureSetFallbacks', None, '')
        self.item4 = item28Item(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'CompatibleDeviceFallback', None, '')
        self.item5 = item28Item(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'ArtworkDisplayGamut', None, '')
        self.item6 = item28Item(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'ArtworkDeviceProductDescription', None, '')
        self.item7 = item28Item(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'ArtworkDynamicDisplayMode', None, '')
        self.item8 = item28Item(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'GraphicsFeatureSetClass', None, '')
        self.item9 = item28Item(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'ArtworkDeviceScaleFactor', None, '')
        self.item10 = item28Item(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'DevicePerformanceMemoryClass', None, '')

class item32Item(PlistItem,):
    pass

class item32(PlistItem,):
    def __init__(self, item_index_tuple=None, item=None, data=None, item_index_head=''):
        item_index_tuple = () if item_index_tuple == None else item_index_tuple
        super().__init__(item_index_tuple, item, item_index_head=item_index_head)
        
        self.item_index_tuple = ('CacheExtra', 'AoKnINTLPoKML3ctoP0AZg')
        self.item = 'AoKnINTLPoKML3ctoP0AZg'
        self.item_index_head = ''
        self.data = None
        self.dict = {'CacheExtra': {'AoKnINTLPoKML3ctoP0AZg': {'AoKnINTLPoKML3ctoP0AZg': {}}}}
        self.dict_index = '["CacheExtra"]["AoKnINTLPoKML3ctoP0AZg"]["AoKnINTLPoKML3ctoP0AZg"]'
        self.path = 'CacheExtra.AoKnINTLPoKML3ctoP0AZg.AoKnINTLPoKML3ctoP0AZg'
        self.path_tuple = ('CacheExtra', 'AoKnINTLPoKML3ctoP0AZg', 'AoKnINTLPoKML3ctoP0AZg')
        self.item1 = item32Item(('CacheExtra', 'AoKnINTLPoKML3ctoP0AZg'), 'media-compression', None, '')
        self.item2 = item32Item(('CacheExtra', 'AoKnINTLPoKML3ctoP0AZg'), 'universal-lossy-buffer-compression', None, '')
        self.item3 = item32Item(('CacheExtra', 'AoKnINTLPoKML3ctoP0AZg'), 'buffer-compression', None, '')
        self.item4 = item32Item(('CacheExtra', 'AoKnINTLPoKML3ctoP0AZg'), 'universal-buffer-compression', None, '')

class CacheExtra(PlistItem,):
    def __init__(self, item_index_tuple=None, item=None, data=None, item_index_head=''):
        item_index_tuple = () if item_index_tuple == None else item_index_tuple
        super().__init__(item_index_tuple, item, item_index_head=item_index_head)
        
        self.item_index_tuple = ('CacheExtra',)
        self.item = 'CacheExtra'
        self.item_index_head = ''
        self.data = None
        self.dict = {'CacheExtra': {'CacheExtra': {}}}
        self.dict_index = '["CacheExtra"]["CacheExtra"]'
        self.path = 'CacheExtra.CacheExtra'
        self.path_tuple = ('CacheExtra', 'CacheExtra')
        self.item1 = CacheExtraItem(('CacheExtra',), 'oBbtJ8x+s1q0OkaiocPuog', None, '')
        self.item2 = CacheExtraItem(('CacheExtra',), '96GRvvjuBKkU4HzNsYcHPA', None, '')
        self.item3 = CacheExtraItem(('CacheExtra',), 'wYMBabAO8VguyDDVgCsPdg', None, '')
        self.item4 = CacheExtraItem(('CacheExtra',), 'TZ/0j62wM3D0CuRt+Nc/Lw', None, '')
        self.device_category = CacheExtraItem(('CacheExtra',), 'VuGdqp8UBpi9vPWHlPluVQ', None, '')
        self.GUID_partition_scheme = CacheExtraItem(('CacheExtra',), 'xUHcyT2/HE8oi/4LaOI+Sw', None, '')
        self.item5 = CacheExtraItem(('CacheExtra',), 'NaA/zJV7myg2w4YNmSe4yQ', None, '')
        self.item6 = CacheExtraItem(('CacheExtra',), 'DViRIxZ/ZwO007CLcEYvZw', None, '')
        self.item7 = CacheExtraItem(('CacheExtra',), 'QbQzuIbef01P4JeoL9EmKg', None, '')
        self.item8 = CacheExtraItem(('CacheExtra',), 'gBw7IWiBnLHaA+lBrZBgWw', None, '')
        self.item9 = CacheExtraItem(('CacheExtra',), 'pB5sZVvnp+QjZQtt2KfQvA', None, '')
        self.item10 = CacheExtraItem(('CacheExtra',), 'qwXfFvH5jPXPxrny0XuGtQ', None, '')
        self.device_issuance = CacheExtraItem(('CacheExtra',), 'zHeENZu+wbg7PUprwNwBWg', None, '')
        self.item11 = CacheExtraItem(('CacheExtra',), 'LeSRsiLoJCMhjn6nd6GWbQ', None, '')
        self.itemx = CacheExtraItem(('CacheExtra',), '9MZ5AdH43csAUajl/dU+IQ', None, '')
        self.item12 = CacheExtraItem(('CacheExtra',), 'JhEU414EIaDvAz8ki5DSqw', None, '')
        self.item13 = CacheExtraItem(('CacheExtra',), '+3Uf0Pm5F8Xy7Onyvko0vA', None, '')
        self.device_model = CacheExtraItem(('CacheExtra',), 'Z/dqyWS6OZTRy10UcmUAhw', None, '')
        self.item14 = CacheExtraItem(('CacheExtra',), 'Nzu4E/VsXjEIa83CkRdZrQ', None, '')
        self.item15 = CacheExtraItem(('CacheExtra',), '91LyMcx4z1w3SGVeqteMnA', None, '')
        self.item16 = CacheExtraItem(('CacheExtra',), 'JUWcn+5Ss0nvr5w/jk4WEg', None, '')
        self.item17 = CacheExtraItem(('CacheExtra',), 'rkqlwPcRHwixY4gapPjanw', None, '')
        self.item18 = CacheExtraItem(('CacheExtra',), 'IMLaTlxS7ITtwfbRfPYWuA', None, '')
        self.item19 = CacheExtraItem(('CacheExtra',), '4qfpxrvLtWillIHpIsVgMA', None, '')
        self.item20 = CacheExtraItem(('CacheExtra',), 'h63QSdBCiT/z0WU6rdQv6Q', None, '')
        self.item21 = CacheExtraItem(('CacheExtra',), 'qNNddlUK+B/YlooNoymwgA', None, '')
        self.item22 = CacheExtraItem(('CacheExtra',), 'k7QIBwZJJOVw+Sej/8h8VA', None, '')
        self.item23 = CacheExtraItem(('CacheExtra',), 'mZfUC7qo4pURNhyMHZ62RQ', None, '')
        self.device_system = CacheExtraItem(('CacheExtra',), 'ivIu8YTDnBSrYv/SN4G8Ag', None, '')
        self.item24 = CacheExtraItem(('CacheExtra',), '4W7X4OWHjri5PGaAGsCWxw', None, '')
        self.item25 = CacheExtraItem(('CacheExtra',), 'emXA9B552rnSoI7xXE91DA', None, '')
        self.item26 = CacheExtraItem(('CacheExtra',), 'NUYAz1eq3Flzt7ZQxXC/ng', None, '')
        self.item27 = CacheExtraItem(('CacheExtra',), '97JDvERpVwO+GHtthIh7hA', None, '')
        self.item28 = item28(('CacheExtra', 'oPeik/9e8lQWMszEjbPzng'), 'oPeik/9e8lQWMszEjbPzng', None, '')
        self.item29 = CacheExtraItem(('CacheExtra',), 'ybGkijAwLTwevankfVzsDQ', None, '')
        self.item30 = CacheExtraItem(('CacheExtra',), '9s45ldrCC1WF+7b6C4H2BA', None, '')
        self.item31 = CacheExtraItem(('CacheExtra',), 'LTI8wHvEYKy8zR1IXBW1uQ', None, '')
        self.item32 = item32(('CacheExtra', 'AoKnINTLPoKML3ctoP0AZg'), 'AoKnINTLPoKML3ctoP0AZg', None, '')
        self.item33 = CacheExtraItem(('CacheExtra',), 'bbtR9jQx50Fv5Af/affNtA', None, '')
        self.item34 = CacheExtraItem(('CacheExtra',), 'nSo8opze5rFk+EdBoR6tBw', None, '')
        self.item35 = CacheExtraItem(('CacheExtra',), 'HXTqT3UXOKuTEklxz+wMAA', None, '')
        self.item36 = CacheExtraItem(('CacheExtra',), '5pYKlGnYYBzGvAlIU8RjEQ', None, '')
        self.item37 = CacheExtraItem(('CacheExtra',), 'h9jDsbgj7xIVeIQ8S3/X3Q', None, '')
        self.item38 = CacheExtraItem(('CacheExtra',), 'mumHZHMLEfAuTkkd28fHlQ', None, '')
        self.item39 = CacheExtraItem(('CacheExtra',), 'k+KTni1jrwErpcDMEnn3aw', None, '')
        self.item40 = CacheExtraItem(('CacheExtra',), '/YYygAofPDbhrwToVsXdeA', None, '')
        self.item41 = CacheExtraItem(('CacheExtra',), 'c7fCSBIbX1mFaRoKT5zTIw', None, '')

class PlistItem():
    def __init__(self, item_index_tuple=None, item=None, data=None, item_index_head=''):
        item_index_tuple = () if item_index_tuple == None else item_index_tuple
        super().__init__(item_index_tuple, item, item_index_head=item_index_head)
        
        self.item_index_tuple = ()
        self.item = ''
        self.item_index_head = ''
        self.data = None
        self.dict = {'': None}
        self.dict_index = '[""]'
        self.path = ''
        self.path_tuple = ('',)
        self.CacheUUID = PlistItem((), 'CacheUUID', None, '')
        self.CacheData = PlistItem((), 'CacheData', None, '')
        self.CacheExtra = CacheExtra(('CacheExtra',), 'CacheExtra', None, '')
        self.CacheVersion = PlistItem((), 'CacheVersion', None, '')

