# -*- coding: utf-8 -*-
"""Фильтр алертов: из 8 событий оставляем только critical.
Запуск: python3 alerts.py
"""
import json


def main():
    with open("events.json", encoding="utf-8") as f:
        события = json.load(f)

    критичные = [e for e in события if e["level"] == "critical"]

    for e in критичные:
        print(f'[{e["level"].upper()}] #{e["id"]} {e["message"]}')

    print(f"критичных {len(критичные)}")


if __name__ == "__main__":
    main()
