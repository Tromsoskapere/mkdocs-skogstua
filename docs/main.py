# docs/main.py
import mkdocs_macros

def define_env(env):
    """
    This is the hook for defining variables, macros and filters
    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """
    
    @env.macro
    def list_siblings_and_children():
        """
        Returns a Markdown list of siblings and children of the current page.
        """
        if not env.page or not env.page.ancestors:
            return ""
        
        # The parent section is the last ancestor
        parent_section = env.page.ancestors[-1]
        
        if not parent_section.children:
            return ""

        output = ["## Pages in this Section\n"]
        for item in parent_section.children:
            if item.is_page:
                # Check if it's the current page to add a class or marker
                active_marker = " (Active)" if item == env.page else ""
                output.append(f"- [{item.title}]({item.url}){active_marker}")
            elif item.is_section:
                output.append(f"- **{item.title}**")
                for child_page in item.children:
                    active_marker = " (Active)" if child_page == env.page else ""
                    output.append(f"  - [{child_page.title}]({child_page.url}){active_marker}")
        
        return "\n".join(output)
