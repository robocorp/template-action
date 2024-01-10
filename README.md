# Template: Python - Actions

This template gets you started in creating Actions for [Robocorp Action Server](https://github.com/robocorp/robo/tree/master/action_server/docs#readme).

`Actions` and `Action Server` enable you to "give your AI Agents hands" meaning that your AI/LLM Agent can help your users perform distinct actions that get executed based on the LLM discussion.

## Quickstart

Install Robocorp Action Server with pip:

```sh
pip install action-server
```

Bootstrap a new project using this template. You’ll be prompted for a name of the project (directory):

```sh
action-server new
```

2. Start Action Server in the :

```sh
cd my-project
action-server start --expose
```

Once that’s done, you’ll have an Action Server UI locally (by default at [http://localhost:8080](http://localhost:8080)), and a public internet-facing URL (something like "https://twently-cuddly-dinosaurs.robocorp.link").

## Dependency management

Action Server uses [./conda.yaml](conda.yaml) file serving as the configuration file for managing the environment in which your actions runs. It specifies the dependencies and packages required, ensuring that each run happens in a clean and repeatable environment.

To add a new dependency, simply add them to the pip section of the [./conda.yaml](conda.yaml) depependencies:

```yaml
channels:
  - conda-forge

dependencies:
  - python=3.10.12
  - pip=23.2.1
  - robocorp-truststore=0.8.0
  - pip:
      - robocorp==1.3.0
      - numpy==2023.3
```

## Environment management

- Run and debug your Python Action code
- Running the Actions Server on your machine for local testing
- Run and expose your Action Server to the internet behind a unique URL and key so that you can set up your AI Agent to test the full E2E developer preview of the whole setup.

The template leverages the new Python open-source structure from [robocorp -libraries](https://github.com/robocorp/robo#libraries).

The template provides you with the basic structure of a Python project: logging out of the box and controlling your action without fiddling with the base Python stuff. The environment contains the most used libraries, so you do not have to start thinking about those right away.

👉 After running the bot, check out the `log.html` under the `output` -folder.

The action here is just a simple current date time-getter, leaving you with a canvas to paint on.

Do note that with Robocorp tooling, you:

- Do NOT need Python installed
- You do not need to write `pip install ...`; the [conda.yaml](conda.yaml) is here for a reason.
- You do not need to worry about Python's main -functions and, most importantly, the logging setup

🚀 Now, go get'em

For more information, do not forget to check out the following:

- [Robocorp Documentation -site](https://robocorp.com/docs)
- [Portal for more examples](https://robocorp.com/portal)
