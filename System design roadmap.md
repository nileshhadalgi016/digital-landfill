# The Complete System Design Roadmap (For Beginners)

This is a zero-to-fundamentals path through System Design — no prior experience assumed. It's organized into 9 phases, each building on the last. Work through them in order; don't skip Foundations even if you're eager to get to the case studies, since everything after leans on it.

**Total estimated time:** ~10–14 weeks at a steady, part-time pace (5–8 hrs/week). Adjust freely — this is a floor, not a deadline.

**How to use this doc:** For each topic, you'll get why it matters, what to actually study under it, and where to learn it for free. Check things off as you go.

---

## 1. Foundations & Building Blocks
⏱ **~1–1.5 weeks**

Everything else in System Design assumes you're comfortable with these basics. Don't skip this even if some of it feels obvious.

**What is System Design**
- Why it matters: Sets the mental model for everything that follows — you're designing for scale, not just correctness.
- Covers: difference between System Design and coding/DSA, high-level vs low-level design
- Resources: *The System Design Primer* (GitHub — donnemartin/system-design-primer), ByteByteGo YouTube channel

**Client-Server Model**
- Why it matters: Almost every system you'll design is some flavor of client(s) talking to server(s).
- Covers: client vs server roles, request/response cycle, multiple clients per server
- Resources: MDN Web Docs — "How the Web works"

