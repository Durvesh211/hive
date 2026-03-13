# Inventory Monitor Agent

## Overview

The **Inventory Monitor Agent** is an example Hive agent that monitors inventory levels and detects items that fall below a defined stock threshold.

This agent demonstrates a simple business automation workflow where an autonomous agent checks inventory data and identifies low-stock items that may require restocking.

## Features

* Monitors inventory levels
* Detects items below a predefined threshold
* Generates a report of low-stock items
* Demonstrates a simple Hive agent implementation

## Agent Workflow

The agent follows this workflow:

1. Load inventory data
2. Check each item's quantity
3. Compare the quantity against a threshold value
4. Identify items with low stock
5. Generate a list of items requiring restocking

## Example Inventory Data

```
{
 "bolts": 5,
 "nuts": 20,
 "washers": 3,
 "bearings": 15
}
```

## Expected Output

```
Low stock items: ['bolts', 'washers']
```

## How to Run

From the agent directory run:

```
python agent.py
```

or

```
python -m inventory_monitor_agent
```

## Use Case

This agent demonstrates how Hive agents can automate **business processes**, such as:

* Supply chain monitoring
* Inventory alerts
* Automated stock reporting

## Author

Durvesh Hedau
