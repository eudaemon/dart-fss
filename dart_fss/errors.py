# -*- coding: utf-8 -*-

ERROR_CODE = {
    '000': 'OK',
    '010': 'Unregistered API key',
    '011': 'This API key is temporarily locked',
    '013': 'No data',
    '020': 'This API key is over query limit',
    '100': 'Invalid field',
    '800': 'Open API was closed for web service',
    '900': 'Unknown error'
}


def check_err_code(**kwargs) -> None:
    """ DART API 에서 전달받은 값의 오류를 체크하는 함수
    Parameters
    ----------
    kwargs: dict
        DART 서버에서 전달받은 값

    Raises
    ------
    DartException
        err_code 가 정상이 아닐때 발생하는 오류

    """
    err_code = kwargs.get('status')
    err_msg = kwargs.get('message')
    if err_code == '000' or err_code == '013':
        pass
    else:
        raise DartAPIError(err_code, err_msg)


class DartError(Exception):
    """ Dart Error """
    pass


class DartAPIError(DartError):
    """ DART API 에서 오류 메시지를 전송 받았을때 발생하는 오류 """
    def __init__(self, err_code, err_msg):
        if err_code not in ERROR_CODE:
            err_code = '900'
        message = '{}, {}'.format(ERROR_CODE[err_code], err_msg)
        super().__init__(message)


class NotFoundConsolidated(DartError):
    """ 연결재무제표가 없을때 발생하는 오류 """
    def __init__(self, err_msg='Could not find consolidated financial statements'):
        super().__init__(err_msg)

