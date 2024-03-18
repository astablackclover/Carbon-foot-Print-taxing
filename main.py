class CarbonTaxCalculator:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name, carbon_footprint):
        self.products[product_name] = carbon_footprint

    def calculate_tax(self):
        total_carbon_footprint = sum(self.products.values())
        tax_rate = 0.05  # 5% tax rate
        tax_amount = total_carbon_footprint * tax_rate
        return tax_amount

    def display_products(self):
        print("\nProducts and their Carbon Footprints:")
        for product, footprint in self.products.items():
            print(f"{product}: {footprint} pounds of CO2")


def main():
    calculator = CarbonTaxCalculator()

    # Collect product information from the user
    while True:
        product_name = input("Enter product name (or 'done' to finish): ").strip()
        if product_name.lower() == "done":
            break
        try:
            carbon_footprint = float(input("Enter carbon footprint emitted by the product (in pounds of CO2): "))
            calculator.add_product(product_name, carbon_footprint)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Calculate and display tax amount
    tax_amount = calculator.calculate_tax()
    print(f"\nTotal Carbon Tax Amount: ${tax_amount:.2f}")

    # Display products and their carbon footprints
    calculator.display_products()


if __name__ == "__main__":
    main()
