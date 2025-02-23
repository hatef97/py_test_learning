import time
import pytest

from person import Person


class TestPerson:
    @pytest.fixture
    def setup(self):
        self.p1 = Person('hatef', 'barin')
        self.p2 = Person('john', 'wick')
        yield 'setup'
        time.sleep(2)

    def test_fullname(self, setup):
        assert self.p1.fullname() == 'hatef barin'
        assert self.p2.fullname() == 'john wick'

    def test_email(self, setup):
        assert self.p1.email() == 'hatefbarin@email.com'
        assert self.p2.email() == 'johnwick@email.com'
