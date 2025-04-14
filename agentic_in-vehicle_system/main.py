from agents.crew import VehicleMonitoringCrew

def run():
    """
    Entry point for running the in-vehicle monitoring system.
    """
    # Create an instance of the crew
    crew_instance = VehicleMonitoringCrew().crew()

    inputs = {
        "driver_image":   "dataset/scenarios/scenario20/state.jpg",
        "child_image":    "dataset/scenarios/scenario20/kids.webp",
        "phone_image":    "dataset/scenarios/scenario20/phone.jpg",
        "seatbelt_image": "dataset/scenarios/scenario20/seatbelt.webp",
        "alcohol_image":  "dataset/scenarios/scenario20/alcohol.jpg",
        "speed_value": 130
    }

    # Kick off the crew
    result = crew_instance.kickoff(inputs=inputs)
    print("Monitoring Results:")
    print(result)
