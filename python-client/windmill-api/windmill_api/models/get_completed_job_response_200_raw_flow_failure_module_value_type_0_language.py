from enum import Enum


class GetCompletedJobResponse200RawFlowFailureModuleValueType0Language(str, Enum):
    DENO = "deno"
    PYTHON3 = "python3"
    GO = "go"

    def __str__(self) -> str:
        return str(self.value)