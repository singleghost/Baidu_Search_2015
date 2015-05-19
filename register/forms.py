#coding=utf-8
from django import forms

SEX_CHOICES = (('boy','男森'),('girl','女森'),)
class RegisterForm(forms.Form):
    team_name = forms.CharField(label='队伍名称',widget=forms.TextInput(attrs=
                    {'title':'队伍昵称',}))
    email = forms.EmailField(label ='E-mail(接收认证邮件)')
    m1_name = forms.CharField(label='队员1姓名')
    m1_sex = forms.ChoiceField(label='性别',choices=SEX_CHOICES)
    m1_phone_number = forms.IntegerField(label='手机号码')
    m1_phone_number_short = forms.IntegerField(label='短号(可选)',required=False)
    m1_profession = forms.CharField(label='专业(可选)',required=False)
    m1_student_id = forms.IntegerField(label='学号')
    m2_name = forms.CharField(label='队员2姓名')
    m2_sex = forms.ChoiceField(label='性别',choices=SEX_CHOICES)
    m2_phone_number = forms.IntegerField(label='手机号码')
    m2_phone_number_short = forms.IntegerField(label='短号(可选)',required=False)
    m2_profession = forms.CharField(label='专业(可选)',required=False)
    m2_student_id = forms.IntegerField(label='学号')
    m3_name = forms.CharField(label='队员3姓名')
    m3_sex = forms.ChoiceField(label='性别',choices=SEX_CHOICES)
    m3_phone_number = forms.IntegerField(label='手机号码')
    m3_phone_number_short = forms.IntegerField(label='短号(可选)',required=False)
    m3_profession = forms.CharField(label='专业(可选)',required=False)
    m3_student_id = forms.IntegerField(label='学号')
    account = forms.CharField(label='队伍账号')
    password = forms.CharField(label='队伍密码')
