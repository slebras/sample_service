from pytest import raises

from SampleService.core.acls import SampleACL, SampleACLOwnerless
from core.test_utils import assert_exception_correct


def test_build_ownerless():
    a = SampleACLOwnerless()
    assert a.admin == ()
    assert a.write == ()
    assert a.read == ()

    a = SampleACLOwnerless(['baz', 'bat'], read=['wheee'], write=['wugga', 'a', 'b'])
    assert a.admin == ('baz', 'bat')
    assert a.write == ('wugga', 'a', 'b')
    assert a.read == ('wheee',)


def test_build_fail_ownerless():
    _build_fail_ownerless(['a', ''], None, None, ValueError(
        'Index 1 of iterable admin cannot be a value that evaluates to false'))
    _build_fail_ownerless(None, ['', ''], None, ValueError(
        'Index 0 of iterable write cannot be a value that evaluates to false'))
    _build_fail_ownerless(None, None, ['a', 'b', ''], ValueError(
        'Index 2 of iterable read cannot be a value that evaluates to false'))


def _build_fail_ownerless(admin, write, read, expected):
    with raises(Exception) as got:
        SampleACLOwnerless(admin, write, read)
    assert_exception_correct(got.value, expected)


def test_eq_ownerless():
    assert SampleACLOwnerless(['bar']) == SampleACLOwnerless(['bar'])
    assert SampleACLOwnerless(['bar']) != SampleACLOwnerless(['baz'])

    assert SampleACLOwnerless(write=['bar']) == SampleACLOwnerless(write=['bar'])
    assert SampleACLOwnerless(write=['bar']) != SampleACLOwnerless(write=['baz'])

    assert SampleACLOwnerless(read=['bar']) == SampleACLOwnerless(read=['bar'])
    assert SampleACLOwnerless(read=['bar']) != SampleACLOwnerless(read=['baz'])

    assert SampleACLOwnerless('foo') != 1
    assert 'foo' != SampleACLOwnerless('foo')


def test_hash():
    # hashes will change from instance to instance of the python interpreter, and therefore
    # tests can't be written that directly test the hash value. See
    # https://docs.python.org/3/reference/datamodel.html#object.__hash__

    assert hash(SampleACLOwnerless(['bar'])) == hash(SampleACLOwnerless(['bar']))
    assert hash(SampleACLOwnerless(['bar'])) != hash(SampleACLOwnerless(['baz']))

    assert hash(SampleACLOwnerless(write=['bar'])) == hash(SampleACLOwnerless(write=['bar']))
    assert hash(SampleACLOwnerless(write=['bar'])) != hash(SampleACLOwnerless(write=['baz']))

    assert hash(SampleACLOwnerless(read=['bar'])) == hash(SampleACLOwnerless(read=['bar']))
    assert hash(SampleACLOwnerless(read=['bar'])) != hash(SampleACLOwnerless(read=['baz']))


def test_build():
    a = SampleACL('foo')
    assert a.owner == 'foo'
    assert a.admin == ()
    assert a.write == ()
    assert a.read == ()

    a = SampleACL('foo', ['baz', 'bat'], read=['wheee'], write=['wugga', 'a', 'b'])
    assert a.owner == 'foo'
    assert a.admin == ('baz', 'bat')
    assert a.write == ('wugga', 'a', 'b')
    assert a.read == ('wheee',)


def test_build_fail():
    _build_fail('', None, None, None, ValueError(
        'owner cannot be a value that evaluates to false'))
    _build_fail('foo', ['a', ''], None, None, ValueError(
        'Index 1 of iterable admin cannot be a value that evaluates to false'))
    _build_fail('foo', None, ['', ''], None, ValueError(
        'Index 0 of iterable write cannot be a value that evaluates to false'))
    _build_fail('foo', None, None, ['a', 'b', ''], ValueError(
        'Index 2 of iterable read cannot be a value that evaluates to false'))


def _build_fail(owner, admin, write, read, expected):
    with raises(Exception) as got:
        SampleACL(owner, admin, write, read)
    assert_exception_correct(got.value, expected)


def test_eq():
    assert SampleACL('foo') == SampleACL('foo')
    assert SampleACL('foo') != SampleACL('bar')

    assert SampleACL('foo', ['bar']) == SampleACL('foo', ['bar'])
    assert SampleACL('foo', ['bar']) != SampleACL('foo', ['baz'])

    assert SampleACL('foo', write=['bar']) == SampleACL('foo', write=['bar'])
    assert SampleACL('foo', write=['bar']) != SampleACL('foo', write=['baz'])

    assert SampleACL('foo', read=['bar']) == SampleACL('foo', read=['bar'])
    assert SampleACL('foo', read=['bar']) != SampleACL('foo', read=['baz'])

    assert SampleACL('foo') != 1
    assert 'foo' != SampleACL('foo')


def test_hash():
    # hashes will change from instance to instance of the python interpreter, and therefore
    # tests can't be written that directly test the hash value. See
    # https://docs.python.org/3/reference/datamodel.html#object.__hash__

    assert hash(SampleACL('foo')) == hash(SampleACL('foo'))
    assert hash(SampleACL('bar')) == hash(SampleACL('bar'))
    assert hash(SampleACL('foo')) != hash(SampleACL('bar'))

    assert hash(SampleACL('foo', ['bar'])) == hash(SampleACL('foo', ['bar']))
    assert hash(SampleACL('foo', ['bar'])) != hash(SampleACL('foo', ['baz']))

    assert hash(SampleACL('foo', write=['bar'])) == hash(SampleACL('foo', write=['bar']))
    assert hash(SampleACL('foo', write=['bar'])) != hash(SampleACL('foo', write=['baz']))

    assert hash(SampleACL('foo', read=['bar'])) == hash(SampleACL('foo', read=['bar']))
    assert hash(SampleACL('foo', read=['bar'])) != hash(SampleACL('foo', read=['baz']))
