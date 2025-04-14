from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from agents.tools.custom_tool import Base64ImageClassifierTool

@CrewBase
class VehicleMonitoringCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def driver_state_agent(self):
        return Agent(
            config=self.agents_config["driver_state_agent"],
            tools=[Base64ImageClassifierTool()]
        )

    @agent
    def child_occupancy_agent(self):
        return Agent(
            config=self.agents_config["child_occupancy_agent"],
            tools=[Base64ImageClassifierTool()]
        )

    @agent
    def phone_usage_agent(self):
        return Agent(
            config=self.agents_config["phone_usage_agent"],
            tools=[Base64ImageClassifierTool()]
        )

    @agent
    def seatbelt_usage_agent(self):
        return Agent(
            config=self.agents_config["seatbelt_usage_agent"],
            tools=[Base64ImageClassifierTool()]
        )

    @agent
    def alcohol_presence_agent(self):
        return Agent(
            config=self.agents_config["alcohol_presence_agent"],
            tools=[Base64ImageClassifierTool()]
        )

    @agent
    def speed_monitor_agent(self):
        return Agent(config=self.agents_config["speed_monitor_agent"])

    @task
    def driver_state_task(self):
        return Task(config=self.tasks_config["driver_state_task"])

    @task
    def child_occupancy_task(self):
        return Task(config=self.tasks_config["child_occupancy_task"])

    @task
    def phone_usage_task(self):
        return Task(config=self.tasks_config["phone_usage_task"])

    @task
    def seatbelt_usage_task(self):
        return Task(config=self.tasks_config["seatbelt_usage_task"])

    @task
    def alcohol_presence_task(self):
        return Task(config=self.tasks_config["alcohol_presence_task"])

    @task
    def speed_monitor_task(self):
        return Task(config=self.tasks_config["speed_monitor_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.driver_state_agent(),
                self.child_occupancy_agent(),
                self.phone_usage_agent(),
                self.seatbelt_usage_agent(),
                self.alcohol_presence_agent(),
                self.speed_monitor_agent()
            ],
            tasks=[
                self.driver_state_task(),
                self.child_occupancy_task(),
                self.phone_usage_task(),
                self.seatbelt_usage_task(),
                self.alcohol_presence_task(),
                self.speed_monitor_task()
            ],
            process=Process.sequential,
            verbose=True
        )
