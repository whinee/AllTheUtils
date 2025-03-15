## Define mini-templates for each portion of the document.

## Top Dependencies

<%def name="h2(s)">## ${s}
</%def>

<%def name="h3(s)">### ${s}
</%def>

<%def name="h4(s)">#### ${s}
</%def>

<%def name="heading(s, level=1)">
<%
    hashtags = "#" * level
%>
${hashtags} ${s}
</%def>

<%!
    def indent(s, spaces=4):
        new = s.replace('\n', '\n' + ' ' * spaces)
        return ' ' * spaces + new.strip()
%>

<%!
    def submodule_list_item(submodule):
        name = submodule.name
        return f"- [{name}](./" + name.split(".")[-1] + ('/index' if submodule.is_package else '') + ".md)"
%>

<%!
    def go_back_to_index(module, top_bar: bool = False, bottom_bar: bool = False):
        bar = "---"
        name = module.name
        name_parts = name.split(".")
        if len(name_parts) == 1:
            return ""
        dots_multiplier = 1
        if module.is_package:
            dots_multiplier = 2
        return ("\n\n" + bar if top_bar else "") + "\n\n[← Go back to `" + ".".join(name_parts[:-1]) + f"`]({"." * dots_multiplier}/index.md)\n\n" + (bar + "\n\n" if bottom_bar else "")
%>

<%def name="function(func, level=2)" buffered="True">
<%
    returns = show_type_annotations and func.return_annotation() or ''
    if returns:
        returns = ' → ' + returns
%>
${heading(f"`{func.name}`", level)}
```python
(${", ".join(func.params(annotate=show_type_annotations))})${returns}
```

${func.docstring}
</%def>

<%def name="variable(var, level=2)" buffered="True">
<%
    annot = show_type_annotations and var.type_annotation() or ''
    if annot:
        annot = f"\n\n```python\n{annot}\n```"
%>
${heading(f"`{var.name}`", level)}${annot}

${var.docstring}
</%def>

<%def name="class_(cls, level)" buffered="True">
${heading(f"`{cls.name}`", level)}<%
annotation_ls = cls.params(annotate=show_type_annotations)
if not len(annotation_ls):
    annotation = ""
else:
    annotation = f'```python\n({", ".join(annotation_ls)})\n```'
%>
${annotation}

${cls.docstring}
<%
  class_vars = cls.class_variables(show_inherited_members, sort=sort_identifiers)
  static_methods = cls.functions(show_inherited_members, sort=sort_identifiers)
  inst_vars = cls.instance_variables(show_inherited_members, sort=sort_identifiers)
  methods = cls.methods(show_inherited_members, sort=sort_identifiers)
  mro = cls.mro()
  subclasses = cls.subclasses()
%>
% if mro:
${h4('Ancestors (in MRO)')}
% for c in mro:
- ${c.refname}
% endfor

% endif
% if subclasses:
${h4('Descendants')}
% for c in subclasses:
- ${c.refname}
% endfor

% endif
% if class_vars:
${h4('Class variables')}
% for v in class_vars:
${variable(v, 5)}
% endfor
% endif
% if static_methods:
${h4('Static methods')}
% for f in static_methods:
${function(f, 5)}

% endfor
% endif
% if inst_vars:
${h4('Instance variables')}
% for v in inst_vars:
${variable(v, 5)}

% endfor
% endif
% if methods:
${h4('Methods')}
% for m in methods:
${function(m, 5)}

% endfor
% endif
</%def>


## Start the output logic for an entire module.

<%
  variables = module.variables(sort=sort_identifiers)
  classes = module.classes(sort=sort_identifiers)
  functions = module.functions(sort=sort_identifiers)
  submodules = module.submodules()
  heading = 'Namespace' if module.is_namespace else 'Module'
%>

# ${heading} ${module.name}
## =${'=' * (len(module.name) + len(heading))}

${module.docstring.strip()}


${go_back_to_index(module)}
% if submodules:
${h2('Sub-modules')}
    % for m in submodules:
${submodule_list_item(m)}
    % endfor
% endif

% if variables:
${h2('Variables')}
    % for v in variables:
${variable(v, 3)}

    % endfor
% endif

% if functions:
${h2('Functions')}
    % for f in functions:
${function(f, 3)}

    % endfor
% endif

% if classes:
${h2('Classes')}
    % for c in classes:
${class_(c, 3)}

    % endfor
% endif
${go_back_to_index(module, top_bar=True)}
