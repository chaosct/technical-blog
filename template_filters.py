from __future__ import annotations

from datetime import datetime

CA_MONTHS = (
    "gener",
    "febrer",
    "març",
    "abril",
    "maig",
    "juny",
    "juliol",
    "agost",
    "setembre",
    "octubre",
    "novembre",
    "desembre",
)

EN_MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


def format_blog_date(value: datetime, lang: str = "ca") -> str:
    month_index = value.month - 1
    if lang == "ca":
        return f"{value.day} {CA_MONTHS[month_index]} {value.year}"
    return f"{value.day} {EN_MONTHS[month_index]} {value.year}"
