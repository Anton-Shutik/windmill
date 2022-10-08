from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.flow_value_modules_item_value_type_2_iterator_type_1_type import (
    FlowValueModulesItemValueType2IteratorType1Type,
)

T = TypeVar("T", bound="FlowValueModulesItemValueType2IteratorType1")


@attr.s(auto_attribs=True)
class FlowValueModulesItemValueType2IteratorType1:
    """
    Attributes:
        expr (str):
        type (FlowValueModulesItemValueType2IteratorType1Type):
    """

    expr: str
    type: FlowValueModulesItemValueType2IteratorType1Type
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expr = self.expr
        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expr": expr,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expr = d.pop("expr")

        type = FlowValueModulesItemValueType2IteratorType1Type(d.pop("type"))

        flow_value_modules_item_value_type_2_iterator_type_1 = cls(
            expr=expr,
            type=type,
        )

        flow_value_modules_item_value_type_2_iterator_type_1.additional_properties = d
        return flow_value_modules_item_value_type_2_iterator_type_1

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