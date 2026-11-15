import re

def extract_invoice_data(text):

    invoice_data = {}

    # Extract vendor name
    lines = text.strip().split("\n")
    invoice_data["Vendor"] = lines[0].strip() if lines else None

    # Invoice number
    match = re.search(
        r"Invoice\s*(?:Number|No\.?)\s*:\s*(.+)",
        text, re.IGNORECASE
    )
    invoice_data["Invoice Number"] = match.group(1).strip() if match else None

    # Date
    match = re.search(
        r"Date\s*:\s*(.+)",
        text, re.IGNORECASE
    )
    invoice_data["Date"] = match.group(1).strip() if match else None

    # Item
    match = re.search(
        r"Item\s*:\s*(.+)",
        text, re.IGNORECASE
    )
    invoice_data["Item"] = match.group(1).strip() if match else None

    # Quantity
    match = re.search(
        r"Quantity\s*:\s*(\d+)",
        text, re.IGNORECASE
    )
    invoice_data["Quantity"] = int(match.group(1)) if match else None

    # Price
    match = re.search(
        r"Price\s*:\s*₹?\s*([\d,]+(?:\.\d+)?)",
        text, re.IGNORECASE
    )
    invoice_data["Price"] = float(match.group(1).replace(",", "")) if match else None

    # Tax
    match = re.search(
        r"Tax\s*:\s*(\d+(?:\.\d+)?)\s*%",
        text, re.IGNORECASE
    )
    invoice_data["Tax"] = float(match.group(1)) if match else None

    # Total
    match = re.search(
        r"Total\s*:\s*₹?\s*([\d,]+(?:\.\d+)?)",
        text, re.IGNORECASE
    )
    invoice_data["Total"] = float(match.group(1).replace(",", "")) if match else None

    return invoice_data