from .models import *
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='パスワードの確認', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'is_adviser', 'birth', 'gender', 'height', 'is_admin', 'bone_type', 'color_type')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("パスワードが間違っています")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password',
                  'is_active', 'is_admin', 'username', 'first_name', 'last_name', 'is_adviser', 'birth', 'gender', 'height', 'bone_type', 'color_type')

    def clean_password(self):
        return self.initial["password"]

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'gender', 'height', 'is_adviser', 'bone_type', 'color_type')

    def clean_password(self):
        return self.initial["password"]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='必須  有効なメールアドレスを入力してください。',
        label='Eメールアドレス',
    )

    username = forms.CharField(
        max_length=30,
        required=True,
        help_text='必須',
        label='ユーザーネーム'
    )

    last_name = forms.CharField(
        max_length=20,
        required=True,
        help_text="必須",
        label='性'
    )

    first_name = forms.CharField(
        max_length=20,
        required=True,
        help_text="必須",
        label='名'
    )

    birth = forms.DateField(
        widget=forms.SelectDateWidget(),
        required=True,
        help_text='必須',
        label='生年月日'
    )

    GENDER = (
        ("男性", "男性"),
        ("女性", "女性"),
        ("その他", "その他")
    )
    gender = forms.ChoiceField(
        choices=GENDER,
        required=True,
        help_text='必須',
        label='性別'
    )

    is_adviser = forms.BooleanField(
        required=False,
        label='アドバイザーとして登録する場合はチェックを入れてください',
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'birth', 'gender', 'height', 'is_adviser', 'password1', 'password2', )
    
    def __init__(self, year, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if year != None:
            self.fields["birth"].widget = forms.SelectDateWidget(years=range(1910, year))

class AdviserEditForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Adviser
        fields = ('profile', 'is_active', 'profile_pic', 'instagram', 'wear', 'tiktok', 'twitter', 'facebook', 'hp')

class LoginForm(forms.Form):
    email = forms.CharField(label='メールアドレス', max_length=30)
    password = forms.CharField(
            label='パスワード', max_length=128, widget=forms.PasswordInput())

class ReviewForm(forms.ModelForm):   
    class Meta:
        model = Review
        fields = ['score', 'comment']

class BoneMenTest(forms.Form):
    ONE = (
        (0, 'A.上半身は厚くがっちりしていて、身体にメリハリがある'),
        (1, 'B.身体は薄くスタイリッシュで、ラインが柔らかい'),
        (2, 'C.骨格のフレームがしっかりしていて、各関節が大きい')
    )
    one = forms.ChoiceField(choices=ONE, label='全体的な身体の印象は？')

    TWO = (
        (0, 'A.少量のトレーニングで筋肉がつきやすい'),
        (1, 'B.筋肉よりも脂肪がつきやすく、筋トレの効果を感じにくい'),
        (2, 'C.肉感というより骨感が強い')
    )
    two = forms.ChoiceField(choices=TWO, label='筋肉や脂肪の付き方は？')

    THREE = (
        (0, 'A.肌は弾力があり、触るとハリのある質感'),
        (1, 'B.肌は薄く、ソフトな質感'),
        (2, 'C.肌質は硬く、筋が目立つ')
    )
    three = forms.ChoiceField(choices=THREE, label='身体の肌の質感は？')

    FOUR = (
        (0, 'A.どちらかというと、首は短め'),
        (1, 'B.どちらかというと、首はすらっと長め'),
        (2, 'C.首はやや太く、首筋が目立つ')
    )
    four = forms.ChoiceField(choices=FOUR, label='首の長さや特徴は？')

    FIVE = (
        (0, 'A.鎖骨はほとんど目立たない'),
        (1, 'B.鎖骨は細く、やや目立つ'),
        (2, 'C.鎖骨はしっかり出ていて、服の上からでもわかる')
    )
    five = forms.ChoiceField(choices=FIVE, label='鎖骨の大きさや出方は？')

    SIX = (
        (0, 'A.手首は肉感があり、骨はあまり出ていない'),
        (1, 'B.手首は細く、骨は少し出ている'),
        (2, 'C.手首は細いが、骨がしっかり出ている')
    )
    six = forms.ChoiceField(choices=SIX, label='手首の骨の大きさや出方は？')

    SEVEN = (
        (0, 'A.腰位置が高く、お尻は丸みがあり立体的'),
        (1, 'B.腰位置が低く、お尻はなだらかに下がって見える'),
        (2, 'C.腰位置が高く、お尻は小さく平面的')
    )
    seven = forms.ChoiceField(choices=SEVEN, label='ヒップラインやおしりの形は？')

    EIGHT = (
        (0, 'A.膝は小さく丸く、あまり出ていない'),
        (1, 'B.膝は小さく丸く、少し出ている'),
        (2, 'C.膝の関節が大きく、丸いというより縦に長い感じ')
    )
    eight = forms.ChoiceField(choices=EIGHT, label='膝の大きさや形の特徴、出方は？')

    NINE = (
        (0, 'A.厚手素材やストレッチ素材の服、オーバーサイズの服は着太りして見える'),
        (1, 'B.胸元が大きく開いたトップスは物足りない。大きい服に着られる。'),
        (2, 'C.ジャストサイズや丈が短い服を着ると、バランスが悪くなる')
    )
    nine = forms.ChoiceField(choices=NINE, label='苦手な服装は？')

class BoneWomenTest(forms.Form):
    ONE = (
        (0, 'A. ヒップやバストが大きく、ボリュームのある体型'),
        (1, 'B. 上半身より下半身に肉がつきやすく下重心の体型'),
        (2, 'C. あまり肉は付かないが骨がしっかりと目立つ骨太体型')
    )
    one = forms.ChoiceField(choices=ONE, label='全体的な身体の印象は？')

    TWO = (
        (0, 'A. 首はやや短め、撫で肩気味'),
        (1, 'B. 首は細くて長め、肩のラインはあまり気にならない'),
        (2, 'C. 首はやや長めで筋が見える、肩幅が大きく見える')
    )
    two = forms.ChoiceField(choices=TWO, label='首から肩にかけての特徴は？')

    THREE = (
        (0, 'A. 腰位置が高い'),
        (1, 'B. 腰位置が低い'),
        (2, 'C. 腰位置は普通')
    )
    three = forms.ChoiceField(choices=THREE, label='腰の位置は？')

    FOUR = (
        (0, 'A. 胸板が厚く横から見ると立体的で傾斜がある'),
        (1, 'B. 横から見るとなだらかで薄い'),
        (2, 'C. どちらでもない')
    )
    four = forms.ChoiceField(choices=FOUR, label='胸板の厚みは？')

    FIVE = (
        (0, 'A. 手の平に厚みがある'),
        (1, 'B. 手の平はうすい'),
        (2, 'C. 厚さよりも、手の甲が筋っぽいのが目立つ')
    )
    five = forms.ChoiceField(choices=FIVE, label='手の平、甲の特徴は？')

    SIX = (
        (0, 'A. 小さい'),
        (1, 'B. 普通'),
        (2, 'C. 大きい')
    )
    six = forms.ChoiceField(choices=SIX, label='指の関節の大きさは?')

    SEVEN = (
        (0, 'A. くびれがあまりない'),
        (1, 'B. くびれがわかりやすい'),
        (2, 'C. どちらでもない')
    )
    seven = forms.ChoiceField(choices=SEVEN, label='ウエストの特徴は？')

    EIGHT = (
        (0, 'A. 太ももは太くひざ下は細い、骨はまっすぐ'),
        (1, 'B. 太ももは細くひざ下は太い、すねは外部に湾曲しやすい'),
        (2, 'C. 太ももにはあまり肉はつかず、すねの骨は太い')
    )
    eight = forms.ChoiceField(choices=EIGHT, label='太もも、ひざ下の特徴は？')

    NINE = (
        (0, 'A. 筋肉がつきやすい'),
        (1, 'B. 筋肉がつきにくい'),
        (2, 'C. 筋肉がつきにくく、骨太な印象が強い')
    )
    nine = forms.ChoiceField(choices=NINE, label='筋肉はつきやすい？')

class ColorTest(forms.Form):
    ONE = (
        (0, 'A. 猫っ毛で量は少なめ	'),
        (1, 'B. 量は普通～多め'),
        (2, 'C. 量は少なめ～普通'),
        (3, 'D. 量は多い')
    )
    one = forms.ChoiceField(choices=ONE, label='髪の量は？')

    TWO = (
        (0, 'A. 艶があり、ハリがない'),
        (1, 'B. 艶がなく、ハリがある'),
        (2, 'C. 艶もハリも少なめ'),
        (3, 'D. 艶もハリもある')
    )
    two = forms.ChoiceField(choices=TWO, label='髪質は？')

    THREE = (
        (0, 'A. 明るく透明感のある黄みの茶色'),
        (1, 'B. やや赤みのこげ茶または ソフトな黒'),
        (2, 'C. 橙がかったこげ茶または緑がかった焦茶'),
        (3, 'D. 強い印象の真っ黒')
    )
    three = forms.ChoiceField(choices=THREE, label='髪色は？')

    FOUR = (
        (0, 'A. 透明感とつやがある'),
        (1, 'B. ノーマル～オイリーな肌質'),
        (2, 'C. 皮膚が薄くパウダリーな質感'),
        (3, 'D. とても色白またはとても色黒でキメが細かい')
    )
    four = forms.ChoiceField(choices=FOUR, label='肌質は？')

    FIVE = (
        (0, 'A. 橙がかったピンク'),
        (1, 'B. 薄い青みのピンクまたは赤紫'),
        (2, 'C. 赤みが少ないまたは茶がかった赤紫'),
        (3, 'D. 冴えたピンク または赤黒い感じ')
    )
    five = forms.ChoiceField(choices=FIVE, label='頬、唇の色は？')

    SIX = (
        (0, 'A. 明るい茶色'),
        (1, 'B. 赤みのこげ茶またはグレイッシュな黒'),
        (2, 'C. 緑みのこげ茶'),
        (3, 'D. はっきりした黒')
    )
    six = forms.ChoiceField(choices=SIX, label='目の色は？')

    SEVEN = (
        (0, 'A. 明るくて可愛らしい'),
        (1, 'B. 上品で涼やか'),
        (2, 'C. 落ち着いて大人っぽい'),
        (3, 'D. 個性的で印象深い')
    )
    seven = forms.ChoiceField(choices=SEVEN, label='印象は？')

    EIGHT = (
        (0, 'A. 丸型or卵型'),
        (1, 'B. 面長or丸くやや骨ばっている'),
        (2, 'C. 長四角orしもぶくれorえらが張っている'),
        (3, 'D. ベース型orダイヤ型or小さい角型')
    )
    eight = forms.ChoiceField(choices=EIGHT, label='輪郭は？')

    NINE = (
        (0, 'A. 丸いor垂れ目orはにわ目'),
        (1, 'B. リーフ型or半月型or切れ長'),
        (2, 'C. 猫目or涙道が膨らんでいるor瞼の皮膚が薄い'),
        (3, 'D. 大きくて上昇してるorとても切れ長orとがった三角目')
    )
    nine = forms.ChoiceField(choices=NINE, label='目の形は？')

    TEN = (
        (0, 'A. 小さくて下が厚いor輪郭がぼんやり'),
        (1, 'B. 上の山がくっきりしていて薄いor輪郭がソフトで厚い'),
        (2, 'C. 広くて両端下がりor広くて上下とも薄い'),
        (3, 'D. 大きくて厚いorとても薄い')
    )
    ten = forms.ChoiceField(choices=TEN, label='唇の形は？')

    ELEVEN = (
        (0, 'A. 低めで小さい'),
        (1, 'B. 細長い'),
        (2, 'C. 丸くて大きい'),
        (3, 'D. とても高いorとても低い')
    )
    eleven = forms.ChoiceField(choices=ELEVEN, label='鼻は？')

    TWELVE = (
        (0, 'A. なで肩で全体に丸みがある'),
        (1, 'B. 他のどれにもあてはまらない'),
        (2, 'C. いかり肩で腰に丸みがある'),
        (3, 'D. 直線的でボーイッシュ')
    )
    twelve = forms.ChoiceField(choices=TWELVE, label='体型は？')

class new_conv(forms.Form):
    body = forms.CharField(required=False, widget=forms.Textarea)
    CHOICES = (
        ('お任せコーデ提案', 'お任せコーデ提案'),
        ('自分の持っている服の着合わせアドバイス', '自分の持っている服の着合わせアドバイス'),
        ('服選びのコツ伝授', '服選びのコツ伝授'),
        ('その他', 'その他')
    )
    order = forms.MultipleChoiceField(choices=CHOICES, required=True, widget=forms.CheckboxSelectMultiple)
    other = forms.CharField(required=False)
    price = forms.CharField(required=False)
