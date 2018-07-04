import pytest
import lzma

from hypothesis import given
import hypothesis.strategies as st

from my_lib import add_elements, get_gutenberg_text, word_count

@pytest.mark.parametrize("a,b,c", [
([1,2], [3,4], [4,6]),
([1,2], [3,5], [4,7])
]
)
def test_add_elements(a, b, c):
    assert add_elements(a, b) == c

def test_wrong_type():
    with pytest.raises(TypeError):
        add_elements([1,2], 3)

@pytest.fixture
def warandpeace():
    with lzma.open('warandpeace.txt.xz', mode='rt') as f:
        test = f.read()
        book_text = get_gutenberg_text(text)
    return book_text

def test_count_lines(warandpeace):
    assert len(warandpeace.split('\n')) == 65678


@given(st.lists(st.integers()), st.lists(st.integers())
def test_add_elements_2(a , b):
    assert add_elements(a, b) == 
