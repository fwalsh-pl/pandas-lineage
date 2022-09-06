"""
```
cd examples/mock-api-example/
python getting_started.py
```
"""

from uuid import uuid4

from pandas_lineage import read_csv
from pandas_lineage.types import JobRun
import os


job_run = JobRun(run_id=uuid4().hex, namespace='test', name='test')
start = job_run.emit_start()

df = read_csv('./mock_csv.csv', job_run=job_run)