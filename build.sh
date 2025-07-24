curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
source .venv/bin/activate
reflex init
reflex export
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
