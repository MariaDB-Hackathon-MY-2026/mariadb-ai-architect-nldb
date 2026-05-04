"""Build ALTER TABLE statements to change FK actions (ON DELETE/ON UPDATE)."""

from __future__ import annotations

from dataclasses import dataclass

from core.introspect import ForeignKeyConstraintInfo


@dataclass(frozen=True)
class FkActionUpdate:
    constraint_name: str
    table_name: str
    column_name: str
    referenced_table_name: str
    referenced_column_name: str
    update_rule: str
    delete_rule: str


def build_fk_action_update_statements(*, fk: ForeignKeyConstraintInfo, update_rule: str, delete_rule: str) -> list[str]:
    # Drop + re-add with new rules
    constraint = fk.constraint_name
    table = fk.table_name
    col = fk.column_name
    ref_table = fk.referenced_table_name
    ref_col = fk.referenced_column_name

    update_rule = update_rule.upper().strip()
    delete_rule = delete_rule.upper().strip()

    add = (
        f"ALTER TABLE `{table}` "
        f"ADD CONSTRAINT `{constraint}` FOREIGN KEY (`{col}`) "
        f"REFERENCES `{ref_table}` (`{ref_col}`) "
        f"ON UPDATE {update_rule} ON DELETE {delete_rule}"
    )
    drop = f"ALTER TABLE `{table}` DROP FOREIGN KEY `{constraint}`"
    return [drop, add]

