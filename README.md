## WWSimulaTOR

Basic simulation of a WabiSabi making test request through new tor circuits every time.
Some specificities are not replicated for sake of simplicity but it should be pretty representative.
Sorry for code in Python, if you want to change behavior, add parameters or functionnalities (like A/B testing) please contact me or PR.

Config in `config.py`.
Past runs in `testruns.txt`

### Usage
Prerequisites: tor, python3

`tor --controlport 9051`
`python3 main.py`

