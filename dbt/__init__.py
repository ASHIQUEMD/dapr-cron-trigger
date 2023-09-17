import datetime
import logging
import azure.functions as func

def main(triggerData) -> None:
    """
    Sample Dapr Binding Trigger
    See https://aka.ms/azure-functions-dapr for more information about using this binding
    
    These tasks should be completed prior to running :
         1. Install Dapr
         2. func extensions install -p Microsoft.Azure.WebJobs.Extensions.Dapr -v 0.15.0-preview01
    Run the app with below steps
         1. Start function app with Dapr: dapr run --app-id functionapp --app-port 3001 --dapr-http-port 3501 --resources-path .\components\ -- func host start
    """
    logging.info(f"Invoked by Dapr cron binding trigger: Hello, World! The time is {datetime.datetime.now()}")
