import os
from datetime import date
from datetime import datetime

now = datetime.now()


# type = info, warn, error
def logging(ctx, type="info"):
    logFileLocation = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                   "../Logs", "{}.log".format(date.today()))
    logFile = open(logFileLocation, mode='a', encoding="utf-8")
    type = "[{}]".format(type.upper())
    logFile.write("{} {} : {}\n".format(type, now.strftime("%H:%M:%S"), ctx))


if __name__ == "__main__":
    logging("This is test log")