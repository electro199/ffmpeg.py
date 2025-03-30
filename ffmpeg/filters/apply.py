from .base import BaseFilter
from ..inputs import BaseInput, StreamSpecifier


def apply(
    node: BaseFilter,
    *parent: BaseInput | StreamSpecifier,
) -> StreamSpecifier:
    node.parent_nodes.extend(parent)
    return node.get_outputs()  # type: ignore


def apply2(
    node: BaseFilter,
    *parent: BaseInput | StreamSpecifier,
) -> list[StreamSpecifier]:
    node.parent_nodes.extend(parent)
    return node.get_outputs()  # type: ignore
