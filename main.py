import asyncio
from agents import Agent, Runner, ModelSettings
from track.tracker import KevTracker
from tools.functions import gather_context, send_email_report
from agents.extensions.visualization import draw_graph
from utils.env_utils import get_last_count, load_prompts, update_last_count


async def main():
    '''
    Main entrypoint for Kev-Reporter. Checks for new CISA KEVs, gathers context via the Context Controller Agent, 
    and generates reports via the Reporter Agent.
    '''
    print("Starting Kev-Reporter agent workflow...\n")
    
    current_kev_count = get_last_count()
    print(f"[INFO] Loaded last KEV count from .env -> {current_kev_count}\n")
    
    kev_tracker = KevTracker(start_count=current_kev_count)
    new_kevs = kev_tracker.new_items()

    if not new_kevs:
        print("[INFO] No new KEVs found.")
        return
    
    print(f"[INFO] Found {len(new_kevs)} new KEVs since last count.\n")
    
    context_controller_agent_system_prompt, reporter_agent_system_prompt = load_prompts()

    reporter_agent = Agent(name="Reporter Agent" , instructions=reporter_agent_system_prompt, tools=[send_email_report], model_settings=ModelSettings(tool_choice="send_email_report"), tool_use_behavior="stop_on_first_tool", model="gpt-5-mini")
    context_controller_agent = Agent(name="Context Controller Agent", instructions=context_controller_agent_system_prompt, tools=[gather_context], handoffs=[reporter_agent], model_settings=ModelSettings(tool_choice="gather_context"))
    #draw_graph(agent=context_controller_agent, filename="./docs/agent-diagram")
    print("[INFO] Agents initialized successfully. Beginning processing...\n")

    for kev in new_kevs:
        result = await Runner.run(context_controller_agent, str(kev))
        print("\n[REPORT OUTPUT]\n")
        print(result.final_output)
        print("-" * 80 + "\n")
    
    new_count = current_kev_count + len(new_kevs)
    update_last_count(new_count)
    print(f"[INFO] Updated LAST_KEV_COUNT in .env -> {new_count}\n")

if __name__ == "__main__":
    asyncio.run(main())

