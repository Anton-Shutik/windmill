from enum import Enum


class CompletedJobFlowStatusModulesItemType(str, Enum):
    WAITINGFORPRIORSTEPS = "WaitingForPriorSteps"
    WAITINGFOREVENT = "WaitingForEvent"
    WAITINGFOREXECUTOR = "WaitingForExecutor"
    INPROGRESS = "InProgress"
    SUCCESS = "Success"
    FAILURE = "Failure"

    def __str__(self) -> str:
        return str(self.value)