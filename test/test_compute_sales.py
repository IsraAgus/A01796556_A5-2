from pathlib import Path

from computeSales import (
    build_price_lookup,
    compute_total_cost,
    parse_sales_lines,
    read_json_file,
)


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _load_prices():
    catalog = read_json_file(DATA_DIR / "TC1.ProductList.json")
    return build_price_lookup(catalog)


def _run_case(sales_file: str) -> float:
    prices = _load_prices()
    sales = read_json_file(DATA_DIR / sales_file)
    lines = parse_sales_lines(sales)
    return round(compute_total_cost(prices, lines), 2)


def test_tc1_total():
    assert _run_case("TC1.Sales.json") == 2481.86


def test_tc2_total():
    assert _run_case("TC2.Sales.json") == 166568.23


def test_tc3_total():
    assert _run_case("TC3.Sales.json") == 165235.37