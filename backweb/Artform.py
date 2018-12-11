from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=3, required=True,
                            error_messages={
                                'required':'请填写标题',
                                'min_length':'文章标题不能少于3个字符'
                            })
    content = forms.CharField(min_length=5, required=True,
                              error_messages={
                                  'required':'文章内容必填'
                              })
    icon = forms.ImageField(required=True, error_messages={'required':'首图必填'})


class EditArtForm(forms.Form):
    title = forms.CharField(min_length=3, required=True,
                            error_messages={
                                'required':'请填写标题',
                                'min_length':'文章标题不能少于3个字符'
                            })
    content = forms.CharField(min_length=5, required=True,
                              error_messages={
                                  'required':'文章内容必填'
                              })
    icon = forms.ImageField(required=False)
