from crewai import Task

class ProductTasks():
    def list_product_task(self, agent, product_topic, product_description):
        return Task(
            description=(
                f'Create a compelling product listing for: {product_topic}. '\
                f'Product description: {product_description}. '\
                'The listing should be engaging, informative, and optimized for search engines. Highlight key features and benefits. '\
                'Your final output should be a formatted product listing ready for publication.'
            ),
            expected_output='A well-structured and persuasive product listing, including a title, description, and key features.',
            agent=agent
        )

    def price_product_task(self, agent):
        return Task(
            description=(
                'Analyze the market and determine a competitive and profitable price point for the product. '\
                'Use the product listing created by the listing agent as context. '\
                'Consider factors like production cost, competitor pricing, and perceived value. '\
                'Your final answer must be the suggested retail price as a single numerical value.'
            ),
            expected_output='The suggested retail price for the product (e.g., 299.99).',
            agent=agent,
            context=[] # Context will be added in the crew setup
        )

    def plan_logistics_task(self, agent):
        return Task(
            description=(
                'Develop a comprehensive logistics and fulfillment plan for the new product. '\
                'Use the product listing and pricing as context. '\
                'Consider inventory management, warehousing, shipping partners, and delivery timelines. '\
                'Your final output should be a detailed logistics plan.'
            ),
            expected_output='A detailed logistics plan covering inventory, warehousing, and shipping.',
            agent=agent,
            context=[] # Context will be added in the crew setup
        )

    def reporting_task(self, agent):
        return Task(
            description=(
                'Summarize the outputs from the listing, pricing, and logistics tasks into a final report. '
                'Use the outputs from the `list_product_task`, `price_product_task`, and `plan_logistics_task` as the `listing_output`, `pricing_output`, and `logistics_output` arguments for the `summarize_outputs` tool.'
            ),
            expected_output='The final summary report, formatted as a single block of text, containing the complete product listing, the final price, and the detailed logistics plan. The report should start with "**E-Commerce Task Summary Report**".',
            agent=agent,
            context=[] # Context will be added in the crew setup
        )
