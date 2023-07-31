#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64

class Base64:
    class Encode:
        bit16 = base64.b16encode
        bit32 = base64.b32encode
        bit64 = base64.b64encode
        bit85 = base64.b85decode

    class Decode:
        bit16 = base64.b16decode
        bit32 = base64.b32decode
        bit64 = base64.b64decode
        bit85 = base64.b85decode

