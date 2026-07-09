from langgraph.graph import StateGraph, END

from ai_agent.state import AgentState
from ai_agent.tools import (
    log_interaction,
    edit_interaction,
    search_hcp,
    interaction_summary,
    next_best_action,
)

def agent_node(state: AgentState):
    user_input = state["user_input"].lower()

    if "edit" in user_input:
        response = edit_interaction.invoke({"user_input": user_input})

    elif "search" in user_input:
        response = search_hcp.invoke({"user_input": user_input})

    elif "summary" in user_input:
        response = interaction_summary.invoke({"user_input": user_input})

    elif "next" in user_input or "follow" in user_input:
        response = next_best_action.invoke({"user_input": user_input})

    else:
        response = log_interaction.invoke({"user_input": user_input})

    return {
        "user_input": user_input,
        "response": response,
    }



builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)

builder.set_entry_point("agent")

builder.add_edge("agent", END)

graph = builder.compile()