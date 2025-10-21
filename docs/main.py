# docs/main.py

def define_env(env):
    """
    This is the hook for the macros plugin.
    """
    @env.macro
    def hello_world():
        """
        A simple test macro.
        """
        return "### Hello from the macro! The GitHub Actions build works."