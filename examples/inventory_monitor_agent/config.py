"""
Configuration file for the Inventory Monitor Agent
This file stores parameters used by the agent.
"""


class InventoryConfig:
    """
    Configuration class for inventory monitoring settings.
    """

    def __init__(self):
        # Threshold below which an item is considered low stock
        self.stock_threshold = 10

        # Name of the agent
        self.agent_name = "Inventory Monitor Agent"

        # Version of the agent
        self.version = "1.0"

        # Author of the agent
        self.author = "Durvesh Hedau"

    def display_config(self):
        """
        Display the configuration details.
        """

        print("Agent Name:", self.agent_name)
        print("Version:", self.version)
        print("Author:", self.author)
        print("Stock Threshold:", self.stock_threshold)