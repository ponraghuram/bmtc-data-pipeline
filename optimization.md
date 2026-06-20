# Performance & Cost Considerations

## Cluster Strategy
- Job clusters (not all-purpose) for each Workflow task — 
  spins up for the run, terminates after, no idle cost
- Autoscaling 1-4 workers — BMTC dataset is small, 
  but pattern scales to larger sources

## Partition Strategy
- Gold tables partitioned by `city` — query pattern is 
  always city-filtered for the dashboard
- AQE enabled — coalesces small shuffle partitions 
  automatically, avoiding the "200 partition on tiny data" problem

## Caching Decisions
- Silver DataFrame NOT cached — read once, written once, 
  reused nowhere else in this pipeline
- If Gold required 3+ aggregations from the same Silver 
  DataFrame, caching would be justified

## Cost Estimate (Illustrative)
At 6GB/day raw volume (Swiggy-scale estimate from Day 10):
- Job cluster: 2-4 workers, ~15 min runtime/day
- Estimated: <$5/day on standard instances
- At 10x scale (60GB/day): partition tuning + Photon 
  runtime would keep cost sub-linear