# mk-docs

## Theme

We use the [Material theme](https://squidfunk.github.io/mkdocs-material/) for MK Docs. You can find the updated features in the theme [specimen](https://squidfunk.github.io/mkdocs-material/specimen/). We also run most of the [available extensions](https://squidfunk.github.io/mkdocs-material/extensions/).

### Example configurations

!!! tip "Learn from running projects"
    Here there is a list of projects using mkdocs in different ways for documenting various things:

    - SmartCitizen Docs: https://docs.smartcitizen.me
    - Fabacademy Barcelona Local Docs: https://fablabbcn-projects.gitlab.io/learning/fabacademy-local-docs/
    - This documentation: https://knowledge.fablabbcn.org

## Customization

You can deeply customize it by simply editing the the `mkdocs.yml` file the root folder [mkdocs.yml](https://github.com/fablabbcn/knowledge/blob/master/mkdocs.yml).

An interesting feature is the possibility to manually customize navigation. See [Smart Citizen Docs](https://github.com/fablabbcn/smartcitizen-docs/blob/master/mkdocs.yml) as an example.

## Automation

We use [Github Action](https://docs.github.com/en/actions) to automatically update [knowledge.fablabbcn.org](https://knowledge.fablabbcn.org/) every time you commit a change. 

Currently we run a single workflow to simply build the site like `mkdocs build` but more complex features are possible. Find an example [here](https://github.com/fablabbcn/knowledge/blob/master/.github/workflows/main.yml).