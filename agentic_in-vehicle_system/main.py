from agents.crew import VehicleMonitoringCrew

def run():
    """
    Entry point for running the in-vehicle monitoring system.
    """
    # Create an instance of the crew
    crew_instance = VehicleMonitoringCrew().crew()

    inputs = {
        "driver_image":   "scenario8/state.jpg",
        "child_image":    "scenario8/kids.jpg",
        "phone_image":    "scenario8/phone.webp",
        "seatbelt_image": "scenario8/seatbelt.jpg",
        "alcohol_image":  "scenario8/alcohol.jpg",
        "speed_value": 70
    }

    # Kick off the crew
    result = crew_instance.kickoff(inputs=inputs)
    print("Monitoring Results:")
    print(result)
