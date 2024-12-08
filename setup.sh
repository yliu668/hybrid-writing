mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"yl1913@georgetown.edu\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml