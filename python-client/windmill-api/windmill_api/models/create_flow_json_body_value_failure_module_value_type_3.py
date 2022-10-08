from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_flow_json_body_value_failure_module_value_type_3_type import (
    CreateFlowJsonBodyValueFailureModuleValueType3Type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFlowJsonBodyValueFailureModuleValueType3")


@attr.s(auto_attribs=True)
class CreateFlowJsonBodyValueFailureModuleValueType3:
    """
    Attributes:
        type (CreateFlowJsonBodyValueFailureModuleValueType3Type):
        path (Union[Unset, str]):
    """

    type: CreateFlowJsonBodyValueFailureModuleValueType3Type
    path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CreateFlowJsonBodyValueFailureModuleValueType3Type(d.pop("type"))

        path = d.pop("path", UNSET)

        create_flow_json_body_value_failure_module_value_type_3 = cls(
            type=type,
            path=path,
        )

        create_flow_json_body_value_failure_module_value_type_3.additional_properties = d
        return create_flow_json_body_value_failure_module_value_type_3

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