# Template: Python - Actions

This template gets you started in creating Actions for [Robocorp Action Server](https://github.com/robocorp/robo/tree/master/action_server/docs#readme).

`Actions` and `Action Server` enable you to "give your AI Agents hands" meaning that your AI/LLM Agent can help your users perform distinct actions that get executed based on the LLM discussion.

You can get this template just by cloning from here or by running the command `action-server new` as per the installation instructions of [Action Server](https://github.com/robocorp/robo/tree/master/action_server/docs#readme)

To get full functionality in VS Code, we recommend getting our [Robocorp Code](https://robocorp.com/docs/developer-tools/visual-studio-code) -extension. With the extension in place, you get a simple way to:
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
* [Robocorp Documentation -site](https://robocorp.com/docs)
* [Portal for more examples](https://robocorp.com/portal)