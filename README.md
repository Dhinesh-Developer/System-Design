# High-Level System Design (HLD) — Python

A practical learning repository for **High-Level System Design (HLD)** using Python.
This repository focuses on understanding how scalable, secure, observable, and reliable backend systems are designed and implemented.

## 🎯 Learning Goal

Learn HLD through the **20/80 approach** — focusing on the most important system design concepts that provide maximum practical value for an entry-level Software Engineer.

The goal is not only to understand theory, but also to **implement the concepts using Python and FastAPI**.

---

## 📚 Topics Covered

### 1. Scalability

* Vertical Scaling
* Horizontal Scaling
* Stateless vs Stateful Services
* Load Balancing
* Bottlenecks
* Capacity Estimation
* QPS / RPS
* Latency
* Throughput

### 2. API Design

* REST API
* HTTP Methods
* Request & Response
* HTTP Status Codes
* JSON
* Authentication
* Authorization
* Pagination
* API Versioning
* Idempotency

### 3. Caching

* Why Caching?
* Redis
* Cache Hit / Cache Miss
* Cache-Aside Pattern
* TTL
* LRU
* Cache Invalidation
* Hot Keys
* Cache Stampede

### 4. Observability

* Logging
* Metrics
* Tracing
* Monitoring
* Health Checks
* Liveness & Readiness
* Request / Correlation IDs
* Prometheus
* Grafana
* OpenTelemetry Basics
* p50 / p95 / p99 Latency

### 5. Security Basics

* Authentication
* Authorization
* JWT
* OAuth2 Basics
* HTTPS / TLS
* Password Hashing
* RBAC
* API Rate Limiting
* Environment Variables
* Secrets Management
* HTTP 401 / 403 / 429

---

## 🛠️ Technology Stack

* **Python**
* **FastAPI**
* **Redis**
* **PostgreSQL**
* **Prometheus**
* **Grafana**
* **OpenTelemetry**
* **JWT**
* **REST APIs**
* **Git & GitHub**

---

## 🏗️ Architecture Concepts

The basic architecture explored in this repository:

```text
                    ┌──────────────┐
                    │    Client    │
                    └──────┬───────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Load Balancer   │
                  └────────┬────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       ┌─────────────┐           ┌─────────────┐
       │  FastAPI 1  │           │  FastAPI 2  │
       └──────┬──────┘           └──────┬──────┘
              │                         │
              └────────────┬────────────┘
                           ▼
                    ┌─────────────┐
                    │    Redis    │
                    │    Cache    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ PostgreSQL  │
                    │  Database   │
                    └─────────────┘
```

---

# 🚀 Practical Projects

## 1. Secure Task Management System

A beginner-friendly backend system similar to a simple Jira/Trello application.

### Features

* User Registration
* User Login
* JWT Authentication
* Role-Based Access Control
* Task CRUD
* User/Admin Roles
* Password Hashing
* Redis Caching
* Rate Limiting
* Logging
* Request IDs
* Prometheus Metrics
* Health Checks

### Architecture

```text
Client
   │
   ▼
FastAPI
   │
   ├── Authentication
   ├── Authorization / RBAC
   ├── Rate Limiting
   ├── Logging
   │
   ▼
Task Service
   │
   ├── Redis
   │
   └── PostgreSQL
```

---

## 2. E-Commerce Order System

A beginner-to-intermediate system designed to understand how an e-commerce backend can scale.

### Features

* User Authentication
* Product Management
* Product Search
* Shopping Cart
* Order Creation
* Order Cancellation
* Inventory Management
* Admin APIs
* Redis Caching
* PostgreSQL
* Rate Limiting
* Metrics & Monitoring

### Architecture

```text
                    Client
                       │
                       ▼
                Load Balancer
                       │
              ┌────────┴────────┐
              ▼                 ▼
          FastAPI 1         FastAPI 2
              │                 │
              └────────┬────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
          Redis              PostgreSQL
          Cache               Database
```

### HLD Concepts Practiced

* Horizontal Scaling
* Stateless Services
* Load Balancing
* Caching
* Database Design
* API Design
* Rate Limiting
* Observability
* Failure Handling

---

## 3. URL Shortener

A simple but powerful system for learning real-world HLD concepts.

Example:

