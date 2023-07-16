
from PlistParser.PlistParser import PlistParser, FastPlistParser
from PlistParser.Plist import Plist,PlistItem
from PlistParser.Base64 import Base64
from PlistParser.Extend import attribute_mapping_dict_iPhone14_Pro_Max

plist = r'plist/com.apple.MobileGestalt.plist'
out_plist = r'plist/example.plist'

plist_parser = PlistParser()
plist_value = plist_parser.parser_dict(plist)
print(plist_value)
plist_value = plist_parser.parser_plist(plist_value, out_plist)
print(plist_value)
data = plist_parser.customization_parser_dict_value(~Plist().CacheExtra.device_model, 'abbbcd')
print(data)

print(~Plist().CacheExtra.device_model)
print(-Plist().CacheExtra.device_model)
print(+Plist().CacheExtra.device_model)
print(Plist().CacheExtra.device_model.item)
print(Plist().CacheExtra.device_model.item_index_head)
print(Plist().CacheExtra.device_model.item_index_tuple)

data = {
    ~Plist().CacheUUID: None,
    ~Plist().CacheExtra.device_category: None,
    ~Plist().CacheExtra.device_issuance: None,
}
print(data)
data = plist_parser.plist_dict_to_cust_dict(data)
print(data)

plist_value = plist_parser.parser_plist(out_file='plist/example.plist')

plist_parser = FastPlistParser(plist_parser)

data = plist_parser.device_model()
print(data)
data = plist_parser.device_category()
print(data)
data = plist_parser.device_issuance()
print(data)
data = plist_parser.device_system()
print(data)

print(+Plist().CacheExtra.device_model)



data = {
    ~Plist().CacheExtra.device_model:'abcc',
    ~Plist().CacheExtra.device_model:None,  # 查询
}
data = plist_parser.plist_dict_to_cust_dict(data)
data = plist_parser.customization_parser_dict_values(data)
print(data)
print(plist_parser.customization_parser_dict_value(~Plist().CacheExtra.device_issuance))
print(plist_parser.plist_dict)


data = {
    Base64.Decode.bit64: {},
}
data = plist_parser.parser_base64(b'YWRtaW4=', data)
print(data)

data = PlistParser()
print(data.__dict__)
print(Plist().__dict__)

data = Plist().simplification_dict()
print(data)

data = Plist().CacheExtra + {}
print(data)

data = -Plist()
print(data)


print('-'*60)

data = PlistItem((),'').load_parse_dict(
                    plist_parser.parser_dict(plist),
                    attribute_mapping_dict_iPhone14_Pro_Max,
                    )
print(-data.CacheExtra)

# d = Plist((),'').save_py_file('./../PlistParser.test-s/test.py')

d = data
d.save_py_file()
print(d)

d * './../PlistParser.test-s/test.py'





