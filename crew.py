from crewai import Crew, Process
from tasks import ProductTasks
from agents import ProductAgents, llm

class ProductCrew:
    def __init__(self):
        self.agents = ProductAgents()
        self.tasks = ProductTasks()

    def crew(self):
        # Instantiate agents
        listing_agent = self.agents.listing_agent()
        pricing_agent = self.agents.pricing_agent()
        logistics_agent = self.agents.logistics_agent()
        reporting_agent = self.agents.reporting_agent()

        # Instantiate tasks
        list_product_task = self.tasks.list_product_task(listing_agent, '{product_topic}', '{product_description}')
        price_product_task = self.tasks.price_product_task(pricing_agent)
        plan_logistics_task = self.tasks.plan_logistics_task(logistics_agent)
        reporting_task = self.tasks.reporting_task(reporting_agent)

        # Set context for tasks
        price_product_task.context = [list_product_task]
        plan_logistics_task.context = [list_product_task, price_product_task]
        reporting_task.context = [list_product_task, price_product_task, plan_logistics_task]

        return Crew(
            agents=[
                listing_agent,
                pricing_agent,
                logistics_agent,
                reporting_agent
            ],
            tasks=[
                list_product_task,
                price_product_task,
                plan_logistics_task,
                reporting_task
            ],
            process=Process.sequential,
            memory=True,  # Enable memory for the crew
            verbose=True,
            manager_llm=llm,  # Set the manager LLM to the local model
            embedder={
                "provider": "ollama",
                "config": {
                    "model": "llama3"
                }
            }
        )
