from django import forms


class LoginForm(forms.Form):
    qq = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "QQ", "required": "required", }),
                         max_length=20, error_messages={"required": "QQ不能为空", })
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required", }),
                               max_length=20, error_messages={"required": "密码不能为空", })
