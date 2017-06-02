from workshop_2 import User


def test_user_save():
    user = User(
        username='test',
        email='test@email.com',
        password='pass'
    )

    # a = user.save()
    # assert a=='dodano do bazy'

    loaded_user = User.load_by_email(email='test@email.com')
    assert loaded_user.username == 'test'
    assert loaded_user.email == 'test@email.com'