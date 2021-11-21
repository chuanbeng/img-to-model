mkdir -p ~/.streamlit/
echo "
[general]n
email = "chuanbeng.tay@gmail.com"n
" > ~/.streamlit/credentials.toml
echo "
[server]\nheadless = true\nenableCORS=false\nport = \n
" > ~/.streamlit/config.toml