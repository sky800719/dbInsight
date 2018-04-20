from celery.utils.log import get_task_logger
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from celery.decorators import task
from .utils import DALUtil,DataGatherUtil,SYSConfig

logger = get_task_logger(__name__)

@task(name="task_a", default_retry_delay=5, max_retries=3, bind=True)
def task_a(self):
    try:
        print ("in task_a")
    except Exception as e:
        # 隔5S重试，最多3次
        logger.info(str(e))
        raise self.retry(exc=e)

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="task_b",
    ignore_result=True, bind=True)

def task_b(self):
    # 每1分钟执行一次
    print ("task b begin")
    DataGatherUtil.dataExtract(1, SYSConfig.DB_CATALOG_CONN, 100)
    print ("task b end")
