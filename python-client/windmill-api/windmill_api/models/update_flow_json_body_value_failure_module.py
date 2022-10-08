from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.update_flow_json_body_value_failure_module_input_transforms import (
    UpdateFlowJsonBodyValueFailureModuleInputTransforms,
)
from ..models.update_flow_json_body_value_failure_module_retry import UpdateFlowJsonBodyValueFailureModuleRetry
from ..models.update_flow_json_body_value_failure_module_sleep_type_0 import (
    UpdateFlowJsonBodyValueFailureModuleSleepType0,
)
from ..models.update_flow_json_body_value_failure_module_sleep_type_1 import (
    UpdateFlowJsonBodyValueFailureModuleSleepType1,
)
from ..models.update_flow_json_body_value_failure_module_stop_after_if import (
    UpdateFlowJsonBodyValueFailureModuleStopAfterIf,
)
from ..models.update_flow_json_body_value_failure_module_value_type_0 import (
    UpdateFlowJsonBodyValueFailureModuleValueType0,
)
from ..models.update_flow_json_body_value_failure_module_value_type_1 import (
    UpdateFlowJsonBodyValueFailureModuleValueType1,
)
from ..models.update_flow_json_body_value_failure_module_value_type_2 import (
    UpdateFlowJsonBodyValueFailureModuleValueType2,
)
from ..models.update_flow_json_body_value_failure_module_value_type_3 import (
    UpdateFlowJsonBodyValueFailureModuleValueType3,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFlowJsonBodyValueFailureModule")


@attr.s(auto_attribs=True)
class UpdateFlowJsonBodyValueFailureModule:
    """
    Attributes:
        input_transforms (UpdateFlowJsonBodyValueFailureModuleInputTransforms):
        value (Union[UpdateFlowJsonBodyValueFailureModuleValueType0, UpdateFlowJsonBodyValueFailureModuleValueType1,
            UpdateFlowJsonBodyValueFailureModuleValueType2, UpdateFlowJsonBodyValueFailureModuleValueType3]):
        stop_after_if (Union[Unset, UpdateFlowJsonBodyValueFailureModuleStopAfterIf]):
        sleep (Union[Unset, UpdateFlowJsonBodyValueFailureModuleSleepType0,
            UpdateFlowJsonBodyValueFailureModuleSleepType1]):
        summary (Union[Unset, str]):
        suspend (Union[Unset, int]):
        retry (Union[Unset, UpdateFlowJsonBodyValueFailureModuleRetry]):
    """

    input_transforms: UpdateFlowJsonBodyValueFailureModuleInputTransforms
    value: Union[
        UpdateFlowJsonBodyValueFailureModuleValueType0,
        UpdateFlowJsonBodyValueFailureModuleValueType1,
        UpdateFlowJsonBodyValueFailureModuleValueType2,
        UpdateFlowJsonBodyValueFailureModuleValueType3,
    ]
    stop_after_if: Union[Unset, UpdateFlowJsonBodyValueFailureModuleStopAfterIf] = UNSET
    sleep: Union[
        Unset, UpdateFlowJsonBodyValueFailureModuleSleepType0, UpdateFlowJsonBodyValueFailureModuleSleepType1
    ] = UNSET
    summary: Union[Unset, str] = UNSET
    suspend: Union[Unset, int] = UNSET
    retry: Union[Unset, UpdateFlowJsonBodyValueFailureModuleRetry] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_transforms = self.input_transforms.to_dict()

        if isinstance(self.value, UpdateFlowJsonBodyValueFailureModuleValueType0):
            value = self.value.to_dict()

        elif isinstance(self.value, UpdateFlowJsonBodyValueFailureModuleValueType1):
            value = self.value.to_dict()

        elif isinstance(self.value, UpdateFlowJsonBodyValueFailureModuleValueType2):
            value = self.value.to_dict()

        else:
            value = self.value.to_dict()

        stop_after_if: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stop_after_if, Unset):
            stop_after_if = self.stop_after_if.to_dict()

        sleep: Union[Dict[str, Any], Unset]
        if isinstance(self.sleep, Unset):
            sleep = UNSET

        elif isinstance(self.sleep, UpdateFlowJsonBodyValueFailureModuleSleepType0):
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        else:
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        summary = self.summary
        suspend = self.suspend
        retry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_transforms": input_transforms,
                "value": value,
            }
        )
        if stop_after_if is not UNSET:
            field_dict["stop_after_if"] = stop_after_if
        if sleep is not UNSET:
            field_dict["sleep"] = sleep
        if summary is not UNSET:
            field_dict["summary"] = summary
        if suspend is not UNSET:
            field_dict["suspend"] = suspend
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        input_transforms = UpdateFlowJsonBodyValueFailureModuleInputTransforms.from_dict(d.pop("input_transforms"))

        def _parse_value(
            data: object,
        ) -> Union[
            UpdateFlowJsonBodyValueFailureModuleValueType0,
            UpdateFlowJsonBodyValueFailureModuleValueType1,
            UpdateFlowJsonBodyValueFailureModuleValueType2,
            UpdateFlowJsonBodyValueFailureModuleValueType3,
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = UpdateFlowJsonBodyValueFailureModuleValueType0.from_dict(data)

                return value_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = UpdateFlowJsonBodyValueFailureModuleValueType1.from_dict(data)

                return value_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_2 = UpdateFlowJsonBodyValueFailureModuleValueType2.from_dict(data)

                return value_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            value_type_3 = UpdateFlowJsonBodyValueFailureModuleValueType3.from_dict(data)

            return value_type_3

        value = _parse_value(d.pop("value"))

        _stop_after_if = d.pop("stop_after_if", UNSET)
        stop_after_if: Union[Unset, UpdateFlowJsonBodyValueFailureModuleStopAfterIf]
        if isinstance(_stop_after_if, Unset):
            stop_after_if = UNSET
        else:
            stop_after_if = UpdateFlowJsonBodyValueFailureModuleStopAfterIf.from_dict(_stop_after_if)

        def _parse_sleep(
            data: object,
        ) -> Union[
            Unset, UpdateFlowJsonBodyValueFailureModuleSleepType0, UpdateFlowJsonBodyValueFailureModuleSleepType1
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _sleep_type_0 = data
                sleep_type_0: Union[Unset, UpdateFlowJsonBodyValueFailureModuleSleepType0]
                if isinstance(_sleep_type_0, Unset):
                    sleep_type_0 = UNSET
                else:
                    sleep_type_0 = UpdateFlowJsonBodyValueFailureModuleSleepType0.from_dict(_sleep_type_0)

                return sleep_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _sleep_type_1 = data
            sleep_type_1: Union[Unset, UpdateFlowJsonBodyValueFailureModuleSleepType1]
            if isinstance(_sleep_type_1, Unset):
                sleep_type_1 = UNSET
            else:
                sleep_type_1 = UpdateFlowJsonBodyValueFailureModuleSleepType1.from_dict(_sleep_type_1)

            return sleep_type_1

        sleep = _parse_sleep(d.pop("sleep", UNSET))

        summary = d.pop("summary", UNSET)

        suspend = d.pop("suspend", UNSET)

        _retry = d.pop("retry", UNSET)
        retry: Union[Unset, UpdateFlowJsonBodyValueFailureModuleRetry]
        if isinstance(_retry, Unset):
            retry = UNSET
        else:
            retry = UpdateFlowJsonBodyValueFailureModuleRetry.from_dict(_retry)

        update_flow_json_body_value_failure_module = cls(
            input_transforms=input_transforms,
            value=value,
            stop_after_if=stop_after_if,
            sleep=sleep,
            summary=summary,
            suspend=suspend,
            retry=retry,
        )

        update_flow_json_body_value_failure_module.additional_properties = d
        return update_flow_json_body_value_failure_module

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties