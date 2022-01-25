# Source Code
*   [`main.py`](main.py)
    *   The **final state** of the project with our Discord command bot
*   [`main_client_initial.py`](main_client_initial.py)
    *   The Discord client before adding the `dotenv` stuff (and the key)
        *   This implements everything up to [lecture notes section Client Object](../#client-object)
*   [`main_client_dotenv.py`](main_client_dotenv.py)
    *   The Discord client after adding using `dotenv` to source our API Token from the `.env` file
        *   This implements everything up to [lecture notes section Loading `.env` files with `python-dotenv`](../#loading-env-files-with-python-dotenv)
*   [`main_client_events.py`](main_client_events.py)
    *   The Discord client after adding the `on_ready` and `on_message` events
    *   This implements everything up to [lecture notes section `on_message` Event](../#on_message-event)
*   [`main_bot_msg_listen.py`](main_client_msg_listen.py)
    *   The Discord `commands.Bot` class from `main.py` 
    *   This illustrates the listener that can be attached to the `on_message` listener illustrated in the [lecture notes section `on_message` Event With `command.Bot` Class](../#on_message-event-with-commandbot-class)