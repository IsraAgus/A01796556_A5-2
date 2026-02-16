"""
computeSales.py

Actividad 5.2 - Compute Sales
- Invocación:
    python computeSales.py priceCatalogue.json salesRecord.json

El programa:
1) Lee un catálogo de productos (JSON: lista de objetos con 'title' y 'price').
2) Lee un registro de ventas (JSON: lista de objetos con 'Product' y 'Quantity').
3) Calcula el costo total (sum(price[Product] * Quantity)).
4) Maneja datos inválidos: reporta en consola y continúa.
5) Imprime resultados en consola y guarda SalesResults.txt incluyendo tiempo
   transcurrido.
"""

from __future__ import annotations

import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


RESULTS_FILE = "SalesResults.txt"


@dataclass(frozen=True)
class SaleLine:
    """Representa una línea de venta validada."""

    product: str
    quantity: float


def read_json_file(path: Path) -> Any:
    """Lee un archivo JSON y devuelve el objeto parseado.

    Si el archivo no existe o el JSON es inválido, levanta excepción.
    """
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_price_lookup(catalog_data: Any) -> dict[str, float]:
    """Construye un diccionario {product_title: price} desde el catálogo.

    El catálogo esperado es una lista de objetos con llaves:
    - title (str)
    - price (numérico)
    Cualquier registro inválido se ignora y se reporta.
    """
    prices: dict[str, float] = {}

    if not isinstance(catalog_data, list):
        raise ValueError("Price catalogue JSON must be a list of products.")

    for idx, item in enumerate(catalog_data):
        if not isinstance(item, dict):
            print(f"[CATALOG ERROR] Item {idx} is not an object. Skipping.")
            continue

        title = item.get("title")
        price = item.get("price")

        if not isinstance(title, str) or not title.strip():
            print(f"[CATALOG ERROR] Item {idx} missing valid 'title'. Skipping.")
            continue

        if not isinstance(price, (int, float)):
            msg = (
                f"[CATALOG ERROR] Item {idx} '{title}' missing valid 'price'. "
                "Skipping."
            )
            print(msg)
            continue

        prices[title] = float(price)

    return prices


def parse_sales_lines(sales_data: Any) -> list[SaleLine]:
    """Parsea el JSON de ventas a una lista de SaleLine validada.

    Ventas esperadas: lista de objetos con:
    - Product (str)
    - Quantity (numérico)
    Registros inválidos se reportan y se omiten.
    """
    lines: list[SaleLine] = []

    if not isinstance(sales_data, list):
        raise ValueError("Sales record JSON must be a list of sales lines.")

    for idx, item in enumerate(sales_data):
        if not isinstance(item, dict):
            print(f"[SALES ERROR] Line {idx} is not an object. Skipping.")
            continue

        product = item.get("Product")
        quantity = item.get("Quantity")

        if not isinstance(product, str) or not product.strip():
            print(f"[SALES ERROR] Line {idx} missing valid 'Product'. Skipping.")
            continue

        if not isinstance(quantity, (int, float)):
            msg = (
                f"[SALES ERROR] Line {idx} '{product}' missing valid 'Quantity'. "
                "Skipping."
            )
            print(msg)
            continue

        lines.append(SaleLine(product=product, quantity=float(quantity)))

    return lines


def compute_total_cost(prices: dict[str, float], sales_lines: list[SaleLine]) -> float:
    """Calcula el total.

    Si el producto no existe en el catálogo, reporta y continúa.
    """
    total = 0.0

    for idx, line in enumerate(sales_lines):
        if line.product not in prices:
            msg = (
                f"[MISSING PRODUCT] Line {idx}: '{line.product}' not found in "
                "catalogue. Skipping."
            )
            print(msg)
            continue

        total += prices[line.product] * line.quantity

    return total


def format_report(total: float, elapsed_seconds: float) -> str:
    """Genera una salida human-readable."""
    return (
        "Sales Results\n"
        "=============\n"
        f"Total cost: ${total:,.2f}\n"
        f"Elapsed time: {elapsed_seconds:.6f} seconds\n"
    )


def write_results(report: str, output_path: Path) -> None:
    """Escribe el reporte a archivo."""
    output_path.write_text(report, encoding="utf-8")


def main(argv: list[str]) -> int:
    """Punto de entrada CLI."""
    if len(argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        return 1

    catalog_path = Path(argv[1])
    sales_path = Path(argv[2])

    start = time.perf_counter()

    try:
        catalog_data = read_json_file(catalog_path)
        prices = build_price_lookup(catalog_data)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"[FATAL] Cannot load price catalogue: {exc}")
        return 1

    try:
        sales_data = read_json_file(sales_path)
        sales_lines = parse_sales_lines(sales_data)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"[FATAL] Cannot load sales record: {exc}")
        return 1

    total = compute_total_cost(prices, sales_lines)

    elapsed = time.perf_counter() - start
    report = format_report(total=total, elapsed_seconds=elapsed)

    print(report)
    write_results(report, Path(RESULTS_FILE))

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
