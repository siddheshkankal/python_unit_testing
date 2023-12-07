import string
import random
 
 
def generate_password():
    while True:
        password = "".join(
            random.choices(
                string.ascii_letters
                + string.digits
                + string.punctuation,
                k=12,
            )
        )
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
        ):
            return password
 
 
def test_generate_password():
    password = generate_password()
    assert len(password) >= 8, "1st failed"
    assert any(c.islower() for c in password), "2nd failed"
    assert any(c.isupper() for c in password), "3rd failed"
    assert any(c.isdigit() for c in password), "4th failed"
    assert any(c in string.punctuation for c in password), "5th failed"