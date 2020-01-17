from django import forms


class QuestionForm(forms.Form):
    fresh = forms.ChoiceField(
        label='참신함',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }),
        choices=[(5, '5점'),
                 (4, '4점'),
                 (3, '3점'),
                 (2, '2점'),
                 (1, '1점'),
                 (0, '0점')]
    )

    complete = forms.ChoiceField(
        label='완성도',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }),
        choices=[(5, '5점'),
                 (4, '4점'),
                 (3, '3점'),
                 (2, '2점'),
                 (1, '1점'),
                 (0, '0점')]
    )

    interest = forms.ChoiceField(
        label='흥미도',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }),
        choices=[(5, '5점'),
                 (4, '4점'),
                 (3, '3점'),
                 (2, '2점'),
                 (1, '1점'),
                 (0, '0점')]
    )

    need = forms.ChoiceField(
        label='필요성',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }),
        choices=[(5, '5점'),
                 (4, '4점'),
                 (3, '3점'),
                 (2, '2점'),
                 (1, '1점'),
                 (0, '0점')]
    )
