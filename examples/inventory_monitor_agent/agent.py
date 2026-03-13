


class InventoryMonitorAgent:
    def __init__(self):
        self.threshold =10

    def check_inventory(self, inventory):
        low_stock_items = []

        for item, quantity in inventory.items():
            if quantity < self.threshold:
                low_stock_items.append(item)

        return low_stock_items


if __name__ == "__main__":
    agent = InventoryMonitorAgent()

    inventory_data = {
        "bolts": 5, 
        "nuts": 20,
        "washers": 3,
        "bearings": 15
    }

    result = agent.check_inventory(inventory_data)

    print("Low stock items:", result)