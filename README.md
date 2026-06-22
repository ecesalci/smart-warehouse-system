# Smart Warehouse Management System

This project is a robust, file-based warehouse management system developed in Python, fortified with comprehensive error handling.

## Features
- **User-Friendly:** You can cancel any operation and return to the main menu at any step by simply pressing 'Q'.
- **Robust Error Handling:** Input validation is strictly enforced to prevent negative stock/price entries or invalid data types.
- **Dynamic Reporting:** All data is instantly saved and categorized in an `Inventory_Report.txt` file.
- **Persistent Data:** Your inventory data is automatically loaded from the file upon startup, ensuring no data loss.
- **Admin Panel:** Specialized category-based price editing functionality.
- **Sorting:** Flexible sorting options for products by name (alphabetical) or by price.

## Menu Options
1. **Add Product:** Add new items to the inventory.
2. **Inventory Statistics:** View total value and category-based statistics.
3. **Critical Stock Alert:** Monitor items that fall below a specified threshold.
4. **Search Inventory:** Search by keyword or filter by price range.
5. **Stock Out:** Reduce stock quantities for existing items.
6. **Sort:** Sort products by price or name.
7. **Show Report:** Display the current inventory report.
8. **Edit Price:** Update product prices via a categorized management panel.
9. **Exit:** Close the application.

## Installation
1. Ensure you have Python installed on your system.
2. Download the project files.
3. Run the application from your terminal using: `python <filename>.py`

## Usage
Once the program is running, navigate through the menu by entering the corresponding numbers. The system features rigorous input validation; if you enter invalid data, it will prompt you to provide the correct information without crashing.