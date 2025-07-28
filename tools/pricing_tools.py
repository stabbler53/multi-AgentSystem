from langchain_core.tools import tool

class PricingTools:
    @tool('Calculate Product Price')
    def calculate_price(product_topic: str, product_description: str) -> str:
        """Calculates the optimal price for a product based on market analysis.
        The input to this tool should be the product topic and a detailed description.
        """
        print("--- Pricing Analyst ---")
        print(f'Received product topic: {product_topic}')
        print(f'Received product description: {product_description}')


        price = 100 + (len(product_description) * 0.5)  # Base price + 50 cents per character
        print(f'Calculated Price: {price:.2f}')
        return f'The optimal price is ${price:.2f}'
