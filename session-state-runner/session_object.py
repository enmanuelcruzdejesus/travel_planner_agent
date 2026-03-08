import uuid
from google.adk.sessions import InMemorySessionService
import asyncio

async def main():
    temp_service = InMemorySessionService()
    example_session = await temp_service.create_session(
        app_name = "my_app",
        user_id=f"user {uuid.uuid4()}",
        state={"initial_key":"Hello world for State!"}
    )
    # Run the async function

    print(f"--- Examing Session Properties ---")
    print(f"ID (`id`): {example_session.id}")
    print(f"App Name (`app_name`): {example_session.app_name}")
    print(f"User ID (`user_id`): {example_session.user_id}")
    print(f"State (`state`): {example_session.state}")
    print(f"Events (`events`): {example_session.events}")

    print("Last update time (`last_update_time`):", example_session.last_update_time)

    temp_service = await temp_service.delete_session(
        app_name = "my_app",
        user_id = example_session.user_id,
        session_id = example_session.id
    )

    print("The final status of temp_service -  ", temp_service)


if __name__ == "__main__":
    asyncio.run(main())