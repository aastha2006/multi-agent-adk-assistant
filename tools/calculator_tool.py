from google.adk.tools import Tool

def calculator_func(expression: str) -> str:
    """Evaluates a mathematical expression."""
    try:
        # malicious code execution risk, but acceptable for this demo context as per instructions
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

calculator_tool = Tool(
    name="calculator",
    description="Evaluate mathematical expressions",
    func=calculator_func
)
