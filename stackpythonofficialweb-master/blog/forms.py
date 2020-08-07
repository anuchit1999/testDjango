from django import forms
from .models import ContactUs # Comment
# from django.forms import ModelForm
from django.template.defaultfilters import slugify
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from captcha import fields
from captcha import widgets

"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ('name', 'email', 'body')
        fields = '__all__'
"""


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = '__all__'


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)


captcha = ReCaptchaField(
    public_key='6Lcb8uMUAAAAAAuiV5Ybj5CegQZzoUcx6FeHLm1C',
    private_key='6Lcb8uMUAAAAAPx4sL7qgZFp3AuwYUWAJ17uTVpy',
)


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)


captcha = fields.ReCaptchaField(
    widget=widgets.ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'dark',
            'data-size': 'compact',
        }
    )
)
# The ReCaptchaV2Invisible widget
# ignores the "data-size" attribute in favor of 'data-size="invisible"'


captcha = fields.ReCaptchaField(
    widget=widgets.ReCaptchaV2Checkbox(
        api_params={'hl': 'cl', 'onload': 'onLoadFunc'}
    )
)
# The dictionary is urlencoded and appended to the reCAPTCHA api url.


captcha = fields.ReCaptchaField(
    widget=ReCaptchaV2Invisible(
        attrs={
            'required_score':0.85,

        }
    )
)