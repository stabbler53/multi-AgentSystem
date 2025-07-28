from crewai import Agent
from langchain_community.llms import Ollama
from tools.pricing_tools import PricingTools
from tools.listing_tools import ListingTools
from tools.logistics_tools import LogisticsTools
from tools.reporting_tools import ReportingTools

# Initialize the Ollama model globally
llm = Ollama(model='llama3')

class ProductAgents():
    def pricing_agent(self):
        return Agent(
            role='Lead Pricing Analyst',
            goal='Determine the optimal market price for new products',
            backstory=(
                'With a keen eye for market dynamics and a deep understanding of consumer behavior, you are the go-to expert for setting competitive and profitable prices. Your analysis ensures that products are not just well-received but also financially successful.'
            ),
            tools=[PricingTools.calculate_price],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def listing_agent(self):
        return Agent(
            role='Senior Product Lister',
            goal='Create compelling and optimized product listings for online marketplaces',
            backstory=(
                'You are a master of words and a digital marketing guru. Your listings not only describe products but tell a story that captivates and converts customers. You know how to tailor content for different platforms and audiences to maximize visibility and sales.'
            ),
            tools=[ListingTools.format_listing],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def logistics_agent(self):
        return Agent(
            role='Logistics and Fulfillment Coordinator',
            goal='Manage all aspects of product logistics, from inventory to shipping',
            backstory=(
                'You are the operational backbone of the product launch. Your meticulous planning ensures that products are available, orders are fulfilled accurately, and deliveries are on time. You navigate the complexities of supply chain management with ease.'
            ),
            tools=[LogisticsTools.check_inventory, LogisticsTools.calculate_shipping],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def reporting_agent(self):
        return Agent(
            role='Reporting Analyst',
            goal='Generate comprehensive reports from agent outputs',
            backstory=(
                'You are a meticulous analyst who specializes in summarizing complex information into clear and actionable reports. You synthesize data from various teams to provide a holistic view of the operation.'
            ),
            tools=[ReportingTools.summarize_outputs],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
