__author__ = 'jinguangzhou'
from django.core.exceptions import ValidationError

from .constant import TELE_COUNTRY_CODE


def validate_country_code(code):
    """ validate whether country code is valid"""
    # whether is digit
    # length
    # whether is in country code list
    if not str(code).isdigit():
        msg = u'Country code must be digit'
        raise ValidationError(msg)
    if len(str(code)) > 3:
        msg = u'Country code must be less than three digits'
        raise ValidationError(msg)
    if len(str(code)) < 1:
        msg = u'Country code at least have one digit'
        raise ValidationError(msg)
    if int(code) not in TELE_COUNTRY_CODE.values():
        msg = u'{0} country code doesn\'t exist'.format(code)
        raise ValidationError(msg)


def validate_area_code(area_code):
    """Validate area code"""
    if not str(area_code).strip().isdigit():
        msg = u'Area code should be digit'
        raise ValidationError(msg)
    if len(str(area_code)) != 3:
        msg = u'Area code should have three digits. You can {0} digits.'.format(len(str(area_code)))
        raise ValidationError(msg)


def validate_remain_code(remain_code):
    """Validate remain code"""
    # Todo: test empty input
    if not str(remain_code).isdigit():
        msg = u'Remain code should be digits.'
        raise ValidationError(msg)
    if len(str(remain_code)) != 4:
        msg = u'Remain code should be 4 digits but you have {0}'.format(len(str(remain_code)))
        raise ValidationError(msg)
