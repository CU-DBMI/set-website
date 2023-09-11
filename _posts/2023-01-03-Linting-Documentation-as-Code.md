---
title: "Tip of the Week: Linting Documentation as Code"
author: dave-bunten
tags:
  - tip-of-the-week
  - software
  - documentation
  - docsascode
  - linting
  - staticanalysis
---

# Tip of the Week: Linting Documentation as Code

{% include tip-of-the-week-intro.html %}

<!-- excerpt start -->

[Software documentation](https://en.wikipedia.org/wiki/Software_documentation) is sometimes treated as a less important or secondary aspect of software development. Treating documentation as code allows developers to version control the shared understanding and knowledge surrounding a project. Leveraging this paradigm also enables the use of tools and patterns which have been used to strengthen code maintenance. This article covers one such pattern: [linting](https://en.wikipedia.org/wiki/Lint_(software)), or static analysis, for documentation treated like code.

<!-- excerpt end -->

__TLDR (too long, didn't read);__
There are many linting tools available which enable quick revision of your documentation. Try using [codespell](https://github.com/codespell-project/codespell) for spelling corrections, [mdformat](https://github.com/executablebooks/mdformat) for markdown file formatting corrections, and [vale](https://vale.sh/) for more complex editorial style or natural language assessment within your documentation.

## Spelling Checks

{% capture col1content %}

```markdown
<!--- readme.md --->
## Example Readme

Thsi project is a wokr in progess.
Code will be updated by the team very often.

(CU Anschutz)[https://www.cuanschutz.edu/]
```

_Example readme.md with incorrectly spelled words_
{% endcapture %}
{% capture col2content %}

```console
% codespell readme.md
readme.md:4: Thsi ==> This
readme.md:4: wokr ==> work
readme.md:4: progess ==> progress



```

_Example showing codespell detection of mispelled words_
{% endcapture %}
{% include cols.html col1=col1content col2=col2content %}

[Spelling checks](https://en.wikipedia.org/wiki/Spell_checker) may be used to automatically detect incorrect spellings of words within your documentation (and code!). [Codespell](https://github.com/codespell-project/codespell) is one library which can lint your word spelling. Codespell may be used through the command-line and also through a [pre-commit](https://pre-commit.com/index.html) hook.

## Markdown Format Linting

{% capture col1content %}

```markdown
<!--- readme.md --->
## Example Readme

This project is a work in progress.
Code will be updated by the team very often.

(CU Anschutz)[https://www.cuanschutz.edu/]
```

_Example readme.md with markdown issues_
{% endcapture %}
{% capture col2content %}

```console
% markdownlint readme.md
readme.md:2 MD041/first-line-heading/first-line-h1
First line in a file should be a top-level heading
[Context: "## Example Readme"]
readme.md:6:5 MD011/no-reversed-links Reversed link
syntax [(link)[https://www.cuanschutz.edu/]]

```

_Example showing markdownlint detection of issues_
{% endcapture %}
{% include cols.html col1=col1content col2=col2content %}

The format of your documentation files may also be linted for common issues. This may catch things which are otherwise hard to see when editing content. It may also improve the overall [web accessibility](https://en.wikipedia.org/wiki/Web_accessibility) of your content, for example, through proper HTML header order and image alternate text. [Markdownlint](https://github.com/markdownlint/markdownlint) is one library which can be used to find issues within markdown files.

Additional and similar resources to explore in this area:

- [restructuredtext-lint](https://github.com/twolfson/restructuredtext-lint) - for linting RST files
- [mdformat](https://github.com/executablebooks/mdformat) - an additional markdown linter

## Editorial Style and Grammar

{% capture col1content %}

```markdown
<!--- readme.md --->
# Example Readme

This project is a work in progress.
Code will be updated by the team very often.

[CU Anschutz](https://www.cuanschutz.edu/)
```

_Example readme.md with questionable editorial style_
{% endcapture %}
{% capture col2content %}

```console
% vale readme-example.md
readme-example.md
2:12  error    Did you really mean 'Readme'?   Vale.Spelling
5:11  warning  'be updated' may be passive     write-good.Passive
               voice. Use active voice if you
               can.
5:34  warning  'very' is a weasel word!        write-good.Weasel
```

_Example showing vale warnings and errors_
{% endcapture %}
{% include cols.html col1=col1content col2=col2content %}

Maintaining consistent editorial style and grammar may also be a focus within your documentation. These issues are sometimes more difficult to detect and more opinionated in nature. In some cases, organizations publish guides on this topic (see [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/), or [Google Developer Documenation Style Guide](https://developers.google.com/style)). Some of the complexity of writing style may be linted through tools like [Vale](https://vale.sh/). Using common configurations through Vale can unify how language is used within your documentation by linting for common style and grammar.

Additional and similar resources to explore in this area:

- [textlint](https://textlint.github.io/) - similar to Vale with a modular approach

## Resources

Please see the following the resources on this topic.

- [codespell](https://github.com/codespell-project/codespell) - a code and documentation spell checker.
- [markdownlint](https://github.com/markdownlint/markdownlint) - markdown linter.
- [mdformat](https://github.com/executablebooks/mdformat) - another markdown linter.
- [restructuredtext-lint](https://github.com/twolfson/restructuredtext-lint) - RST file format linter.
- [vale](https://vale.sh/) - an editorial style linter.
- [textlint](https://textlint.github.io/) - another editorial style linter with greater modularity.
