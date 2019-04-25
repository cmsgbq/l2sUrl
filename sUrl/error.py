# -*- coding: utf-8 -*-


from pymaid.error import ErrorManager

__all__ = ['sUrlError']


sUrlError = ErrorManager.create_manager('sUrlError', 7000)

sUrlError.add_error(
    'UrlHasExist', 1, u'[长url已存在|{}]'
)
sUrlError.add_error(
    'UrlNotExist', 2, u'[短url不存在|{}]'
)
# PaymentError.add_error(
#     'DeleteChargeCardTemplateError', 3, u'[DeleteChargeCardTemplateError|{}]'
# )
# PaymentError.add_error(
#     'AmountError', 4, u'[AmountError|{}]'
# )
