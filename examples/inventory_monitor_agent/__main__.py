"""
Entry point for running the Inventory Monitor Agent
"""

from agent import InventoryMonitorAgent


def main():
    """
    Main execution function.
    """

    # Create agent instance
    agent = InventoryMonitorAgent()

    # Sample inventory data
    inventory_data = {
        "bolts": 5,
        "nuts": 20,
        "washers": 3,
        "bearings": 15,
        "screws": 8
    }

    # Run inventory check
    result = agent.check_inventory(inventory_data)

    # Display result
    print("Low stock items:", result)


if __name__ == "__main__":
    main()