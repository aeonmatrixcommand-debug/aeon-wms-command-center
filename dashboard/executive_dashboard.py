class ExecutiveDashboard:

    def get_status(self):

        return {
            "warehouse_health": 95,
            "OTIF": "98.5%",
            "inventory_accuracy": "99.2%",
            "dock_risk": "LOW",
            "AI_status": "ACTIVE"
        }


if __name__ == "__main__":

    dashboard = ExecutiveDashboard()

    print(dashboard.get_status())
