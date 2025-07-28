from langchain_core.tools import tool

class ReportingTools:
    @tool('Summarize Agent Outputs')
    def summarize_outputs(listing_output: str, pricing_output: str, logistics_output: str) -> str:
        """Summarizes the outputs from the listing, pricing, and logistics agents into a final report.
        The input to this tool should be the string outputs from the respective tasks.
        """
        print("--- Reporting Agent ---")
        print(f'Received Listing Output: {listing_output}')
        print(f'Received Pricing Output: {pricing_output}')
        print(f'Received Logistics Output: {logistics_output}')

        # In a real-world scenario, this might involve more complex formatting,
        # saving to a file, or sending an email.
        summary = f"""\
        **E-Commerce Task Summary Report**

        **1. Product Listing:**
        {listing_output}

        **2. Pricing Strategy:**
        - {pricing_output}

        **3. Logistics Plan:**
        - {logistics_output}

        **Conclusion:**
        All tasks are complete. The product is ready for market launch.
        """
        print(f'Generated Summary Report:\n{summary}')
        return summary
