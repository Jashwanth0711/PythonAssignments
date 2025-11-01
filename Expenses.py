# Expense Tracker - Monthly Summary
# Reads expenses from a CSV file and creates a summary report

def read_expenses(filename):
    """Read expense records from file and return as a list"""
    records = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()  # remove extra spaces/newlines

                if not line:  # skip blank lines
                    continue

                try:
                    date, category, amount = line.split(",")
                    amount = float(amount)
                except ValueError:
                    print("Skipping invalid line:", line)
                    continue

                records.append({
                    "date": date,
                    "category": category,
                    "amount": amount
                })

    except FileNotFoundError:
        print("File not found! Please check the filename.")
        return []

    return records


def calculate_summary(records):
    """Calculate total, category-wise, and highest day expenses"""
    if not records:
        return None

    total_expense = 0
    category_totals = {}
    day_totals = {}

    for item in records:
        date = item["date"]
        category = item["category"]
        amount = item["amount"]

        total_expense += amount

    
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += amount

  
        if date not in day_totals:
            day_totals[date] = 0
        day_totals[date] += amount

    highest_day = max(day_totals, key=day_totals.get)
    highest_amount = day_totals[highest_day]

    summary = {
        "total": total_expense,
        "categories": category_totals,
        "highest_day": highest_day,
        "highest_amount": highest_amount
    }

    return summary


def write_summary(summary, filename):
    """Write monthly summary report to a file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("================= Expense Summary (October 2025) =================\n")
        file.write(f"Total Monthly Expense: ₹{summary['total']:.0f}\n\n")

        file.write("Category-wise Breakdown:\n")
        for cat, amt in summary["categories"].items():
            file.write(f"{cat:<15}: ₹{amt:.0f}\n")

        file.write(f"\nHighest Spending Day: {summary['highest_day']} (₹{summary['highest_amount']:.0f})\n")
        file.write("=================================================================\n")


records = read_expenses("expenses.csv")

if records:
    summary = calculate_summary(records)
    write_summary(summary, "monthly_summary.txt")
    print("Monthly summary generated successfully! Check 'monthly_summary.txt'")
else:
    print("No data found to process.")
