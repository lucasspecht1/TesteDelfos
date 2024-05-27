from dagster import asset, op, job

@op
def hello_world():
    return "Hello, Dagster!"

@job
def hello_world_pipeline(): 
    hello_world()