```text
https://example.com/very/long/url
                │
                ▼
           Shortener
                │
                ▼
        https://short.ly/aB72x
```

### Features

* Create Short URLs
* Redirect Short URLs
* Unique Short Code Generation
* Redis Caching
* PostgreSQL Storage
* Rate Limiting
* Metrics
* Logging
* Health Checks
* Error Handling

### Architecture

```text
Client
   │
   ▼
Load Balancer
   │
   ├──────────────┐
   ▼              ▼
API Server 1   API Server 2
   │              │
   └───────┬──────┘
           │
      ┌────┴─────┐
      ▼          ▼
    Redis    PostgreSQL
    Cache      Database
```

### Important HLD Scenario

URL shorteners are typically **read-heavy systems**.

Example:

```text
100 URL creations / second
        ↓
10,000 redirects / second
```

This makes caching extremely useful.

---

# 🧠 System Design Mental Model

For every system, I follow this design process:

```text
1. Requirements
       ↓
2. API Design
       ↓
3. Capacity Estimation
       ↓
4. Database Design
       ↓
5. Application Architecture
       ↓
6. Caching
       ↓
7. Scalability
       ↓
8. Security
       ↓
9. Observability
       ↓
10. Failure Handling
       ↓
11. Trade-offs
```

---

# 📊 20/80 HLD Cheat Sheet

The most important concepts I am focusing on:

| Area                | Key Concepts                         |
| ------------------- | ------------------------------------ |
| Scalability         | Horizontal Scaling, Vertical Scaling |
| Traffic             | RPS, QPS, Throughput                 |
| Performance         | Latency, p95, p99                    |
| Architecture        | Stateless Services                   |
| Networking          | Load Balancer                        |
| API                 | REST, HTTP Methods, Status Codes     |
| Database            | Indexing, Replication, SQL           |
| Caching             | Redis, Cache-Aside, TTL              |
| Security            | JWT, RBAC, HTTPS                     |
| Reliability         | Health Checks, Failure Handling      |
| Observability       | Logs, Metrics, Traces                |
| Monitoring          | Prometheus, Grafana                  |
| Distributed Systems | Rate Limiting, Idempotency           |

---

# 💻 Technologies

```text
Python
FastAPI
Redis
PostgreSQL
Prometheus
Grafana
OpenTelemetry
JWT
REST API
Git
GitHub
```

---

# 📁 Repository Structure

```text
HLD/
│
├── 01-scalability/
│   ├── vertical-scaling/
│   ├── horizontal-scaling/
│   ├── load-balancer/
│   └── capacity-estimation/
│
├── 02-api-design/
│   ├── rest-api/
│   ├── authentication/
│   ├── authorization/
│   ├── pagination/
│   └── idempotency/
│
├── 03-caching/
│   ├── redis/
│   ├── cache-aside/
│   ├── ttl/
│   └── cache-invalidation/
│
├── 04-observability/
│   ├── logging/
│   ├── metrics/
│   ├── health-checks/
│   ├── prometheus/
│   └── opentelemetry/
│
├── 05-security/
│   ├── jwt/
│   ├── rbac/
│   ├── password-hashing/
│   └── rate-limiting/
│
└── projects/
    ├── secure-task-management/
    ├── ecommerce-order-system/
    └── url-shortener/
```

---

# 🎓 Learning Approach

This repository follows a practical approach:

```text
Learn Concept
     ↓
Understand Why
     ↓
Write Python Code
     ↓
Build API
     ↓
Connect Database
     ↓
Add Redis
     ↓
Add Security
     ↓
Add Observability
     ↓
Think About Scaling
     ↓
Design the System
```

The focus is on **understanding the reason behind each component**, not just memorizing system design diagrams.

---

# 📈 Future Learning

After completing these fundamentals, the next areas will include:

* Message Queues
* Kafka
* Database Replication
* Database Sharding
* SQL vs NoSQL
* CAP Theorem
* Distributed Systems
* Event-Driven Architecture
* Microservices
* API Gateway
* CDN
* Object Storage
* Distributed Rate Limiting
* Advanced System Design

---

## ⭐ Goal

> **Learn HLD by building systems, not by memorizing diagrams.**

The ultimate goal is to develop the ability to take a real-world requirement and design a system that is:

**Scalable → Reliable → Secure → Observable → Maintainable**
