import markdown

def generate_html_content(final_state):
    dependencies = final_state["dependencies"]
    install_commands = final_state["installCommands"]
    gitignore_suggestions = final_state["gitignoreSuggestions"]
    env_suggestions = final_state["envSuggestions"]
    prettier_suggestions = final_state["prettierSuggestions"]
    vitest_suggestions = final_state["vitestSuggestions"]
    eslint_suggestions = final_state["eslintSuggestions"]

    # Styling the list
    dependencies_html = "<ul>" + "".join(f"<li>{dep}</li>" for dep in dependencies) + "</ul>" if dependencies else "<p>No dependencies found.</p>"
    install_commands_html = "<ul>" + "".join(f"<li>{cmd}</li>" for cmd in install_commands) + "</ul>" if install_commands else "<p>No install commands suggested.</p>"

    gitignore_html = markdown.markdown(gitignore_suggestions) if gitignore_suggestions else "<p>No suggestions.</p>"
    env_html = markdown.markdown(env_suggestions) if env_suggestions else "<p>No suggestions.</p>"
    prettier_html = markdown.markdown(prettier_suggestions) if prettier_suggestions else "<p>No suggestions.</p>"
    vitest_html = markdown.markdown(vitest_suggestions) if vitest_suggestions else "<p>No suggestions.</p>"
    eslint_html = markdown.markdown(eslint_suggestions) if eslint_suggestions else "<p>No suggestions.</p>"

    html_content = f"""
    <html>
    <head>
    </head>
    <body>
        <h1>AI Suggestions Report</h1>
        <div class="section">
            <h2>Dependencies</h2>
            {dependencies_html}
        </div>
        <div class="section">
            <h2>Install Commands</h2>
            {install_commands_html}
        </div>
        <div class="section">
            <h2>Gitignore Suggestions</h2>
            {gitignore_html}
        </div>
        <div class="section">
            <h2>Env Suggestions</h2>
            {env_html}
        </div>
        <div class="section">
            <h2>Prettier Suggestions</h2>
            {prettier_html}
        </div>
        <div class="section">
            <h2>Vitest Suggestions</h2>
            {vitest_html}
        </div>
        <div class="section">
            <h2>ESLint Suggestions</h2>
            {eslint_html}
        </div>
        <div class="section">
            <a href="/download">Download PDF</a>
        </div>
    </body>
    </html>
    """
    return html_content
