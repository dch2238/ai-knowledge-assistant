import asyncio
import time

# 1. Simulating an asynchronous call to an AI Model
async def query_ai_agent(agent_name: str, delay: int) -> str:
    """Simulates an AI Agent thinking and generating an answer."""
    print(f"[{agent_name}] Sent query to cloud... (will take {delay}s)")
    
    # asyncio.sleep simulates waiting for remote AI tokens without freezing the CPU!
    await asyncio.sleep(delay)
    
    print(f"[{agent_name}] >> Finished thinking!")
    return f"Response from {agent_name}"


# 2. The Main Orchestrator running multiple agents concurrently
async def main():
    start_time = time.time()
    print("--- STARTING CONCURRENT AI AGENT CALLS ---")

    # asyncio.gather fires both agents AT THE SAME TIME!
    # Agent 1 takes 2 seconds, Agent 2 takes 2 seconds.
    results = await asyncio.gather(
        query_ai_agent("Researcher Agent", delay=2),
        query_ai_agent("Critic Agent", delay=2),
        query_ai_agent("Fact-Checker Agent", delay=3)
    )

    total_time = time.time() - start_time
    print("\n--- RESULTS RECEIVED ---")
    for res in results:
        print(f"- {res}")
    
    print(f"\nTotal Elapsed Time: {total_time:.2f} seconds")
    print("(Notice: 2s + 2s took only ~2 seconds total instead of 4 seconds!)")


# 3. Starting the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())