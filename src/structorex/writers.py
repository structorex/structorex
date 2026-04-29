import json
import logging
import os
import html

logger = logging.getLogger(__name__)

class ReportWriter:
    def __init__(self, config):
        self.config = config

    def write(self, visitor):
        raise NotImplementedError

class TextReportWriter(ReportWriter):
    def write(self, visitor):
        try:
            with open(self.config.output_file, "w", encoding="utf-8") as f:
                f.write("PROJECT STRUCTURE:\n")
                f.write("\n".join(visitor.structure))
                f.write("\n\nFILE CONTENTS:")
                for path, content in visitor.content_dict.items():
                    f.write(f"\n{'='*50}\nFile: {path}\n{'='*50}\n{content}")
            logger.info(f"Report successfully saved to: {self.config.output_file}")
        except Exception as e:
            logger.error(f"ERROR saving report: {e}")
            raise

class MarkdownReportWriter(ReportWriter):
    def write(self, visitor):
        try:
            with open(self.config.output_file, "w", encoding="utf-8") as f:
                f.write(f"# Project Report\n\n")
                f.write(f"- **Root:** `{self.config.root_path}`\n")
                f.write(f"- **Total Files Scanned:** {visitor.total_files}\n")
                f.write(f"- **Total Lines:** {visitor.total_lines}\n\n")
                
                f.write("## Structure\n```text\n")
                f.write("\n".join(visitor.structure))
                f.write("\n```\n\n## File Contents\n\n")
                
                for path, content in visitor.content_dict.items():
                    ext = os.path.splitext(path)[1][1:] # without dot
                    f.write(f"### `{path}`\n")
                    if content.startswith("["):
                        f.write(f"{content}\n\n")
                    else:
                        f.write(f"```{ext}\n{content}\n```\n\n")
                        
            logger.info(f"Markdown report successfully saved to: {self.config.output_file}")
        except Exception as e:
            logger.error(f"ERROR saving report: {e}")
            raise

class JsonReportWriter(ReportWriter):
    def write(self, visitor):
        try:
            report = {
                "metadata": {
                    "root": self.config.root_path,
                    "total_files": visitor.total_files,
                    "total_lines": visitor.total_lines
                },
                "structure": visitor.structure,
                "contents": visitor.content_dict
            }
            with open(self.config.output_file, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=2)
            logger.info(f"JSON report successfully saved to: {self.config.output_file}")
        except Exception as e:
            logger.error(f"ERROR saving report: {e}")
            raise

class HtmlReportWriter(ReportWriter):
    def write(self, visitor):
        try:
            with open(self.config.output_file, "w", encoding="utf-8") as f:
                f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
                f.write('<meta charset="utf-8">\n<title>Project Report</title>\n')
                f.write('<style>\n')
                f.write('body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; display: flex; height: 100vh; margin: 0; background: #fff; color: #24292e; }\n')
                f.write('#sidebar { width: 350px; overflow-y: auto; background: #f6f8fa; padding: 15px; border-right: 1px solid #e1e4e8; }\n')
                f.write('#content { flex-grow: 1; padding: 20px; overflow-y: auto; }\n')
                f.write('.tree-line { font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace; white-space: pre; margin: 2px 0; font-size: 13px; }\n')
                f.write('.file-link { cursor: pointer; color: #0366d6; text-decoration: none; }\n')
                f.write('.file-link:hover { text-decoration: underline; }\n')
                f.write('.skipped-file { color: #6a737d; }\n')
                f.write('pre { background: #f6f8fa; padding: 16px; border-radius: 6px; overflow: auto; border: 1px solid #e1e4e8; font-size: 13px; line-height: 1.45; }\n')
                f.write('.file-content-view { display: none; }\n')
                f.write('.file-content-view.active { display: block; }\n')
                f.write('</style>\n</head>\n<body>\n')
                
                f.write('<div id="sidebar">\n')
                f.write(f'<h3>Project Structure</h3>\n')
                f.write(f'<p style="font-size: 12px; color: #586069;">Files: {visitor.total_files} | Lines: {visitor.total_lines}</p>\n')
                f.write('<div>\n')
                
                # Render tree
                for node in visitor.structure_data:
                    prefix = html.escape(node["prefix"] + node["connector"])
                    name = html.escape(node["name"])
                    
                    if node["type"] == "file":
                        safe_path = html.escape(node["path"])
                        f.write(f'<div class="tree-line">{prefix}<a class="file-link" onclick="showContent(\'{safe_path}\')">{name}</a></div>\n')
                    elif node["type"] == "skipped":
                        f.write(f'<div class="tree-line"><span class="skipped-file">{prefix}{name} [skipped]</span></div>\n')
                    else: # dir
                        f.write(f'<div class="tree-line">{prefix}<b>{name}/</b></div>\n')
                
                f.write('</div>\n</div>\n')
                
                f.write('<div id="content">\n')
                f.write('<h2 id="placeholder" style="color: #586069; text-align: center; margin-top: 20%;">Select a file from the sidebar to view its content.</h2>\n')
                
                # Render contents
                for path, content in visitor.content_dict.items():
                    safe_path = html.escape(path)
                    safe_content = html.escape(content)
                    f.write(f'<div id="{safe_path}" class="file-content-view">\n')
                    f.write(f'<h3>{safe_path}</h3>\n')
                    f.write(f'<pre><code>{safe_content}</code></pre>\n')
                    f.write('</div>\n')
                
                f.write('</div>\n')
                
                f.write('<script>\n')
                f.write('function showContent(path) {\n')
                f.write('  document.getElementById("placeholder").style.display = "none";\n')
                f.write('  document.querySelectorAll(".file-content-view").forEach(function(el) { el.classList.remove("active"); });\n')
                f.write('  var target = document.getElementById(path);\n')
                f.write('  if (target) target.classList.add("active");\n')
                f.write('}\n')
                f.write('</script>\n')
                f.write('</body>\n</html>')
            logger.info(f"HTML report successfully saved to: {self.config.output_file}")
        except Exception as e:
            logger.error(f"ERROR saving report: {e}")
            raise

def get_writer(config):
    if config.output_format == "json":
        return JsonReportWriter(config)
    elif config.output_format == "markdown":
        return MarkdownReportWriter(config)
    elif config.output_format == "html":
        return HtmlReportWriter(config)
    else:
        return TextReportWriter(config)
