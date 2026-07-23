
import File1
import time
from importlib import reload
File1.add()
time.sleep(30)
reload(File1)
print("End of file2")
