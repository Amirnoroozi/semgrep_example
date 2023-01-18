from django.utils.safestring import SafeString, SafeData, SafeText
# ruleid:class-extends-safestring
class IWantToBypassEscaping(SafeString):
    def __init__(self):
        super().__init__()
class IWantToBypassEscaping2(SafeText):
class IWantToBypassEscaping3(SafeData):
# ok:class-extends-safestring
class SomethingElse(str):
