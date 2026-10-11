"""Workflow-disaggregated residency activation contract."""

from __future__ import annotations

from dataclasses import asdict, dataclass

MOD_ID = "org.vllm-hust.stateaxis-workflow-disaggregated-residency"


@dataclass(frozen=True, slots=True)
class WorkflowDisaggregatedResidencyConfig:
    """Exact request-level remote-candidate/local-recovery contract."""

    enabled: bool = True
    authority: bool = True
    scope: str = "stateful-workflow-namespace"
    policy: str = "remote-candidate-local-recovery"
    local_instance_id: str = "local-0"
    peer_instance_ids: tuple[str, ...] = ("peer-0",)
    generation_bound: bool = True
    request_bound_safe_points: bool = True
    remote_prefetch: bool = False
    peer_transfer_enabled: bool = False
    fallback_to_local_recompute: bool = True
    atomic_recovery: bool = True
    stable_workflow_identity: bool = True
    persistent_remote_ownership: bool = False
    remote_state_allocations: bool = False
    no_state_lifetime_extension: bool = True
    fail_closed: bool = True

    def __post_init__(self) -> None:
        expected = {
            "enabled": True,
            "authority": True,
            "scope": "stateful-workflow-namespace",
            "policy": "remote-candidate-local-recovery",
            "local_instance_id": "local-0",
            "peer_instance_ids": ("peer-0",),
            "generation_bound": True,
            "request_bound_safe_points": True,
            "remote_prefetch": False,
            "peer_transfer_enabled": False,
            "fallback_to_local_recompute": True,
            "atomic_recovery": True,
            "stable_workflow_identity": True,
            "persistent_remote_ownership": False,
            "remote_state_allocations": False,
            "no_state_lifetime_extension": True,
            "fail_closed": True,
        }
        if asdict(self) != expected:
            raise ValueError(
                "workflow-disaggregated residency requires the reviewed contract"
            )


def workflow_disaggregated_residency() -> WorkflowDisaggregatedResidencyConfig:
    return WorkflowDisaggregatedResidencyConfig()


__all__ = [
    "MOD_ID",
    "WorkflowDisaggregatedResidencyConfig",
    "workflow_disaggregated_residency",
]
