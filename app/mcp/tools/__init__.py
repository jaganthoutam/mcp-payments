"""MCP tool registry with comprehensive analytics and monitoring capabilities."""

from .payments import (
    create_payment,
    verify_payment,
    refund_payment,
    get_payment_status,
)
from .wallets import (
    get_wallet_balance,
    transfer_funds,
    wallet_transaction_history,
    top_up_wallet,
)
from .analytics import (
    get_payment_metrics,
    analyze_user_behavior,
    generate_revenue_analytics,
    detect_fraud_patterns,
    generate_performance_report,
    get_dashboard_metrics,
    generate_custom_report,
    optimize_payment_routing,
    create_payment_optimized,
    smart_payment_routing,
)
# Temporarily commented out to isolate metadata issue
from .monitoring import (
    perform_health_check,
    create_alert,
    resolve_alert,
    record_performance_metric,
    log_error,
    get_system_status,
    get_active_alerts,
    get_performance_metrics,
)
from .compliance import (
    generate_audit_report,
    export_compliance_data,
    validate_pci_compliance,
    get_audit_trail,
)
from .subscriptions import (
    create_subscription,
    get_subscription,
    update_subscription,
    cancel_subscription,
    get_subscription_metrics,
    create_subscription_optimized,
    analyze_subscription_health,
)

# Comprehensive tool registry for production-grade payment system
TOOL_REGISTRY = {
    # Core Payment Tools
    "create_payment": create_payment,
    "verify_payment": verify_payment,
    "refund_payment": refund_payment,
    "get_payment_status": get_payment_status,
    
    # Wallet Management Tools
    "get_wallet_balance": get_wallet_balance,
    "transfer_funds": transfer_funds,
    "wallet_transaction_history": wallet_transaction_history,
    "top_up_wallet": top_up_wallet,
    
    # Subscription Management Tools
    "create_subscription": create_subscription,
    "get_subscription": get_subscription,
    "update_subscription": update_subscription,
    "cancel_subscription": cancel_subscription,
    "get_subscription_metrics": get_subscription_metrics,
    "create_subscription_optimized": create_subscription_optimized,
    "analyze_subscription_health": analyze_subscription_health,
    
    # Analytics Tools
    "get_payment_metrics": get_payment_metrics,
    "analyze_user_behavior": analyze_user_behavior,
    "generate_revenue_analytics": generate_revenue_analytics,
    "detect_fraud_patterns": detect_fraud_patterns,
    "generate_performance_report": generate_performance_report,
    "get_dashboard_metrics": get_dashboard_metrics,
    "generate_custom_report": generate_custom_report,
    
    # AI Optimization Tools
    "optimize_payment_routing": optimize_payment_routing,
    "create_payment_optimized": create_payment_optimized,
    "smart_payment_routing": smart_payment_routing,
    
    # Monitoring Tools
    "perform_health_check": perform_health_check,
    "create_alert": create_alert,
    "resolve_alert": resolve_alert,
    "record_performance_metric": record_performance_metric,
    "log_error": log_error,
    "get_system_status": get_system_status,
    "get_active_alerts": get_active_alerts,
    "get_performance_metrics": get_performance_metrics,
    
    # Compliance & Audit Tools
    "generate_audit_report": generate_audit_report,
    "export_compliance_data": export_compliance_data,
    "validate_pci_compliance": validate_pci_compliance,
    "get_audit_trail": get_audit_trail,
}

# Tool categories for better organization
TOOL_CATEGORIES = {
    "payments": [
        "create_payment",
        "verify_payment", 
        "refund_payment",
        "get_payment_status",
    ],
    "wallets": [
        "get_wallet_balance",
        "transfer_funds",
        "wallet_transaction_history",
        "top_up_wallet",
    ],
    "subscriptions": [
        "create_subscription",
        "get_subscription",
        "update_subscription", 
        "cancel_subscription",
        "get_subscription_metrics",
        "create_subscription_optimized",
        "analyze_subscription_health",
    ],
    "analytics": [
        "get_payment_metrics",
        "analyze_user_behavior",
        "generate_revenue_analytics",
        "detect_fraud_patterns",
        "generate_performance_report",
        "get_dashboard_metrics",
        "generate_custom_report",
    ],
    "ai_optimization": [
        "optimize_payment_routing",
        "create_payment_optimized", 
        "smart_payment_routing",
        "create_subscription_optimized",
        "analyze_subscription_health",
    ],
    "monitoring": [
        "perform_health_check",
        "create_alert",
        "resolve_alert",
        "record_performance_metric",
        "log_error",
        "get_system_status",
        "get_active_alerts",
        "get_performance_metrics",
    ],
    "compliance": [
        "generate_audit_report",
        "export_compliance_data",
        "validate_pci_compliance",
        "get_audit_trail",
    ],
}

