from workshop_2 import User


def test_user_save():
    user = User(
        username='xyz',
        email='test@email.com',
        password='pyk'
    )
    # user_2 = User(
    #     username='abc',
    #     email='test@wp.pl',
    #     password='test'
    # )
    #
    # user = user.load_by_email('test@email.com')
    # user_2 = user_2.load_by_email(user_2.email)
    # print(user.id, user_2.id)
    # user_2.delete()
    user.load_all()