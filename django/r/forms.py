import os
import sys

from django.core import validators

from splunkdj.setup import forms


# allow imports from bin directory
bin_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'bin')
sys.path += bin_path

import framework as frameworklib


class RPathValidator(object):
    def __call__(self, value):
        def raise_error(msg):
            raise validators.ValidationError(msg)

        frameworklib.verify_r_path(value, raise_error)


class RPathField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(RPathField, self).__init__(*args, **kwargs)
        self.validators.append(RPathValidator())


class SetupForm(forms.Form):
    r_path = RPathField(
        endpoint='configs/conf-r',
        entity='paths',
        field='r',
        label='Please specify the library installation path:',
    )
    csv_read_options = forms.CharField(
        endpoint='configs/conf-r',
        entity='csv',
        field='read-options',
        label='Please indicate the options for read.csv:',
        help_text='For the full list of options, please see the '
                  '<a target="_blank" href="http://cran.r-project.org/doc/manuals/r-release/fullrefman.pdf">'
                  'R reference manual</a> under read.csv and write.csv.',
        required=False,
    )
    csv_write_options = forms.CharField(
        endpoint='configs/conf-r',
        entity='csv',
        field='write-options',
        label='Please indicate the options for write.csv:',
        #help_text='For the full list of options, please see the '
        #          '<a target="_blank" href="http://cran.r-project.org/doc/manuals/r-release/fullrefman.pdf">'
        #          'R reference manual</a> under read.csv and write.csv.',
        required=False,
    )