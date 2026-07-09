from langchain_core.tools import tool


@tool
def log_interaction(user_input: str) -> str:
    """Log HCP interaction."""
    return f"Interaction logged successfully: {user_input}"


@tool
def edit_interaction(user_input: str) -> str:
    """Edit an existing interaction."""
    return f"Interaction updated: {user_input}"


@tool
def search_hcp(user_input: str) -> str:
    """Search HCP details."""
    return f"HCP search result for: {user_input}"


@tool
def interaction_summary(user_input: str) -> str:
    """Generate interaction summary."""
    return f"Summary: {user_input}"


@tool
def next_best_action(user_input: str) -> str:
    """Suggest next best action."""
    return "Follow up with the HCP within the next 7 days."