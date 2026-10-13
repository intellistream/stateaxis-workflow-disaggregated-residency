# Current real-online blocker

Both visible Ascend 910B2 devices were idle on 2026-10-13; the captured
`NPU_SNAPSHOT.txt` reports no processes on NPU 4 or 5. No device run was
started because hardware availability is not the blocking condition.

At StateAxis commit `16f6c917...`, the hash-bound v0.2 parser accepts only a
contract where remote prefetch, peer transfer, persistent remote ownership and
remote allocation are false. The policy implementation records a remote
candidate and immediately recovers to the already verified local state. It
does not move or allocate state.

The targeted Rust command in `RESULT.json` passed both relevant tests. Those
tests validate activation, exactness, counters and local recovery; they do not
create a data plane. Consequently, an accelerator ON/OFF run would measure
only host accounting overhead and would not be evidence for the named
mechanism.

`RESULT.json` records the exact repository commits, source and manifest hashes,
hardware snapshot, blocker classification and the implementation/fault/test
gates required before a 3+3 real-online campaign becomes meaningful.
