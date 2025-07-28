from langchain_core.tools import tool

class ListingTools:
    @tool('Format Product Listing')
    def format_listing(product_topic: str, product_description: str) -> str:
        """Formats a product listing for an e-commerce platform.
        The input to this tool should be the product topic and a detailed description.
        """
        # In a real-world scenario, this tool might use a template engine
        # or call a generative AI to create a compelling listing.
        # For this example, we'll use a simple formatting logic.
        print("--- Product Lister ---")
        print(f'Received product topic: {product_topic}')
        print(f'Received product description: {product_description}')

        listing = f"""\
        **Product Title:** SEO-Optimized: {product_topic}\n
        **Description:**\n
        {product_description} This revolutionary new product is designed for excellence and performance. It's not just a product; it's an experience that will change your life.\n
        **Key Features:**\n
        - Feature A: High-quality materials\n
        - Feature B: State-of-the-art technology\n
        - Feature C: User-friendly design\n
        **Category Tags:**\n
        #electronics #gadgets #{product_topic.replace(' ', '').lower()}
        """
        print(f'Formatted Listing:\n{listing}')
        return listing
