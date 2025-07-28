from langchain_core.tools import tool

class ReportingTools:
    @tool('Summarize Agent Outputs')
    def summarize_outputs(task_outputs: str) -> str:
        """Summarizes the outputs from all agents into a final report.
        The input to this tool should be a string containing all the outputs from previous agents.
        """
        print("--- Reporting Agent ---")
        print(f'Received outputs to summarize: {task_outputs}')
        
        # In a real-world scenario, this might involve more complex formatting,
        # saving to a file, or sending an email.
        summary = f"""\
        **E-Commerce Task Summary Report**

        **Generated Listing:**
        {task_outputs}

        **Final Pricing and Logistics:**
        - The product has been priced and logistics have been planned.

        **Conclusion:**
        The product is ready to be pushed to the marketplace.
        """
        print(f'Generated Summary Report:\n{summary}')
        return summary
