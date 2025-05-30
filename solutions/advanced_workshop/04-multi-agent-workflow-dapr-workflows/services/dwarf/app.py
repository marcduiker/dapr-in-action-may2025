from dapr_agents import AssistantAgent
from dapr_agents.llm import HFHubChatClient
from dotenv import load_dotenv
import asyncio
import logging

async def main():
    try:
        # Define Agent
        llm_client = HFHubChatClient(
            model="microsoft/Phi-3-mini-4k-instruct"
        )
        dwarf_service = AssistantAgent(
            name="Gimli",
            role="Dwarf",
            goal="Fight fiercely in battle, protect allies, and expertly navigate underground realms and stonework.",
            instructions=[
                "Speak like Gimli, with boldness and a warrior's pride.",
                "Be strong-willed, fiercely loyal, and protective of companions.",
                "Excel in close combat and battlefield tactics, favoring axes and brute strength.",
                "Navigate caves, tunnels, and ancient stonework with expert knowledge.",
                "Respond concisely, accurately, and relevantly, ensuring clarity and strict alignment with the task."
            ],
            message_bus_name="messagepubsub",
            state_store_name="workflowstatestore",
            state_key="workflow_state",
            agents_registry_store_name="agentstatestore",
            agents_registry_key="agents_registry",
            llm=llm_client
        )

        await dwarf_service.start()
    except Exception as e:
        print(f"Error starting service: {e}")

if __name__ == "__main__":
    load_dotenv()

    logging.basicConfig(level=logging.INFO)
    
    asyncio.run(main())