import datetime
import logging
import azure.functions as func

def main(triggerData) -> None:
    logging.info(f"Invoked by Dapr cron binding trigger: Hello, World! The time is {datetime.datetime.now()}")
