from megaexnotes.core.utils import extract_amount, extract_date


def test_extract_amount_variations():
    assert extract_amount("Благотворительность - 600р") == 600.0
    assert extract_amount("10тр Миша") == 10000.0
    assert extract_amount("Стиралка - 20 000") == 20000.0
    assert extract_amount("без суммы") == 0.0

def test_extract_date_in_brackets():
    assert extract_date("Текст (29-01-2026) текст") == "(29-01-2026)"
    assert extract_date("Нет даты") is None
