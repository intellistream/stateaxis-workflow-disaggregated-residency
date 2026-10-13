# stateaxis-workflow-disaggregated-residency

Extension ID: `org.vllm-hust.stateaxis-workflow-disaggregated-residency`

This active experimental MOD is the independently reviewable request-level
residency decision and recovery contract for StateAxis issue
[#20](https://github.com/Qixin-Gaoke/stateaxis/issues/20). Shuhao Zhang (Tony)
is directly responsible; no advisor is declared.

The v0.2 mechanism applies only to stateful requests. It binds the decision to
the workflow namespace, state ID and generation, evaluates the reviewed remote
candidate at a request boundary, and atomically recovers to the already
verified local state. The contract deliberately disables peer transfer,
remote prefetch, remote allocation, persistent remote ownership and state
lifetime extension. This is the safe minimum policy hook requested by issue
#20, not a completed cross-instance data plane.

## Activation

Activation is default-off and must go through vLLM-HUST Extension Manager/ECPA:

```bash
python -m pip install .
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension check \
  org.vllm-hust.stateaxis-workflow-disaggregated-residency
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension plan \
  org.vllm-hust.stateaxis-workflow-disaggregated-residency
```

StateAxis accepts only version `0.2.0` and the exact research-manifest SHA-256.
It binds the MOD identity into assembly/state graph and exposes lifetime counts
for decisions, stateful candidates, remote candidates, local recoveries and
fail-closed outcomes.

Rollback is to disable or forget the extension. The local StateAxis state path
then remains authoritative with no MOD identity or effect counts.

## Evidence boundary

Matched runtime OFF/ON preserves exact output and clean shutdown. ON evaluates
one generation-bound remote candidate and executes one atomic local recovery;
it performs zero remote allocations. Extension Manager check, plan, dry-run and
a real managed assembly-check process also pass.

No repeated real-online NPU test is reported because the reviewed candidate has
no remote transport to exercise. A device run would measure only host policy
overhead and could not qualify disaggregated residency. No speedup,
cross-instance transfer, migration or remote ownership claim is made. See
[EVIDENCE.md](EVIDENCE.md).
The commit-bound blocker, idle-device snapshot and exact recovery gates are in
`evidence/current-online-blocker-20261013/`.

## Validate

```bash
python -m pip install -e '.[test]'
ruff check .
ruff format --check .
pytest -q
python -m build
```
