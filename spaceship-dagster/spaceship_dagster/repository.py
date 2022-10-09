from dagster import load_assets_from_package_module, repository
from dagster import get_dagster_logger, job, op
from spaceship_dagster import assets
import pandas as pd 
import os



@op
def read_data(context):
    train_data = pd.read_csv('/Users/zafarmahmood/Documents/repos/kaggle/ML-pipelines/spaceship-titanic-data/train.csv')
    #files = [f for f in os.listdir(".") if os.path.isfile(f)]
    #print(train_data)
    #return {f: os.path.getsize(f) for f in files}
    context.log.info(train_data.head(5))
    return train_data


# @op
# def get_total_size(file_sizes):
#     return sum(file_sizes.values())


# @op
# def get_largest_size(file_sizes):
#     return max(file_sizes.values())


@op
def report_file_stats(total_size, largest_size):
    # In real life, we'd send an email or Slack message instead of just logging:
    get_dagster_logger().info(f"Total size: {total_size}, largest size: {largest_size}")


@job
def diamond():
    data = read_data()
    print(data)
    #file_sizes = get_file_sizes()
    #report_file_stats(
    #    total_size=get_total_size(file_sizes),
    #    largest_size=get_largest_size(file_sizes),
    #)


@repository
def spaceship_dagster():
    return [diamond]
