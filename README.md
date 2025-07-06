# OSC Server with VLC HTTP Control

This project is an OSC ([Open Sound Control](https://opensoundcontrol.stanford.edu/index.html)) Server that listens for OSC messages. The aim is to pair this with a client like [Open Stage Control](https://openstagecontrol.ammd.net/) and performs actions on your server/computer.

I'm using it to have an intelligent **Controller** while playing some simulation games, but the sky is the limit.

I start using it to have some kind of radio for driving, so I will probably will be adding more and more functionality!

## Features
- Listens for OSC messages on a specified port.
- It's really simple and fast.
- Modular design with handlers for different types of OSC messages.
- Secure handling of credentials using environment variables.
- Handles different OSC addresses to control VLC (e.g., play, pause, volume).
- Easy way to run/load/execute .exe programs, for ex Steam games.
- Handle Spotify actions, so you can control a spotify account directly.
- Fearly easy way to debug.
- Nice logging to see if something is not ok.

## Disclaimer
For now, this project is just something that make my life easy, if that works for you, you are welcome to try it. I will be adding stuff in the future, but this is not my priority and as you can imagine by the code is the first time I use python like this, and I'm just having fun learning and using it. 

## Usage Prerequisites
Before running the project, ensure you have the following installed:

- [Python 3.12](https://www.python.org/downloads/) or higher.
- ~~[poetry](https://github.com/python-poetry/poetry) to manage the dependencies.~~ (hopefully soon!)
- (Optional) [VS Code](https://code.visualstudio.com/).
- (Optional) [VLC Media Player](https://www.videolan.org/) with the [Lua HTTP](https://code.videolan.org/videolan/vlc/-/blob/master/share/lua/README.txt) interface enabled.
- Developer account from Spotify, you will need to register an app, and get the credentials.

## Installation / Debug

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Rename the `.env.example` file in the root directory and fill the following content replacing the values:
    ```
    VLC_USERNAME=your_vlc_username
    VLC_PASSWORD=your_vlc_password
    ```

## Usage

1. **Start the OSC server:**

    Run the following command to start the OSC server:
    ```bash
    python main.py
    ```

2. **Send OSC messages:**

    Use an OSC client (e.g., [Open Stage Control](https://openstagecontrol.ammd.net/), TouchOSC, OSCulator) to send messages to the server.
    
    The server listens on localhost at port 8001 by default.

    You will get a nice log in the console.

3. **Stop the server:**

    No nice way yet, just press ``ctrl+c`` multiple times in the console. Yes I really don't like that, I will learn/figure it out a better way soon.

## Proyect structure

    pyOSCSrv/
    ├── .vscode/                    # VS Code configuration folder
    │   ├── launch.json             # Configuration for the debugger
    │   ├── settings.json           # Several configs
    ├── handlers/                   # OSC message handlers
    │   ├── base_handler.py         # Base handler class
    │   ├── exec_handler.py         # Handler for exec commands
    │   ├── http_handler.py         # Handler for HTTP requests
    │   ├── http_vlc_handler.py     # Handler for VLC-specific commands
    │   ├── ping_handler.py         # Handler to know if the server is alive
    │   ├── spotify_handler.py      # Handler to send Spotify commands
    │   ├── taskkill_handler.py     # Handler to kill a know process
    ├── .gitignore                  # Files to ignore in Git
    ├── .env.example                # Example environment variables file
    ├── handler_factory.py          # Factory to know wich handler is the best
    ├── logger.py                   # Logger configuration
    ├── main.py                     # Main script to start the OSC server
    ├── README.md                   # This file
    ├── requirements.txt            # List of dependencies
    └── run.ps1                     # Easy script tu run the server

## Contributing
Contributions are more than welcome! If you'd like to contribute in any way, please follow these steps:

    1. Fork the repository.
    2. Create a new branch (git checkout -b feature/YourFeatureName).
    3. Commit your changes (git commit -m 'Add some feature').
    4. Push to the branch (git push origin feature/YourFeatureName).
    5. Open a pull request.

As I'm just starting with python, some nice comments with the pull request will be nice.

## License
This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the [python-osc](https://pypi.org/project/python-osc/) library for making OSC communication easy, awesome library.
- Thanks to [VLC](https://www.videolan.org/) for providing an awesome software with a powerful HTTP interface for media control.
- Thanks to [Open Stage Control](https://openstagecontrol.ammd.net/) without that app I will not have the will to program this, thanks **jean-emmanuel** awesome software you got there.
- Thanks to **muchimi**, And all his improvements in [JoystickGremlinEx](https://github.com/muchimi/JoystickGremlinEx). Your project gave me the strength and motivation to dive into the world of Python. I would love to have the knowledge to collaborate in the future.