**IP Addresses, DNS & how a URL becomes a webpage**
- Why it matters: You can't reason about latency, routing, or CDNs without this.
- Covers: IP addressing basics, DNS resolution, what happens when you hit Enter on a URL
- Resources: "What happens when you type a URL into your browser" (search this exact phrase — it's a classic, widely-answered interview-prep question with great write-ups on GitHub)

**HTTP/HTTPS Basics**
- Why it matters: The protocol nearly all web systems communicate over.
- Covers: request/response structure, status codes, headers, HTTP vs HTTPS
- Resources: MDN Web Docs — HTTP overview

**APIs (REST basics)**
- Why it matters: APIs are how services expose functionality to each other and to clients.
- Covers: what an API is, REST principles, endpoints, verbs (GET/POST/PUT/DELETE)
- Resources: freeCodeCamp — REST API tutorials, Postman Learning Center

**What is a Server**
- Why it matters: Foundational vocabulary — you'll be placing "servers" in every diagram you draw.
- Covers: physical vs virtual servers, what a server actually does, web server vs application server

**Vertical vs Horizontal Scaling (intro concept)**
- Why it matters: The single most repeated trade-off in System Design — you'll revisit it in every phase.
- Covers: scaling up vs scaling out, basic trade-offs of each

---

## 2. Networking & Communication Patterns
⏱ **~1.5–2 weeks**

How different parts of a system actually talk to each other.

**TCP vs UDP (high level)**
- Why it matters: Determines reliability vs speed trade-offs for any communication channel you design.
- Covers: connection-oriented vs connectionless, when each is used (e.g., video streaming vs file transfer)
- Resources: Cloudflare Learning Center — "What is TCP/IP"

**Synchronous vs Asynchronous Communication**
- Why it matters: A core design decision — do services wait for a response, or fire-and-forget?
- Covers: blocking vs non-blocking calls, when async improves scalability

**REST APIs (deeper dive)**
- Why it matters: You'll be designing REST APIs constantly — understanding statelessness and resource modeling matters.
- Covers: statelessness, resource-based URLs, idempotency, versioning
- Resources: freeCodeCamp REST API course

**WebSockets (real-time communication)**
- Why it matters: The backbone of chat apps, live dashboards, multiplayer games — anything "real-time."
- Covers: persistent connections, use cases vs polling
- Resources: MDN Web Docs — WebSockets API

**Webhooks**
- Why it matters: A common pattern for event notification between systems (e.g., payment confirmations).
- Covers: how webhooks work, webhooks vs polling

**Message Queues (concept level — Kafka, RabbitMQ)**
- Why it matters: Decouples services and smooths out traffic spikes — a staple of scalable architecture.
- Covers: producer/consumer model, why queues exist, basic Kafka vs RabbitMQ distinction
- Resources: "Kafka in 100 seconds" style intro videos (ByteByteGo or similar channels), Confluent's free Kafka intro docs

**Publish/Subscribe Pattern**
- Why it matters: The pattern behind most event-driven systems and notification services.
- Covers: pub/sub vs point-to-point messaging, fan-out

**gRPC (intro)**
- Why it matters: Increasingly common for fast internal service-to-service communication.
- Covers: what gRPC is, how it differs from REST, when it's preferred
- Resources: grpc.io official "Introduction to gRPC"

---

## 3. Databases & Storage
⏱ **~2 weeks**

The data layer — arguably where most real design decisions get made.

**SQL vs NoSQL — when to use which**
- Why it matters: One of the most common early decisions (and interview questions) in System Design.
- Covers: structured vs unstructured data, use-case-driven decision making

**Relational Database Basics (tables, keys, joins)**
- Why it matters: You need this vocabulary even if you end up choosing NoSQL.
- Covers: primary/foreign keys, joins, schemas
- Resources: freeCodeCamp — SQL course, Khan Academy — Intro to SQL

**NoSQL Types (Key-Value, Document, Column, Graph)**
- Why it matters: "NoSQL" isn't one thing — each type solves a different problem.
- Covers: Redis (key-value), MongoDB (document), Cassandra (column), Neo4j (graph) — concept level only
- Resources: MongoDB's own "NoSQL Explained" docs

**Indexing**
- Why it matters: The difference between a query that takes 2ms and one that takes 2 seconds.
- Covers: what an index is, how it speeds up reads, trade-offs on writes

**Database Normalization (basic idea)**
- Why it matters: Helps you avoid data duplication and inconsistency in relational schemas.
- Covers: 1NF/2NF/3NF at a conceptual level (don't over-invest here — high-level understanding is enough)

**ACID Properties**
- Why it matters: The guarantees relational databases make — and what you give up if you don't have them.
- Covers: Atomicity, Consistency, Isolation, Durability

**Database Replication**
- Why it matters: How systems stay available and fast when read traffic scales.
- Covers: leader-follower replication, why replication improves availability

**Database Sharding/Partitioning**
- Why it matters: How you scale a database past what one machine can hold.
- Covers: horizontal partitioning, sharding keys, hotspot problems

**Read Replicas vs Write Masters**
- Why it matters: A common real-world scaling pattern you'll use in interviews and in practice.
- Covers: routing reads vs writes, replication lag implications

**CAP Theorem**
- Why it matters: The single most-cited theoretical framework in distributed System Design — you will be asked about this.
- Covers: Consistency, Availability, Partition tolerance, and why you can only fully guarantee two
- Resources: Martin Kleppmann's blog/talks on CAP theorem (search "Kleppmann CAP theorem")

---

## 4. Caching
⏱ **~1 week**

Speed, cheaply.

**Why Caching Exists**
- Why it matters: Reduces load on your database/backend and dramatically improves response times.
- Covers: the general "expensive computation, reused result" idea

**Client-Side vs Server-Side Caching**
- Why it matters: Different layers of your stack need different caching strategies.
- Covers: browser caching, server/app-level caching

**CDN (Content Delivery Network)**
- Why it matters: How large-scale systems serve static content fast, globally.
- Covers: edge servers, geographic distribution, static asset delivery
- Resources: Cloudflare Learning Center — "What is a CDN"

**Cache Eviction Policies (concept level)**
- Why it matters: Caches have limited space — you need a policy for what to remove.
- Covers: LRU (Least Recently Used), LFU (Least Frequently Used)

**Redis / Memcached (concept level)**
- Why it matters: The two most common in-memory caching tools you'll reference in interviews.
- Covers: what they are, in-memory key-value storage, common use cases
- Resources: redis.io — official "What is Redis" intro

**Write-Through vs Write-Back Caching**
- Why it matters: Determines consistency vs performance trade-offs when writing data.
- Covers: when each strategy is appropriate

---

## 5. Scalability Concepts
⏱ **~1.5–2 weeks**

How systems handle more traffic, more data, more users.

**Load Balancing (and algorithms)**
- Why it matters: Distributes traffic so no single server gets overwhelmed — a near-universal component.
- Covers: Round Robin, Least Connections, what a load balancer sits in front of
- Resources: NGINX docs — "What is Load Balancing"

**Horizontal Scaling in Practice**
- Why it matters: Moves from theory (Phase 1) to how it's actually implemented — stateless services, load balancers, etc.
- Covers: adding more machines, coordination challenges

**Stateless vs Stateful Services**
- Why it matters: Stateless services are dramatically easier to scale horizontally.
- Covers: session storage implications, why stateless is generally preferred at scale

**Auto-Scaling**
- Why it matters: How modern cloud systems adjust capacity to real-time demand automatically.
- Covers: scaling triggers (CPU, request count), scaling policies

**Database Scaling (recap in context)**
- Why it matters: Ties replication + sharding (Phase 3) into the broader scaling conversation.
- Covers: applying replication/sharding decisions to real traffic patterns

**Rate Limiting**
- Why it matters: Protects your system from abuse and overload — also a classic interview question ("design a rate limiter").
- Covers: token bucket, leaky bucket, fixed/sliding window algorithms (concept level)

**Back-of-the-Envelope Estimation**
- Why it matters: Interviewers expect you to sanity-check your design with rough numbers (storage, QPS, bandwidth).
- Covers: estimating traffic, storage, and bandwidth needs from user counts
- Resources: "System Design Primer" GitHub repo has a dedicated section on this

---

## 6. Reliability, Availability & Consistency
⏱ **~1.5 weeks**

Keeping systems up — and behaving predictably — when things go wrong.

**Availability vs Reliability (the difference)**
- Why it matters: These get conflated constantly, but they're different guarantees.
- Covers: uptime vs correctness, the "nines" of availability (99.9%, 99.99%, etc.)

**Redundancy & Failover**
- Why it matters: No single point of failure — the core principle behind highly available systems.
- Covers: backup systems, automatic failover, active-active vs active-passive

**Consistency Models**
- Why it matters: Determines what guarantees users get about seeing up-to-date data.
- Covers: Strong Consistency vs Eventual Consistency, real-world examples of each

**CAP Theorem (applied)**
- Why it matters: Now that you know the theory (Phase 3), apply it to real availability/consistency trade-off decisions.
- Covers: choosing CP vs AP systems for specific use cases

**Disaster Recovery Basics**
- Why it matters: Systems need a plan for catastrophic failure, not just routine faults.
- Covers: backups, recovery time objective (RTO), recovery point objective (RPO) — concept level

**Monitoring, Logging & Alerting (concept level)**
- Why it matters: You can't fix what you can't see — critical for operating systems at scale.
- Covers: what gets logged/monitored, why alerting thresholds matter

**Circuit Breaker Pattern**
- Why it matters: Prevents cascading failures when one service starts failing.
- Covers: how a circuit breaker "trips," fallback behavior

---

## 7. Architecture Patterns
⏱ **~1.5 weeks**

How you structure a system's services relative to each other.

**Monolithic Architecture**
- Why it matters: The default starting point for most systems — understanding it makes microservices trade-offs click.
- Covers: single deployable unit, pros/cons

**Microservices Architecture**
- Why it matters: The dominant pattern at scale, and a common interview topic.
- Covers: independently deployable services, service boundaries

**Monolith vs Microservices — trade-offs**
- Why it matters: Knowing *when* to choose each is more valuable than knowing either in isolation.
- Covers: team size, complexity, operational overhead considerations

**API Gateway**
- Why it matters: The single entry point that routes, authenticates, and manages traffic to microservices.
- Covers: routing, rate limiting, auth at the gateway layer

**Service Discovery**
- Why it matters: In a microservices world, services need a way to find each other dynamically.
- Covers: service registries, dynamic IP/port resolution

**Event-Driven Architecture**
- Why it matters: Ties directly back to message queues/pub-sub (Phase 2) — a common pattern for decoupled, scalable systems.
- Covers: producing/consuming events, eventual consistency implications

**CQRS (concept level, later-stage topic)**
- Why it matters: An advanced pattern worth knowing exists, even if you don't use it early on.
- Covers: separating read and write models — high level only, don't over-invest here yet

---

## 8. Security Basics for System Design
⏱ **~1 week**

The non-negotiables — not a full security course, just what System Design expects you to know.

**Authentication vs Authorization**
- Why it matters: Confused constantly, but distinct: who you are vs what you're allowed to do.
- Covers: login/identity vs permissions/access control

**OAuth (concept level)**
- Why it matters: The standard pattern behind "Sign in with Google" and third-party API access.
- Covers: what OAuth solves, tokens vs passwords, high-level flow
- Resources: oauth.net — "OAuth 2.0 Simplified" (free online, concept-level)

**Encryption at Rest & In Transit**
- Why it matters: Baseline expectation for any system handling user data.
- Covers: HTTPS/TLS for data in transit, encrypted storage for data at rest

**Rate Limiting & DDoS Protection (security context)**
- Why it matters: Revisits rate limiting (Phase 5) specifically as a security/abuse-prevention tool.
- Covers: how rate limiting doubles as basic DDoS mitigation

---

## 9. Practice: Case Studies & Interview Process
⏱ **~2–3 weeks**

Where everything comes together. This phase is about applying every prior phase to real, commonly-asked design problems.

**How to Approach a System Design Question (framework)**
- Why it matters: A repeatable framework beats improvising every time — interviewers reward structure.
- Covers: clarify requirements → estimate scale → high-level design → deep dive → identify bottlenecks
- Resources: "System Design Primer" GitHub repo — has a full framework section

**Design a URL Shortener**
- Why it matters: The "hello world" of System Design interviews — touches hashing, databases, and scaling.

**Design a Rate Limiter**
- Why it matters: Directly builds on Phase 5's rate-limiting concepts in a full design context.

**Design a Chat Application (like WhatsApp)**
- Why it matters: Tests WebSockets, message queues, and consistency concepts together.

**Design a News Feed (like Instagram/Twitter)**
- Why it matters: Classic fan-out problem — tests caching, databases, and read-heavy scaling.

**Design a Ride-Sharing App (like Uber)**
- Why it matters: Introduces geospatial/location-based design on top of everything else.

**Design a Video Streaming Service (like YouTube/Netflix)**
- Why it matters: Tests CDN, storage-at-scale, and encoding/delivery trade-offs.

**Common Mistakes Beginners Make in System Design Interviews**
- Why it matters: Avoids wasted effort — most beginners lose points on process, not knowledge.
- Covers: jumping to solutions before clarifying requirements, ignoring scale estimates, over-engineering for hypothetical scale

---

## Next Steps

Once you've worked through all 9 phases, the best reinforcement is repetition: re-attempt the case studies in Phase 9 from scratch, without notes, and time yourself. If a topic still feels shaky, that's your signal to loop back — this roadmap isn't meant to be read once, it's meant to be revisited.
