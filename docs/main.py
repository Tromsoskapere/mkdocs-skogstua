# docs/main.py
import os
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

def define_env(env):
    """
    This is the hook for the macros plugin.
    'env' is an object that contains the page, config, and other site data.
    """
    @env.macro
    def list_folder_contents():
        """
        Generates a Markdown list of all pages in the same directory as the current page.
        """
        # Get the directory of the current page
        current_dir = os.path.dirname(env.page.file.src_path)
        
        # Find all pages that are in the same directory
        sibling_pages = [
            p for p in env.pages 
            if os.path.dirname(p.file.src_path) == current_dir
        ]
        
        # Sort the pages alphabetically by title for a consistent order
        sibling_pages.sort(key=lambda p: p.title)
        
        # If no siblings are found, return an empty string
        if not sibling_pages:
            return ""

        # Build the Markdown list
        output = ["## Pages in this section\n"]
        for page in sibling_pages:
            # Don't link to the current page itself, just list its title
            if page.url == env.page.url:
                output.append(f"- **{page.title}**")
            else:
                output.append(f"- [{page.title}]({page.url})")
        
        # Join the list into a single string and return it
        return "\n".join(output)
