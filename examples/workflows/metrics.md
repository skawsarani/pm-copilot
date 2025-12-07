## Metrics Expert

Expert workflow for tracking, analyzing, and querying metrics. Can directly query metrics stored in `knowledge/product-analytics/metrics/` for answers.

---

### Define Success Metrics

```
Define success metrics for [feature/project]
```

**What it does**:
- Suggests relevant metrics (usage, engagement, business)
- Defines targets and timeframes
- Explains measurement methodology
- References existing metrics from `knowledge/product-analytics/metrics/`

**When to use**: Feature kick-off, goal setting

---

### Analyze Metrics

```
Analyze the metrics in @knowledge/product-analytics/metrics/[file] and tell me what's working
```

**What it does**:
- Identifies trends and anomalies
- Compares to targets
- Suggests hypotheses for changes
- Recommends next steps

**When to use**: Weekly/monthly reviews

---

### Query Metrics

```
What are the current [metric name] numbers?
```

**What it does**:
- Queries metrics files in `knowledge/product-analytics/metrics/`
- Finds relevant metric data
- Provides current values and trends
- Answers questions about metrics directly

**When to use**: Quick metric lookups, answering questions about product performance

**Detailed Steps**:

1. **Search Metrics Files**: Look in `knowledge/product-analytics/metrics/` for relevant data
2. **Extract Values**: Find current metric values
3. **Provide Context**: Show trends, comparisons, targets
4. **Answer Question**: Directly answer the metric question

---

### Create a Metrics Dashboard

```
Design a metrics dashboard for [project/feature]
```

**What it does**:
- Identifies key metrics to track
- Organizes into hierarchy (North Star → Leading → Lagging)
- Suggests visualization approaches

**When to use**: Project kick-off

---

### Compare Metrics

```
Compare [metric A] vs [metric B] from @knowledge/product-analytics/metrics/
```

**What it does**:
- Queries both metrics from knowledge base
- Compares values and trends
- Identifies relationships
- Provides insights

**When to use**: Understanding metric relationships

---

### Answer Metric Questions

```
[Question about product performance/metrics]
```

**What it does**:
- Queries relevant metrics from `knowledge/product-analytics/metrics/`
- Synthesizes data to answer the question
- Provides supporting evidence
- Suggests follow-up questions

**When to use**: Any question about product metrics or performance

**Examples**:
- "What's our current user retention rate?"
- "How are mobile metrics performing vs desktop?"
- "What metrics improved this quarter?"
- "Which features have the highest engagement?"