# Tool descriptions for documentation
TOOL_DESCRIPTIONS = {
    # Payment Tools
    "create_payment": "Initialize a new payment transaction with provider integration",
    "verify_payment": "Verify payment status and update transaction state",
    "refund_payment": "Process payment refund with audit trail",
    "get_payment_status": "Retrieve current payment status and details",
    
    # Wallet Tools
    "get_wallet_balance": "Retrieve current wallet balance for user",
    "transfer_funds": "Execute P2P or merchant transfer",
    "wallet_transaction_history": "Get wallet transaction history",
    "top_up_wallet": "Add funds to user wallet",
    
    # Subscription Tools
    "create_subscription": "Create new subscription plan",
    "get_subscription": "Retrieve subscription details",
    "update_subscription": "Update subscription parameters",
    "cancel_subscription": "Cancel active subscription",
    "get_subscription_metrics": "Get subscription analytics",
    "create_subscription_optimized": "Create AI-optimized subscription with intelligent pricing and routing",
    "analyze_subscription_health": "AI-powered subscription health analysis and churn prediction",
    
    # Analytics Tools
    "get_payment_metrics": "Generate comprehensive payment metrics and KPIs",
    "analyze_user_behavior": "Analyze user behavior patterns and engagement",
    "generate_revenue_analytics": "Generate revenue analytics and forecasting",
    "detect_fraud_patterns": "Detect fraud patterns and analyze transaction risk",
    "generate_performance_report": "Generate system performance analytics",
    "get_dashboard_metrics": "Get real-time dashboard metrics and KPIs",
    "generate_custom_report": "Generate custom analytics reports",
    
    # AI Optimization Tools
    "optimize_payment_routing": "AI-powered payment routing optimization for cost, speed, or success rate",
    "create_payment_optimized": "Create AI-optimized payment with intelligent routing and fraud detection",
    "smart_payment_routing": "Intelligent payment routing based on customer profile and transaction context",
    
    # Monitoring Tools
    "perform_health_check": "Perform comprehensive system health check",
    "create_alert": "Create system alert for monitoring",
    "resolve_alert": "Resolve existing system alert",
    "record_performance_metric": "Record performance metric for monitoring",
    "log_error": "Log error with comprehensive context",
    "get_system_status": "Get comprehensive system status overview",
    "get_active_alerts": "Get list of active system alerts",
    "get_performance_metrics": "Get performance metrics for analysis",
    
    # Compliance Tools
    "generate_audit_report": "Generate compliance audit report",
    "export_compliance_data": "Export data for compliance requirements",
    "validate_pci_compliance": "Validate PCI-DSS compliance status",
    "get_audit_trail": "Retrieve audit trail for transactions",
}

# Tool permissions for access control
TOOL_PERMISSIONS = {
    # Public tools (minimal authentication)
    "public": [
        "get_payment_status",
        "get_wallet_balance",
        "perform_health_check",
        "get_system_status",
    ],
    
    # Standard user tools
    "user": [
        "create_payment",
        "verify_payment",
        "transfer_funds",
        "wallet_transaction_history",
        "top_up_wallet",
        "create_subscription",
        "get_subscription",
        "update_subscription",
        "cancel_subscription",
    ],
    
    # Analytics user tools
    "analyst": [
        "get_payment_metrics",
        "analyze_user_behavior",
        "generate_revenue_analytics",
        "get_dashboard_metrics",
        "generate_custom_report",
        "get_performance_metrics",
        "smart_payment_routing",
        "get_subscription_metrics",
        "analyze_subscription_health",
    ],
    
    # AI optimization tools
    "ai_operator": [
        "optimize_payment_routing",
        "create_payment_optimized",
        "smart_payment_routing",
        "detect_fraud_patterns",
        "create_subscription_optimized",
        "analyze_subscription_health",
    ],
    
    # Operations team tools
    "operator": [
        "create_alert",
        "resolve_alert",
        "record_performance_metric",
        "log_error",
        "get_active_alerts",
        "detect_fraud_patterns",
        "generate_performance_report",
    ],
    
    # Admin tools (full access)
    "admin": [
        "refund_payment",
        "generate_audit_report",
        "export_compliance_data",
        "validate_pci_compliance",
        "get_audit_trail",
    ],
}

__all__ = [
    "TOOL_REGISTRY",
    "TOOL_CATEGORIES", 
    "TOOL_DESCRIPTIONS",
    "TOOL_PERMISSIONS",
]
