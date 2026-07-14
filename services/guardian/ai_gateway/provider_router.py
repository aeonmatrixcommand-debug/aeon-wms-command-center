def get_provider(policy, registry=None):

    # Backward compatibility Sprint 62
    if registry is None:
        return {
            "name": policy,
            "status": "available"
        }

    # Sprint 63 Governance Routing
    if policy.risk_score > 80:
        return registry.get("secure")

    for name, data in registry.providers.items():
        metadata = data["metadata"]

        if metadata.get("latency", 999) < 100:
            return data

    return registry.get("default")
