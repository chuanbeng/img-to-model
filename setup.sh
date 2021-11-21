mkdir -p ~/.streamlit/
echo "
[general]n
email = "chuanbeng.tay@gmail.com"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
port = $PORTn
enableCORS = falsen
" > ~/.streamlit/config.toml